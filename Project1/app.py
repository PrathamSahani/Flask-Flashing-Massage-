from flask import * 

# Intiallize Flask function
app = Flask(__name__)
app.secret_key = "GeeksForGeeks"


#home function for index.html
@app.route("/index")
def home():
    return render_template("index.html")


#row function for Profile.html
@app.route("/Profile")
def row():
    return render_template("Profile.html")


# write if and else condition if we peovide write password then he will redirect
# us in profile page otherwise he will redierect us on same page with 
# flashing massage Invalid Password 
@app.route("/login", methods=['GET','POST'])
def login():
    error= None
    if request.method =="POST":
        if request.form['pass']!="GFG":
            error = "Invalid Password"
        else:
            flash("You are succesfully login into the Flask Application")
            return redirect(url_for('row'))

    return render_template("login.html", error=error)


# execute command with debug function
if __name__ == '__main__':
    app.run(debug=True)

