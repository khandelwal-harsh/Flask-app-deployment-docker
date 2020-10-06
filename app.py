from pymongo import MongoClient
import json
from flask import Flask,jsonify,request
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):

	"""
	A class for converting the data into json format.

	Methods
	-------
	default
		Does the json encoding.

	"""
	def default(self, o):

		"""
		Returns
		------
		json
		encoded json data
		"""
		if isinstance(o, ObjectId):
			return str(o)
		return json.JSONEncoder.default(self, o)


# Creating Client object for MongoDB by passing the authentication string to the MongoClient() method. 
client = MongoClient('mongodb+srv://harsh-t1:greendeck-t1@cluster-1.owmx1.mongodb.net/<dbname>?retryWrites=true&w=majority')

# Creating records object for performing the CRUD operations.
db = client.get_database('products')
records = db.products_list

app = Flask(__name__)

@app.route('/find_document', methods=['GET'])
def find_document():
	"""
	route page: http://127.0.0.1:5000/find_document

	This function finds the specific data based on the your query.

	Attributes
	----------
	resp
		request the query from the user.
	data
		data that the user wants to find based on the query.

	Returns
	-------
	json
		returns the data in json format based on your query.

	"""
	resp = request.json

	data = records.find_one(resp)
	return json.dumps(d,cls = JSONEncoder)


@app.route('/show_all_document', methods=['GET'])
def show_all_document():
	"""
	route page: http://127.0.0.1:5000/show_all_document

	This function show all the data present in the database.

	Attributes
	----------
	data
		all the data present in the database

	Returns
	-------
	json
		returns all the data present in database in json format.	
	
	"""

	data = list(records.find())
	return json.dumps(data,cls = JSONEncoder)


@app.route('/insert_documents', methods=['GET','POST'])
def insert_documents():

	"""
	route page: http://127.0.0.1:5000/insert_documents

	This function insert a new data in  the database.

	Attributes
	----------
	data
		new data that user wants to insert in the database

	Returns
	-------
	json
		returns newly created data in database in json format.	
	
	"""

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

	"""
	route page: http://127.0.0.1:5000/update_documents/<brand_name>

	This function updates the data by searching the data using parameter passed by the user in routing page and then performs update in that data.

	Parameters
	----------
	product_brand_name
		brand_name of the product.

	Attributes
	----------
	resp
		request the data from the user,that user wants to update.
	new_dict
		new data that needs to be updated. 

	Returns
	-------
	string
		returns Update successful string.  	
	
	"""

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

	"""
	route page: http://127.0.0.1:5000/delete_documents

	This function deletes the data from the database based on the query provided by the user.

	Attributes
	----------
	resp
		request the query from the user

	Returns
	-------
	string
		returns deleteion done string.	
	
	"""

	resp = request.json
	records.delete_one(resp)

	return "Deletion Done"
	
if __name__ == '__main__':
    app.run(host = "0.0.0.0",port = 5000)



