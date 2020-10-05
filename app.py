from pymongo import MongoClient
import json
from flask import Flask,jsonify,request
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)



client = MongoClient('mongodb+srv://harsh-t1:greendeck-t1@cluster-1.owmx1.mongodb.net/<dbname>?retryWrites=true&w=majority')
db = client.get_database('products')
records = db.products_list

app = Flask(__name__)

@app.route('/find_document', methods=['GET'])
def find_document():
	resp = request.json

	d = records.find_one(resp)
	return json.dumps(d,cls = JSONEncoder)

@app.route('/show_all_document', methods=['GET'])
def show_all_document():

	d = list(records.find())
	return json.dumps(d,cls = JSONEncoder)

@app.route('/insert_documents', methods=['GET','POST'])
def insert_documents():

	data = {
	'name':request.json['name'],
	'brand_name':request.json['brand_name'],
	'regular_price_value':request.json.get('regular_price_value',""),
	'offer_price_value':request.json.get('offer_price_value',""),
	'currency':request.json.get('currency',""),
	'classification_l1':request.json.get('classification_l1',""),
	'classification_l2':request.json.get('classification_l2',""),
	'classification_l3':request.json.get('classification_l3',""),
	'classification_l4':request.json.get('classification_l4',""),
	'image_url':request.json.get('image_url',"")
	}

	records.insert_one(data)
	return json.dumps(data,cls = JSONEncoder)

@app.route('/update_documents/<product_brand_name>', methods=['PUT'])
def update_document(product_brand_name):
	tasks = list(records.find())

	for task in tasks:
		if task['brand_name']==product_brand_name:
			name = task['name']
			brand_name = task['brand_name']
			regular_price_value = task['regular_price_value']
			offer_price_value = task['offer_price_value']
			currency = task['currency']
			classification_l1 = task['classification_l1']
			classification_l2 = task['classification_l2']
			classification_l3 = task['classification_l3']
			classification_l4 = task['classification_l4']
			image_url = task['image_url']



	resp = request.json

	for key,value in resp.items():
		if key == 'name':
			name = value
		if key == 'brand_name':
			brand_name = value
		if key =='regular_price_value':
			regular_price_value = value
		if key == 'offer_price_value':
			offer_price_value = value
		if key == 'currency':
			currency = value
		if key == 'classification_l1':
			classification_l1 = value
		if key == 'classification_l2':
			classification_l2 = value
		if key == 'classification_l3':
			classification_l3 = value
		if key == 'classification_l4':
			classification_l4 = value
		if key == 'image_url':
			image_url = value



	new_dict = {
	'name':name,
	'brand_name':brand_name,
	'regular_price_value':regular_price_value,
	'offer_price_value':offer_price_value,
	'currency':currency,
	'classification_l1':classification_l1,
	'classification_l2':classification_l2,
	'classification_l3':classification_l3,
	'classification_l4':classification_l4,
	'image_url':image_url
	}


	records.update_one({'brand_name':product_brand_name},{'$set':new_dict})
	return "Updated field Successfully"

	
@app.route('/delete_documents', methods=['DELETE'])
def delete_document():

	resp = request.json
	records.delete_one(resp)

	return "Deletion Done"
	
if __name__ == '__main__':
    app.run(host = "0.0.0.0",port = 5000)



