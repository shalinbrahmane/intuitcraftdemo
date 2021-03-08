import json
import os
from flask import Flask, request as flask_request, make_response
from pymongo import MongoClient
from bson import json_util

app = Flask(__name__)

client = MongoClient("mongodb+srv://mongodevuser:bXvp0y1alsJlfSzg@cluster0.crt4v.mongodb.net/craftdemo?retryWrites=true&w=majority")
db = client.craftdemo
   
@app.route('/')
def hello():
    return 'Hello World'

if __name__ == '__main__':
    app.run()