from flask import Flask, jsonify
import redis

app = Flask(__name__)
redis_obj = redis.Redis(host='redis-service', port=6379, db=0, charset="utf-8", decode_responses=True)


@app.route('/getproductdetails')
def get_product_details():
    product_details_json_object = {}
    redis_obj.set('P_Books', 4)
    redis_obj.set('P_Laptops', 10)
    redis_obj.set('P_Calculators', 20)
    redis_obj.set('P_Playstation', 7)
    redis_obj.set('P_Mobile Phones', 6)
    redis_obj.set('P_Televisions', 66)
    
    for key in redis_obj.keys():
        product_details_json_object[key] = redis_obj.get(key)
    return jsonify(product_details_json_object)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8989)
