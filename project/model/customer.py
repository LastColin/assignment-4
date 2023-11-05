from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import json

URI = "neo4j+s://6c32df2e.databases.neo4j.io"
AUTH = ("neo4j", "7NZ7hrFzNKsf9xgjVSYRV3HZnI3Gz9E8ZuPNR2GJrAc")


def _get_connection() -> Driver:
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()
    return driver

def node_to_json(node):
    node_properties = dict(node.items())
    return node_properties


def findAllCustomers():
    with _get_connection().session() as session:
        customers = session.run("MATCH (a:Customer) RETURN a;")
        nodes_json = [node_to_json(record["a"]) for record in customers]
        
        return nodes_json, f'All customers'

def findCustomerById(id):
    with _get_connection().session() as session:
        customer = session.run("MATCH (a:Customer) where a.id=$id RETURN a;", id=id)
        nodes_json = [node_to_json(record["a"]) for record in customer]
        return nodes_json, f'Customer with id {id} found'

def save_customer(name, age, address, ordered_car, id):
    with _get_connection().session() as session:
        customers = session.run(
        "MERGE (a:Customer {id: $id}) SET a.name = $name, a.age = $age, a.address = $address, a.ordered_car = $ordered_car, a.id = $id RETURN a;",
        name=name, age=age, address=address, ordered_car=ordered_car, id=id)
        nodes_json = [node_to_json(record["a"]) for record in customers]
        return nodes_json, f'Customer with id {id} saved to database'


def update_customer(name, age, address, ordered_car, id):
    with _get_connection().session() as session:
        customers = session.run(
        "MERGE (a:Customer {id: $id}) SET a.name = $name, a.age = $age, a.address = $address, a.ordered_car = $ordered_car, a.id = $id RETURN a;",
        name=name, age=age, address=address, ordered_car=ordered_car, id=id
        )
        nodes_json = [node_to_json(record["a"]) for record in customers]
        return nodes_json, f'Customer with id {id} updated'
    
def delete_customer(id):
    _get_connection().execute_query("MATCH (a:Customer{id: $id}) delete a;", id=id)
    return f'Customer with id {id} deleted'

