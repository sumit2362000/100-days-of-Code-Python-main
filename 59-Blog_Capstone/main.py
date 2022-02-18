
from flask import Flask, render_template
import requests

posts = requests.get("https://api.npoint.io/88c2c1f644ef334058be").json()
post_ex = posts["id"==1]

app = Flask(__name__)
print(app)

@app.route('/')
def get_all_posts():
    return render_template('index.html', all_posts=posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post")
def post():
    return render_template("post.html", post=post_ex)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    print(index)
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
