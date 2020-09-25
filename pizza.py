import urllib
import json
import os
import csv
from flask import Flask , request,  make_response, render_template
import MysqlConnect as connection
from mysql.connector import Error
import re

app = Flask(__name__)

@app.route("/webhook/index")
def index():
    return render_template("index.html")

@app.route('/webhook',methods = ['POST'])
def webhook():
    conn = connection.ConnectMySql()
    req = request.get_json(silent=True , force= True)
    res = makeWebhookResult(req)
    res = json.dumps(res , indent=4)
    print(res)
    r = make_response(res)
    print(r)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):

    if req.get("queryResult").get("action")=="input_details":
        pizzaord = connection.ConnectMySql()
        return()
        
            result = req.get("queryResult")
            parameters = result.get("parameters")
            orderid = parameters.get("orderid")
            name = parameters("name")
            pizza_name = parameters.get("pizza_name")
            pizza_size = parameters.get("pizza_size")
            pizza_type = parameters.get("pizza_type")
            name = parameter.get("name")
            mobileno = parameters.get("mobileno")
            Address = parameters.get("address")
            status = parameters.get("status")
            speech = "Orderid"+orderid +" "+ "Name" + name +" "+"Pizza name"+pizza_name+" "+"Pizza size" +pizza_size+ " " +"Pizza type"+ pizza_type+" " +"mobile no"+ mobileno+" "+
            " Address"+address+"Status: ordered"
            print(speech)
            return {
                "fulfillmentText": speech,
                "fulfillmentText": speech,
            }
            if pizzaord is Flase:
                return err.ReturnConnectionError()
            else:
                try:
                mycursor = pizzadb.cursor()
                query = "select *from pizzaorder"
                mycursor.execute(query)
                myresult = mycursor.fetchall()
                print(myresult)    

if __name__ == "__main__":
    port = int(os.getenv('PORT', 80))
    print("starting on port %d" %(port))
    app.run(debug=True, port=80)
