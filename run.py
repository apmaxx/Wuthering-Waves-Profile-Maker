from flask import Flask, render_template

app = Flask(__name__)

@app.route('/characters')
def wumir_characters():
    return  render_template ("characters.html")
    

@app.route('/characters/aalto')

def aalto_build():
    return render_template("aalto.html")

@app.route('/characters/calcharo')

def calcharo_build():
    return render_template("calcharo.html")

if __name__ == '__main__':
    app.run(debug=True)