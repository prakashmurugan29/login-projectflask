from flask import Flask, render_template, request
app=Flask(__name__)
#routing "/"- first page
@app.route("/")
def home():
    return render_template("login.html")
#routing "/login" - login page
#database : username/password
database={'Ram':'Ram@123', 'Raj':'Raj@123' ,'Ravi':'Ravi@123'} 
@app.route('/form_login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        name1=request.form['username']#Shanmugavel
        password1=request.form['password']#Shanmugavel@123
        if name1 not in database:
            return render_template('login.html',info="Invalid user")
        else:
            if database[name1]!=password1:
                return render_template('login.html',info="Invalid password")
            else:
                return render_template('home.html', name=name1)
    return render_template('login')        
#main program
if __name__=="__main__":
    app.run(debug=True)                                                 


