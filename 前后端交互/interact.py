from flask import Flask,render_template,jsonify,make_response
app=Flask(__name__)
@app.route('/')
def root():
    return "root"

@app.route('/test')
def test():
    res=make_response(jsonify({'msg':'hello world'}))
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res


if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True,port=2000)