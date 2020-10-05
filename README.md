# Flask-app-deployment-docker
CRUD operation on MongoDB atlas are performed using this application

## Docker Deployment

1. Build using Docker command:
	docker build -t <docker-image-name>
2. Run using Docker command:
	docker run it -p 5000:5000 <docker-image-name>

## How to access api

1. Read all the data from the data in MongoDB atlas.
	curl -i -H "Content-Type: application/json" -X GET http://127.0.0.1:5000/show_all_document		

2. Read specific data Ex: find the data whose brand_name = '?'.
	
	For Windows:-
	curl -i -H "Content-Type: application/json" -X GET -d "{"""brand_name""":"""jellycat"""}" http://127.0.0.1:5000/find_document		

	For Linux:-
	curl -i -H "Content-Type: application/json" -X GET -d "{"brand_name":"jellycat"}" http://127.0.0.1:5000/find_document	

3. Insert data. Ex: If you want to add new product,so you must have to provide its name and brand_name ,other fields are not necessary.

	For Windows:-
	curl -i -H "Content-Type: application/json" -X POST -d "{"""name""":"""jenson-t-series""","""brand_name""":"""jenson"""}" http://127.0.0.1:5000/insert_documents

	For Linux:
	curl -i -H "Content-Type: application/json" -X POST -d "{"name":"jenson-t-series","brand_name":"jenson"}" http://127.0.0.1:5000/insert_documents

4. Update specific data.Since there is no primary key in the given data,I used brand_name to find and update the data.

	For Windows:-
	curl -i -H "Content-Type: application/json" -X PUT -d "{"""name""":"""jetson-t-series""","""brand_name""":"""jetson"""}" http://127.0.0.1:5000/update_documents/jenson


	For Linux:-
	curl -i -H "Content-Type: application/json" -X PUT -d "{"name":"jenson-t-series","brand_name":"jenson"}" http://127.0.0.1:5000/update_documents/jenson

		Note:- I am finding the product using brand_name "jenson" and update its name and brand_name.

5. Delete the data Ex: deleting the data using its brand_name.

	For Windows:-
	curl -i -H "Content-Type: application/json" -X DELETE -d "{"""brand_name""":"""jetson"""}" http://127.0.0.1:5000/delete_documents

	For Linux:-
	curl -i -H "Content-Type: application/json" -X DELETE -d "{"brand_name":"jetson"}" http://127.0.0.1:5000/delete_documents

