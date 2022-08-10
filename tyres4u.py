from flask import Flask, render_template 
#   Note we also use the gunicorn module as our professional server

#   Init app
app = Flask(__name__) 


#   Single page site - can be expanded with further routes
@app.route("/", methods=["GET"])
def home () :
    return render_template("index.html")


if __name__ == "__main__" :
    app.run(debug=True)