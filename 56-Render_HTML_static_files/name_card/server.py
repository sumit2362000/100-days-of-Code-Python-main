
from flask import Flask, render_template

'''
HTML ready made sites
https://html5up.net/
using this as base:
https://github.com/html5up/identity
'''

'''
Chrome Developer Tools
settings-more tools-developer tools
in Console:
document.body.contentEditable=true
'''

app = Flask(__name__)
print(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)