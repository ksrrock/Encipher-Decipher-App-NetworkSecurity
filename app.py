from flask import Flask,render_template,request,redirect
app=Flask(__name__)

key="#1562789909112"
def encode(message):
    pass


def decode(message):
    pass


@app.route('/',methods=["GET","POST"])
def encrypt():
    if request.method=="POST":
        message=request.form['plaintext']
        return render_template("index.html",message=message)
    else:
        return render_template("index.html")


@app.route('/decipher',methods=["POST"])
def decrypt():
    decipher=request.form['decipher']
    print("d",decipher)
    return render_template("index.html",decipher=decipher)

    
if __name__=="__main__":
    app.run(debug=True)
