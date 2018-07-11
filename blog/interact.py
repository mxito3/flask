from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def root():
    return render_template('intract.html')

@app.route('/test')
def test():
    return "test"


if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True,port=8080)