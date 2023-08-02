from controller import loginAPI,signUpAPI,logout,book,bookReturn,bookBorrow,homePage,mycollection,addbook,userlist

#Define Routes for ALL APIs
def routes(api):
    api.add_resource(loginAPI, '/login',endpoint= 'login') # redirect to login function
    api.add_resource(signUpAPI, '/signup',endpoint= 'signup',methods = ['GET','POST']) # redirect to signup page
    api.add_resource(logout, '/logout') # redirect to logout function
    api.add_resource(book, '/book',methods = ['GET','DELETE']) # redirect to book function
    api.add_resource(bookReturn, '/bookreturn') # redirect to bookreturn function
    api.add_resource(bookBorrow, '/bookborrow') # redirect to bookborrow function
    api.add_resource(mycollection, '/mycollection',methods = ['GET','POST','DELETE']) # redirect to mycollection function
    api.add_resource(homePage, '/') # redirect to HomePage
    api.add_resource(addbook, '/addbook',endpoint='addbook',methods = ['GET','POST']) # redirect to Add book function
    api.add_resource(userlist,'/users',endpoint = 'users') # redirect to fetch user function