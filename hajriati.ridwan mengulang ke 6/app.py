from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    
    return render_template("index1.html")

@app.route("/halaman2")
def halaman2():
  
    return render_template("index2.html")

@app.route("/halaman3")
def halaman3():
  
    return render_template("index3.html")

@app.route("/halaman4")
def halaman4():
  
    return render_template("index4.html")

if __name__ == "__main__":
  
    app.run(debug=True)