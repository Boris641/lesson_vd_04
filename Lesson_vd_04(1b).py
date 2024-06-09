from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/article/")
def article():
    return render_template("article.html")

@app.route("/contacts/")
def contacts():
    return render_template("contacts.html")





if __name__ == "__main__":
    app.run()




