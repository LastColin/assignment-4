from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import json
from project.model.customer import *


URI = "neo4j+s://6c32df2e.databases.neo4j.io"
AUTH = ("neo4j", "7NZ7hrFzNKsf9xgjVSYRV3HZnI3Gz9E8ZuPNR2GJrAc")

# Get connection to database
def _get_connection() -> Driver:
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()
    return driver

def node_to_json(node):
    node_properties = dict(node.items())
    return node_properties


# ------------------------------------------------------------------------------------------------------------------------------------
#Car
def findAllCars():
    with _get_connection().session() as session:
        cars = session.run("MATCH (a:Car) RETURN a;")
        nodes_json = [node_to_json(record["a"]) for record in cars]
        print(nodes_json)
        return nodes_json, f'All cars'

def findCarByReg(reg):
    with _get_connection().session() as session:
        cars = session.run("MATCH (a:Car) where a.reg=$reg RETURN a;", reg=reg)
        nodes_json = [node_to_json(record["a"]) for record in cars]

        return nodes_json, f'Car with reg number {reg} found'

def save_car(make, model, reg, year, capacity):
    with _get_connection().session() as session:
        cars = session.run("MERGE (a:Car{make: $make, model: $model, reg: $reg, year: $year, capacity:$capacity}) RETURN a;", \
            make = make, model = model, reg = reg, year = year, capacity = capacity)
        
        nodes_json = [node_to_json(record["a"]) for record in cars]
        return nodes_json, f'Car with reg number {reg} saved to database'

def update_car(make, model, reg, year, capacity):
    with _get_connection().session() as session:
        cars = session.run("MATCH (a:Car{reg:$reg}) set a.make=$make, a.model=$model, \
        a.year = $year, a.capacity = $capacity RETURN a;", reg=reg, make=make, model=model, year=year, capacity=capacity)
        
        nodes_json = [node_to_json(record["a"]) for record in cars]
        return nodes_json, f'Car with reg number {reg} updated'

def delete_car(reg):
    _get_connection().execute_query("MATCH (a:Car{reg: $reg}) delete a;", reg = reg)
    return f'Car with reg number {reg} deleted'



# ------------------------------------------------------------------------------------------------------------------------------------
# booking/ renting/ returning car
def book_car(customerId, carId):
    with _get_connection().session() as session:
        car = session.run("MATCH (a:Car) where a.reg=$reg RETURN a;", reg=carId)
        car = [node_to_json(record["a"]) for record in car]
        customer = session.run("MATCH (a:Customer) where a.id=$id RETURN a;", id=customerId)
        customer = [node_to_json(record["a"]) for record in customer]

        if car[0]['capacity'] == 'Booked':
            return 'car is already Booked'

        elif customer[0]['ordered_car'] != 'None':
            return 'customer has already booked a car'

        else:
            update_car(car[0]['make'], car[0]['model'], car[0]['reg'], car[0]['year'], capacity='Booked')
            update_customer(customer[0]['name'], customer[0]['age'], customer[0]['address'], carId, customer[0]['id']) 

        return 'car booked successfully'


def cancel_booking(customerId, carId):
    with _get_connection().session() as session:
        car = session.run("MATCH (a:Car) where a.reg=$reg RETURN a;", reg=carId)
        car = [node_to_json(record["a"]) for record in car]

        customer = session.run("MATCH (a:Customer) where a.id=$id RETURN a;", id=customerId)
        customer = [node_to_json(record["a"]) for record in customer]

        if car[0]['capacity'] == 'Booked' and customer[0]['ordered_car'] == carId:
            update_car(car[0]['make'], car[0]['model'], car[0]['reg'], car[0]['year'], capacity='Available')
            update_customer(customer[0]['name'], customer[0]['age'], customer[0]['address'], 'None', customer[0]['id']) 

        else:
            return 'car is not booked by this customer'

        return 'order cancelled successfully'


def rent_booked_car(customerId, carId):
    with _get_connection().session() as session:
        car = session.run("MATCH (a:Car) where a.reg=$reg RETURN a;", reg=carId)
        car = [node_to_json(record["a"]) for record in car]

        customer = session.run("MATCH (a:Customer) where a.id=$id RETURN a;", id=customerId)
        customer = [node_to_json(record["a"]) for record in customer]

        if car[0]['capacity'] == 'Booked' and customer[0]['ordered_car'] == carId:
            update_car(car[0]['make'], car[0]['model'], car[0]['reg'], car[0]['year'], capacity='Rented')
            update_customer(customer[0]['name'], customer[0]['age'], customer[0]['address'], carId, customer[0]['id']) 
            return 'car rented successfully'

        else:
            return 'Car is not booked by this customer'


def return_rented_car(customerId, carId):
    with _get_connection().session() as session:
        car = session.run("MATCH (a:Car) where a.reg=$reg RETURN a;", reg=carId)
        car = [node_to_json(record["a"]) for record in car]

        customer = session.run("MATCH (a:Customer) where a.id=$id RETURN a;", id=customerId)
        customer = [node_to_json(record["a"]) for record in customer]

        if car[0]['capacity'] == 'Rented' and customer[0]['ordered_car'] == carId:
            update_car(car[0]['make'], car[0]['model'], car[0]['reg'], car[0]['year'], capacity='Available')
            update_customer(customer[0]['name'], customer[0]['age'], customer[0]['address'], 'None', customer[0]['id']) 
            return 'car returned successfully'

        else:
            return 'Car is not rented by this customer'



