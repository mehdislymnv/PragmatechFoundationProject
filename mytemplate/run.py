from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def main_index():
    return render_template("app/template-Fabricator/index.html")

from controllers.app import main 
if __name__=='__main__':
    app.run(debug=True)