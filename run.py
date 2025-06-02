from flask import Flask, render_template

app = Flask(__name__)

@app.route('/characters')
def wuwa_login():


    return  render_template ("characters.html")

if __name__ == '__main__':
    app.run(debug=True)