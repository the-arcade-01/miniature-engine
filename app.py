from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['POST','GET'])
def index():
    val = None
    if request.method == 'POST':
        val = request.form('1')
    else:
        pass
    return render_template('index.html',val = val)

if __name__ == '__main__':
    app.run(debug=True)
