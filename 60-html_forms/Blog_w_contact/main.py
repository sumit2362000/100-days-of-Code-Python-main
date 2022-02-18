
from flask import Flask, render_template, request
import requests
import smtplib

posts = requests.get("https://api.npoint.io/88c2c1f644ef334058be").json()
post_ex = posts["id"==1]

# Uncomment out send_email line in line 32 of Main.py
OWN_EMAIL = "YOUR OWN EMAIL ADDRESS"
OWN_PASSWORD = "YOUR EMAIL ADDRESS PASSWORD"

app = Flask(__name__)
print(app)

@app.route('/')
def get_all_posts():
    return render_template('index.html', all_posts=posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(f'Name: {data["name"]}')
        print(f'Email: {data["email"]}')
        print(f'Phone: {data["phone_number"]}')
        print(f'Message: {data["message"]}')
        # send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

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

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)

if __name__ == "__main__":
    app.run(debug=True)
