# Flask-based REST API server

This is a simple implementation of the REST API server using Flask with Python.

## Flast setup

Create a virtual environment for Flask:
```
virtualenv flask
```

Install Flask:
```
flask/bin/pip install flask
```

## Start the server (using the Flask's dev web server)

Make sure that port 5000 is not occupied.

```
chmod u+x uran.py
```

Start the server:

```
./uran.py
```

## Test REST API

### Get the list of existing orders

```
curl -i http://localhost:5000/uran/api/v1.0/orders
```

Result:

```
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 339
Server: Werkzeug/0.14.1 Python/3.6.7
Date: Tue, 26 Feb 2019 12:41:17 GMT

{
  "orders": [
    {
      "id": 1, 
      "instrument": "6758.T", 
      "price": 3800, 
      "quantity": 10000
    }, 
    {
      "id": 2, 
      "instrument": "6753.T", 
      "price": 2700, 
      "quantity": 5000
    }, 
    {
      "id": 3, 
      "instrument": "6751.T", 
      "price": 3200, 
      "quantity": 8000
    }
  ]
}
```

### Get an individual order

Make a parameterized GET request:

```
curl -i http://localhost:5000/uran/api/v1.0/orders/2
```

Response:

```
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 105
Server: Werkzeug/0.14.1 Python/3.6.7
Date: Tue, 26 Feb 2019 12:44:33 GMT

{
  "order": {
    "id": 2,
    "instrument": "6753.T",
    "price": 2700,
    "quantity": 5000
  }
}
```

### Add a new order

Submit a POST request:

```
curl -i -H "Content-Type: application/json" -X POST -d '{"instrument":"7001.T", "quantity":"1000", "price":"2800"}' http://localhost:5000/uran/api/v1.0/orders
```

Result:
```
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 109
Server: Werkzeug/0.14.1 Python/3.6.7
Date: Tue, 26 Feb 2019 12:47:10 GMT

{
  "order": {
    "id": 5,
    "instrument": "7001.T",
    "price": "2800",
    "quantity": "1000"
  }
}
```

### Delete an order by ID

Submit a DELETE request
```
curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/uran/api/v1.0/orders/3
```

Result:
```
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 21
Server: Werkzeug/0.14.1 Python/3.6.7
Date: Tue, 26 Feb 2019 12:52:36 GMT

{
  "result": true
}
```

## Notes

In PROD use Nginx as the real Web Server.
