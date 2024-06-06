from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_word():

    return render_template("navigation.html")

@app.route("/home/")
def home():

    return render_template("home.html")



@app.route("/article/")
def article():

    return render_template("article.html")

@app.route("/сontacts/")
def сontacts():

    return render_template("contact.html")





if __name__ == "__main__":
    app.run()




