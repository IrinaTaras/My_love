from flask import Flask, render_template


app = Flask(__name__)
@app.route("/")

def profil_my_love():
    return render_template("my_cat.html")

app.run()

