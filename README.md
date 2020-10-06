# Flask-app-deployment-docker
CRUD operation on MongoDB atlas are performed using this application

## Docker Deployment

Go to the project directory and apply following commands in your terminal.

1. Build using Docker command:

	docker build -t <docker-image-name> .
	
		Ex:- docker build flask-app .
2. Run using Docker command:

	docker run it -p 5000:5000 <docker-image-name>
	
		Ex: docker run it -p 5000:5000 flask-app

## How to access api

1. Read all the data from the data in MongoDB atlas.

		curl -i -H "Content-Type: application/json" -X GET http://127.0.0.1:5000/show_all_document
		
  	Input Screenshot:

	[![Input-using-curl.png](https://i.postimg.cc/65QrF5Bs/Input-using-curl.png)](https://postimg.cc/XXTBCWZx)
	
	Output Screenshot:
	
	[![Output.png](https://i.postimg.cc/B6qLDM6W/Output.png)](https://postimg.cc/qt5vHcyQ)
	

2. Read specific data Ex: find the data whose brand_name = '?'.
	
	For Windows:-
	
		curl -i -H "Content-Type: application/json" -X GET -d "{"""brand_name""":"""jellycat"""}" http://127.0.0.1:5000/find_document		

	For Linux:-
	
		curl -i -H "Content-Type: application/json" -X GET -d "{"brand_name":"jellycat"}" http://127.0.0.1:5000/find_document	
		
	Input and Output Screenshot:
	
	[![Input-and-output-using-curl.png](https://i.postimg.cc/C5RKHtp2/Input-and-output-using-curl.png)](https://postimg.cc/y3zB7Ldh)
	

3. Insert data. Ex: If you want to add new product,so you must have to provide its name and brand_name ,other fields are not necessary.

	For Windows:-
	
		curl -i -H "Content-Type: application/json" -X POST -d "{"""name""":"""jenson-t-series""","""brand_name""":"""jenson"""}" http://127.0.0.1:5000/insert_documents

	For Linux:
	
		curl -i -H "Content-Type: application/json" -X POST -d "{"name":"jenson-t-series","brand_name":"jenson"}" http://127.0.0.1:5000/insert_documents
		
	Input Screenshot:
	
	[![Input-using-curl.png](https://i.postimg.cc/W4sbftPg/Input-using-curl.png)](https://postimg.cc/9DNhDm0Q)
	
	Output Screenshot:
	
	[![Output-from-Mongo-DB-atlas.png](https://i.postimg.cc/pVm8BcCx/Output-from-Mongo-DB-atlas.png)](https://postimg.cc/5jM643Dk)		
	

4. Update specific data.Since there is no primary key in the given data,I used brand_name to find and update the data.

	For Windows:-
	
		curl -i -H "Content-Type: application/json" -X PUT -d "{"""name""":"""jetson-t-series""","""brand_name""":"""jetson"""}" http://127.0.0.1:5000/update_documents/jenson


	For Linux:-
	
		curl -i -H "Content-Type: application/json" -X PUT -d "{"name":"jenson-t-series","brand_name":"jenson"}" http://127.0.0.1:5000/update_documents/jenson

	Note:- I am finding the product using brand_name "jenson" and update its name and brand_name.
	
	Input Screenshot:
	
	[![Input-using-Curl.png](https://i.postimg.cc/52VCb4VN/Input-using-Curl.png)](https://postimg.cc/XpsJg0qT)
	
	Output Screenshot:
	
	[![Output-in-Mongo-DB.png](https://i.postimg.cc/fbHtcY0J/Output-in-Mongo-DB.png)](https://postimg.cc/yJZ8BgjH)
	

5. Delete the data Ex: deleting the data using its brand_name.

	For Windows:-
	
		curl -i -H "Content-Type: application/json" -X DELETE -d "{"""brand_name""":"""jetson"""}" http://127.0.0.1:5000/delete_documents

	For Linux:-
	
		curl -i -H "Content-Type: application/json" -X DELETE -d "{"brand_name":"jetson"}" http://127.0.0.1:5000/delete_documents
		
	Input and Output Screenshot:
	
	[![Input-and-output-using-curl.png](https://i.postimg.cc/Vs0rtrsk/Input-and-output-using-curl.png)](https://postimg.cc/Z0Z5tqyG)

