# assignment-4
assignment 4 in info212

run server.py to start server

endpoints:
  car endpoints:
    /get_cars
    /get_car_by_reg_number
    /save_car
    /update_car
    /delete_car

  customer endpoints:  
    /get_customers
    /get_customer_by_id
    /save_customer
    /update_customer
    /delete_customer

  employee endpoints:
    /get_employees
    /get_employee_by_id
    /save_employee
    /update_employee
    /delete_employee

  order endpoints:
    /order-car/<customerId>/<carId>
    /rent-car/<customerId>/<carId>
    /return-car/<customerId>/<carId>
