from flask import Flask, render_template

app=Flask(__name__)

@app.route('/homework')
def homework():
    return render_template('hw.html')

if __name__=='__main__':
    app.run(debug=True) 