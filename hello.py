from flask import Flask , render_template
app = Flask(__name__)


@app.route('/')
def checkerboard():
    return render_template("basic.html")








if __name__=="__main__":       
    app.run(debug=True)  