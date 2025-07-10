from flask import Flask
app = Flask(__name__)
@app.route('/')
def firstApp():
    return "Hello world"
app.run(debug = True)


