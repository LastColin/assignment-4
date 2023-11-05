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


def findAllEmployees():
    with _get_connection().session() as session:
        employees = session.run("MATCH (a:employee) RETURN a;")
        nodes_json = [node_to_json(record["a"]) for record in employees]

        return nodes_json, f'All emplyees'

def findEmployeeById(id):
    with _get_connection().session() as session:
        employee = session.run("MATCH (a:employee) where a.id=$id RETURN a;", id=id)

        nodes_json = [node_to_json(record["a"]) for record in employee]
        return nodes_json, f'Employee with id {id} found'

def save_employee(name, address, branch, id):
    with _get_connection().session() as session:
        employees = session.run(
            "MERGE (a:employee {id: $id}) SET a.name = $name, a.address = $address, a.branch = $branch, a.id = $id RETURN a;",
            name=name,address=address, branch=branch, id=id
        )
        nodes_json = [node_to_json(record["a"]) for record in employees]
        return nodes_json, f'Employee with id {id} saved to database'

def update_employee(name, address, branch, id):
    with _get_connection().session() as session:
        employees = session.run(
        "MERGE (a:employee {id: $id}) SET a.name = $name, a.address = $address, a.branch = $branch, a.id = $id RETURN a;",
        name=name, address=address, branch=branch ,id=id
        )
        print(employees)
        nodes_json = [node_to_json(record["a"]) for record in employees]
        return nodes_json, f'Employee with id {id} updated'
    
def delete_employee(id):
    _get_connection().execute_query("MATCH (a:employee{id: $id}) delete a;", id=id)
    return f'Employee with id {id} deleted'