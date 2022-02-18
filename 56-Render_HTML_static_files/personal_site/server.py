from flask import Flask, render_template


'''
Rendering Templates
https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates
'''

'''
Notes:
Chrome likes to cache sites, be sure hard reload on chrome(shift + refresh)
'''

'''
HTML ready made sites
https://html5up.net/
'''

app = Flask(__name__)
print(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)