import os
from flask import Flask, render_template, send_from_directory


# initialization
app = Flask(__name__)
app.config.update(
    Debug = True,
)

# controllers
@app.route('/home')
def home():
    return render_template('chris_base.html')
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    
@app.route("/")
def index():
    return render_template('intro.html')
    
@app.route("/hello")
def hello():
    return "Hello, World!"

#launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0',port=port)

