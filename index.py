from flask import *
#import flask
#import flask as fk
app=Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")
    #return("Home page")

@app.route("/hai")
@app.route("/about")
@app.route("/aboutus")
def about():
    return render_template("about.html")
    #return("About page")
@app.route("/contact")
@app.route("/contactus")

def contact():
    return render_template("contact.html")
    #return("contact page")

if __name__=='__main__':
    app.run(debug=True)
    
