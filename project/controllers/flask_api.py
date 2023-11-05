from project import app
from flask import Flask, render_template, request, redirect, url_for
from project.model.car import *
from project.model.customer import *
from project.model.employee import *
import json

@app.route('/', methods=["GET", "POST"])


# ------------------------------------------------------------------------------------------------------------------------------------
#Car

@app.route('/get_cars', methods=["GET"])
def query_records():
    return findAllCars()

@app.route('/get_car_by_reg_number', methods=['GET'])
def find_car_by_reg_number():
   record = json.loads(request.data)
   print(record)
   print(record['reg'])
   return findCarByReg(record['reg'])

@app.route('/save_car', methods=["POST"])
def save_car_info():
    record = json.loads(request.data)
    print(record)
    return save_car(record['make'], record['model'], record['reg'], record['year'], record['capacity'])

@app.route('/update_car', methods=['PUT'])
def update_car_info():
    record = json.loads(request.data)
    print(record)
    return update_car(record['make'], record['model'], record['reg'], record['year'], record['capacity'])


@app.route('/delete_car', methods=['DELETE'])
def delete_car_info():
    record = json.loads(request.data)
    return delete_car(record['reg'])

# ------------------------------------------------------------------------------------------------------------------------------------
#Customer

@app.route('/get_customers', methods=["GET"])
def query_customers():
    return findAllCustomers()

@app.route('/get_customer_by_id', methods=['GET'])
def find_customer_by_id():
   record = json.loads(request.data)
   print(record)
   print(record['id'])
   return findCustomerById(record['id'])

@app.route('/save_customer', methods=["POST"])
def save_customer_info():
    record = json.loads(request.data)
    print(record)
    return save_customer(record['name'], record['age'], record['address'], record['ordered_car'], record['id'])

@app.route('/update_customer', methods=['PUT'])
def update_customer_info():
    record = json.loads(request.data)
    print(record)
    return update_customer(record['name'], record['age'], record['address'], record['ordered_car'], record['id'])

@app.route('/delete_customer', methods=['DELETE'])
def delete_customer_info():
    record = json.loads(request.data)
    print(record)
    delete_customer(record['id'])
    return findAllCustomers()


# ------------------------------------------------------------------------------------------------------------------------------------
#Employee

@app.route('/get_employees', methods=["GET"])
def query_employees():
    return findAllEmployees()

@app.route('/get_employee_by_id', methods=['GET'])
def find_employee_by_id():
   record = json.loads(request.data)
   print(record)
   print(record['id'])
   return findEmployeeById(record['id'])

@app.route('/save_employee', methods=["POST"])
def save_employee_info():
    record = json.loads(request.data)
    print(record)
    return save_employee(record['name'], record['address'], record['branch'], record['id'])

@app.route('/update_employee', methods=['PUT'])
def update_employee_info():
    record = json.loads(request.data)
    print(record)
    return update_employee(record['name'], record['address'], record['branch'], record['id'])

@app.route('/delete_employee', methods=['DELETE'])
def delete_employee_info():
    record = json.loads(request.data)
    print(record)
    delete_employee(record['id'])
    return findAllEmployees()



# ------------------------------------------------------------------------------------------------------------------------------------
# book car
@app.route('/order-car/<customerId>/<carId>', methods=['PUT'])
def order_car(customerId, carId):  
    return book_car(customerId, carId)

# cancel order
@app.route('/cancel-order/<customerId>/<carId>', methods=['PUT'])
def cancel_order(customerId, carId):  
    return cancel_booking(customerId, carId)

#rent car
@app.route('/rent-car/<customerId>/<carId>', methods=['PUT'])
def rent_car(customerId, carId):  
    return rent_booked_car(customerId, carId)

#return car
@app.route('/return-car/<customerId>/<carId>', methods=['PUT'])
def return_car(customerId, carId):  
    return return_rented_car(customerId, carId)