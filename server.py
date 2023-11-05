#Project Flask MVC

from project import app

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
    


# test data
car = {
    "make": "Toyota",
    "model": "Corolla",
    "reg": "AA1234",
    "year": "2010",
    "capacity": "Available",
}

customer = {
    "name": "John Kramer",
    "age": "30",
    "address": "New Jersey",
    "ordered_car": "None",
    "id": "1"
}

employee = {
    "name": "Freddy Krueger",
    "address": "Elm Street",
    "branch": "Ohio",
    "id": "1"
}

