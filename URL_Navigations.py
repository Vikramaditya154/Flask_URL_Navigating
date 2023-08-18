from flask import Flask,render_template

app=Flask(__name__)


@app.route('/python')
def Python():
    return render_template('first.html')

@app.route('/django')
def Django():
    return render_template('second.html')

if __name__=='__main__':
    app.run(debug=True)