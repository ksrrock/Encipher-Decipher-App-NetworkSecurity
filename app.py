from flask import Flask,render_template,request,redirect
app=Flask(__name__)


def encode(message):
    s=[]
    print(message)
    for i in message:
        key=25-(ord(i)-ord('a'))+ord('a')
        print(key)
        s.append(chr(key))
    print(s)
    return ''.join(s)


def decode(message):
    s=[]
    for i in message:
        key=25-(ord(i)-ord('a'))+ord('a')
        s.append(chr(key))
    
    return ''.join(s)


@app.route('/',methods=["GET","POST"])
def encrypt():
    if request.method=="POST":
        message=request.form['plaintext']
        print(message)
        return render_template("index.html",message=encode(message))
    else:
        return render_template("index.html")


@app.route('/decipher',methods=["POST"])
def decrypt():
    decipher=request.form['decipher']
    print("d",decipher)
    return render_template("index.html",decipher=decode(decipher))

    
if __name__=="__main__":
    app.run(debug=True)
