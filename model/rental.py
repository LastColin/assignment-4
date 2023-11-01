from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import re

URI = "neo4j+s://66299abf.databases.neo4j.io"
AUTH = ("neo4j", "yY1nDcViJGzBRNZaCbXQwZXa10235zL8uAE_BGMs1t4")


def _get_connection() -> Driver:
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()

    return driver

def findCar(car):
    data = _get_connection().execute_query('MATCH (a:car) Return a;')
    return data

def updateCar(car):
    data = _get_connection().execute_query("MATCH (a:car) where a.name = $name RETURN a;", name=car.name)
    return data

def addCar(name):
    data = _get_connection().execute_query("CREATE (a:car {name: $name}) RETURN a;", name=name)
    return data


class Car:
    def __init__(self, name, model, make, regnr):
        self.name = name
        self.model = model
        self.make = make
        self.regnr = regnr

    def get_Name(self):
        return self.name
    
    def set_Name(self, value):
        self.name = value
    
    def get_Model(self):
        return self.model
    
    def set_Model(self, value):
        self.model = value

    def get_Make(self):
        return self.make
    
    def set_Make(self, value):
        self.make = value

    def get_Regnr(self):
        return self.regnr
    
    def set_Regnr(self, value):
        self.regnr = value
