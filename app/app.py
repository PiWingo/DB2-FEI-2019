import pymongo
from flask import Flask, request, render_template

app = Flask(__name__)

# client = pymongo.MongoClient("mongodb+srv://<username>:<password>@db2-master-wddrg.gcp.mongodb.net/test?retryWrites=true&w=majority")

# db = client.data

# coll = db.teste

# print(coll.find_one())

@app.route('/')
def hello():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()