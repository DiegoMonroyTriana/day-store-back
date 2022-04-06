from flask import Flask, jsonify
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route('/', methods = ['GET'])
def get_metas():

   return jsonify([
     {
       "ciudad": "México",
        "meta": 15,
        "servicios": 9
     }, 
     {
        "ciudad": "Monterrey",
        "meta": 10,
        "servicios": 1
     },
     {
       "ciudad": "Guadalajara",
       "meta": 10,
       "servicios": 4
     },
     {
        "ciudad": "Puebla",
        "meta": 8,
        "servicios": 8
     },
     {
       "ciudad": "Tijuana",
       "meta": 8 ,
       "servicios": 5 
     },
     {
       "ciudad": "Toluca",
        "meta": 9,
        "servicios": 10
     },
     {
       "ciudad": "Ciudad Juárez",
       "meta": 10,
       "servicios": 7
     }
   ])

if __name__ == '__main__':
    app.run()
  