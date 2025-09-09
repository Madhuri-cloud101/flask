# 08 september 2025
# Making a Server
from flask import Flask, request

app = Flask(__name__)

@app.route("/")     # syntax
def home():
    return "home route"

# Here test means -  api endpoint 
# When we make changes in server then first we have to stop code in terminal crtl + c

@app.route("/test", methods=["POST"])   # method - POST (add)
def about():
    data = request.json
    print(data)
    return "about route"

# PUT
@app.route("/update", methods=["PUT"])
def updateNote():
    return "Note Update Success"

#DELETE
@app.route("/remove", methods=["DELETE"])
def removeNote():
    return "Note remove Success"
# server on 
# app.run
if (__name__ == "__main__"):
    app.run(debug=True)      # (debug=True) shortcut to server on/off option 

# github account 
# postman account 
# render account 
# gitscm account 
# install --- pip install gunicorn 
# pip freeze > requirements.txt 
# git init
# git remote add origin 
# git add . 
# git commit -m "initial commit"