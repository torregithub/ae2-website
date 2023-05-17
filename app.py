from flask import Flask #imported flask

app = Flask(__name__) #created flsak app

@app.route("/")#register route to application 
def helloworld():
  return "Hello, World"

if __name__== '__main__': #if its running on app.py
  app.run(host='0.0.0.0', debug=True) #start app
