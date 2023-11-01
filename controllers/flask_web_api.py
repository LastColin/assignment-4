from flask import Flask

app = Flask(__name__)

@app.route('/get_cars', methods=['GET', 'POST'])
def query_records():
    pass