from flask import Flask,render_template,request,session,make_response,redirect,url_for
from db_config import mysql
from flask_restful import Resource
import pymysql,sys,hashlib

#HomePage Class to redirect to Homepage/Login Page
class homePage(Resource):
    def get(self):
        return redirect(url_for('login'))
    
#this class is used to create users
class signUpAPI(Resource):
    def post(self):
        try:
            
            if 'username' in request.form and 'password' in request.form:
                username = request.form['username']
                password = request.form['password']
                hashed_pass = hashlib.md5(password.encode()).hexdigest()
                name = request.form['name']
                email = request.form['email']
                phone = request.form['phone']
                conn = mysql.connect()
                cur = conn.cursor(pymysql.cursors.DictCursor)
                cur.execute("select * from users where username = %s ",(username))
                userData = cur.fetchone()
                cur.close()
                if userData:
                    message = "Please use diffrent username"
                    return redirect(url_for('signup',message =message ))
                else:
                    conn = mysql.connect()
                    cur = conn.cursor(pymysql.cursors.DictCursor)
                    cur.execute("insert into users (name,username,password,email,phone_no) values (%s ,%s,%s,%s,%s)",(name,username,hashed_pass,email,phone))
                    conn.commit()
                    cur.close()
                    message = "user created processed with login"
                    return redirect(url_for('signup',message =message ))
            else:
                return redirect(url_for('signup'))
        except Exception as e:
            print(e)
    def get(self):
        try:
            print('[get]')
            if request.args.get('message'):
                message = request.args.get('message')
                return make_response(render_template('signup.html',message =message))
            else:
                return make_response(render_template('signup.html'))
        except Exception as e:
            print(e)


#LoginApi Class used to authenticate user if username and password is correct
class loginAPI(Resource):
    def post(self):
        try:
            if 'loggedin' in session:
                return redirect(url_for('book'))
            else:
                if 'username' in request.form and 'password' in request.form:
                    username = request.form['username']
                    password = request.form['password']
                    hashed_pass = hashlib.md5(password.encode()).hexdigest()
                    conn = mysql.connect()
                    cur = conn.cursor(pymysql.cursors.DictCursor)
                    cur.execute("select * from users where username = %s ",(username))
                    userexist = cur.fetchone()
                    print(userexist)
                    if userexist:
                        cur.execute("select * from users where username = %s and password = %s",(username,hashed_pass))
                        userData = cur.fetchone()
                        cur.close()
                        if userData:
                            session['loggedin'] = True
                            session['id'] = userData['id']
                            session['isAdmin'] = userData['isAdmin']
                            message = "Logged In successfully"
                            return redirect(url_for('book'))
                        else:
                            message = "Please enter correct username/password"
                            print(message)
                            return redirect(url_for('login',message =message ))
                    else:
                        message = "User not found please signup"
                        print(message)
                        return redirect(url_for('signup',message =message ))
                else:
                    message = "else"
                    print(message)
                    return redirect(url_for('login'))
        except Exception as e:
            print(e)
    def get(self):
        try:
            if request.args.get('message'):
                message = request.args.get('message')
                return make_response(render_template('login.html',message =message))
            else:
                return make_response(render_template('login.html'))
        except Exception as e:
            print(e)

# logout Class used to logout user which currently loggedin
class logout(Resource):
    def get(self):
        try:
            session.pop('loggedin',None)
            session.pop('id',None)
            session.pop('isAdmin',None)
            return redirect(url_for('login'))
        except Exception as e:
            print(e)

#this class is used to fetch users
class userlist(Resource):
    def get(self):
        try:
            if 'loggedin' in session:
                if session['isAdmin'] == 'true':
                    userid = request.args.get('userId')
                    conn = mysql.connect()
                    cur = conn.cursor(pymysql.cursors.DictCursor)
                    if request.args.get('userId'):
                        cur.execute("select * from users where id=%s",(int(userid)))
                        users = cur.fetchall()
                        cur.execute("select * from book_log bl join book b on bl.book_id=b.id where user_id = %s",(int(userid)))
                        books = cur.fetchall()
                    else:
                        cur.execute("select * from users")
                        users = cur.fetchall()
                   
                    print(users)
                    message = "Fetch All Users"
                    if request.args.get('userId'):
                        return make_response(render_template('user-view.html',userdetails = users,booksdetails=books))
                    else:
                        return make_response(render_template('users.html',userslist = users))
                else:
                    return redirect(url_for('book'))
            else:
                message = 'User not login'
                return make_response(render_template('login.html'))
        except Exception as e:
            print(e)


# this class is used for return book
class bookReturn(Resource):
    def get(self):
        try:
            if 'loggedin' in session:
                if request.args.get('booklogId') and request.args.get('bookId'):
                    booklogId = request.args.get('booklogId')
                    userid = session['id']
                    bookId = request.args.get('bookId')
                    conn = mysql.connect()
                    cur = conn.cursor(pymysql.cursors.DictCursor)
                    cur.execute("update book_log set return_date= CURRENT_TIMESTAMP(),status=0\
                                where id=%s",(int(booklogId)))
                    cur.execute("update book set status=1\
                                where id=%s",(int(bookId)))
                    conn.commit()
                    cur.execute("select * from book_log bl join book b on bl.book_id=b.id where user_id = %s",(userid))
                    books = cur.fetchall()
                    print(books)
                    message = "Fetch All Books Logs"
                    if session['isAdmin'] == 'true':
                        return make_response(render_template('collection.html',booksdetails = books,isAdmin='true'))
                    else:
                        return make_response(render_template('collection.html',booksdetails = books))
            else:
                message = 'User not login'
                return make_response(render_template('login.html'))
        except Exception as e:
            print(e)

# this class is used for borrow book
class bookBorrow(Resource):
    def get(self):
        try:
            if 'loggedin' in session:
                if request.args.get('bookId'):
                    bookId = request.args.get('bookId')
                    userid = session['id']
                    isAdmin = session['isAdmin']
                    conn = mysql.connect()
                    cur = conn.cursor(pymysql.cursors.DictCursor)
                    cur.execute("update book set status=0\
                                where id=%s",(int(bookId)))
                    cur.execute("insert into book_log (book_id,user_id,status,remark) values (%s ,%s,%s,%s)",\
                                    (bookId,userid,1,''))
                    conn.commit()
                    cur.execute("select * from book_log bl join book b on bl.book_id=b.id where user_id = %s",(userid))
                    books = cur.fetchall()
                    print(books)
                    message = "Fetch All Books Logs"
                    if session['isAdmin'] == 'true':
                        return make_response(render_template('collection.html',booksdetails = books,isAdmin='true'))
                    else:
                        return redirect(url_for('book'))
            else:
                message = 'User not login'
                return make_response(render_template('login.html'))
        except Exception as e:
            print(e)

# this class is used for to view borrow books
class mycollection(Resource):
    def get (self):
        try:
            
            if 'loggedin' in session:
                userid = session['id']
                isAdmin  = session['isAdmin']
                conn = mysql.connect()
                cur = conn.cursor(pymysql.cursors.DictCursor)
                cur.execute("select * from book_log bl join book b on bl.book_id=b.id where user_id = %s",(userid))
                books = cur.fetchall()
                cur.close()
                print(books)
                message = "Fetch All Bookslog for login user"
                if session['isAdmin'] == 'true':
                    return make_response(render_template('collection.html',booksdetails = books,userid=userid,isAdmin="true"))
                else:
                    return make_response(render_template('collection.html',booksdetails = books,userid=userid))
            else:
                message = 'User not login'
                return make_response(render_template('login.html'))
        except Exception as e:
            print(e)

# this class is used for add books
class addbook(Resource):
    def get (self):
        try:
            print('e')
            if 'loggedin' in session:
                if session['isAdmin'] == 'true':
                    if request.args.get('bookId'):
                        bookId=request.args.get('bookId')
                        conn = mysql.connect()
                        cur = conn.cursor(pymysql.cursors.DictCursor)
                        cur.execute("select * from book where id = %s",(int(bookId)))
                        book = cur.fetchone()
                        print(book)
                        cur.close()
                        return make_response(render_template('add-book.html',bookdata=book))
            return make_response(render_template('add-book.html'))
        except Exception as e:
                print(e)
    def post (self):
        try:
            print('pst')
            if 'loggedin' in session:
                if session['isAdmin'] == 'true':
                        userid=session['id']
                        bookId=request.form['bookId']
                        bookname=request.form['book_name']
                        category=request.form['category']
                        author=request.form['author']
                        isActive=request.form['isActive']
                        conn = mysql.connect()
                        cur = conn.cursor(pymysql.cursors.DictCursor)
                        if bookId =='':
                            cur.execute("insert into book (book_name,category,author,isActive) values (%s ,%s,%s,%s)",\
                                    (bookname,category,author,1))
                        else:
                            cur.execute("update book set book_name=%s, category=%s,author=%s\
                                    where id = %s",(bookname,category,author,int(bookId)))
                        conn.commit()
                        cur.execute("select * from book")
                        books = cur.fetchall()
                        cur.close()
                        print(books)
                        message = "Fetch All Books"
                        return redirect(url_for('book'))
                message = 'login as Admin'
                return make_response(render_template('login.html',message=message))
        except Exception as e:
                print(e)


# this class is used to fetch books
class book(Resource):
    def get(self):
        try:
            message='redirect to book'
            
            if 'loggedin' in session:
                userid = session['id']
                isAdmin  = session['isAdmin']
                conn = mysql.connect()
                cur = conn.cursor(pymysql.cursors.DictCursor)
                
                if session['isAdmin'] == 'true':
                    print(session['isAdmin'])
                    cur = conn.cursor(pymysql.cursors.DictCursor)
                    cur.execute("select * from book")
                    books = cur.fetchall()
                    cur.close()
                    print(books)
                    message = "Fetch All Books"
                    return make_response(render_template('index.html',booksdetails = books,userid=userid,isAdmin="true"))
                else: 
                    cur = conn.cursor(pymysql.cursors.DictCursor)
                    cur.execute("select * from book where status = 1 and isActive=1")
                    books = cur.fetchall()
                    cur.close()
                    print(books)
                    message = "Fetch All Books"
                    return make_response(render_template('index.html',booksdetails = books,userid=userid))
            else:
                message = 'User not login'
                return make_response(render_template('login.html',message =message))
        except Exception as e:
            print(e)

    # Delete method is used to delete books
    def delete(self):
        try:

            if 'loggedin' in session:
                userid = session['id']
                print(request.form)
                print("request.form")
                bookid = request.form['bookid']
                print(request.form['bookid'])
                conn = mysql.connect()
                cur = conn.cursor(pymysql.cursors.DictCursor)
                cur.execute("update book set isActive=0 where id = %s",(int(bookid)))
                conn.commit()
                cur.close()
                return True
            else:
                message = 'User not login'
                return False
        except Exception as e:
            print(e)
