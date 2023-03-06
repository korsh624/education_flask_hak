import requests
from flask import Flask, render_template
app = Flask(__name__)
name='Имя'
def readData():
    r=requests.get('https://reqres.in/api/users?per_page=12').json()
    print(r)
    return r['data']
@app.route("/")
def home():
    return render_template('index.html')
@app.route("/team")
def team():
    array=readData()
    return render_template('team.html',array=array)
if __name__=="__main__":
    app.run(debug=True)



