from flask import Flask, render_template
from flask_restful import Api
from myapis import customers_api

app = Flask(__name__, template_folder="myhtmls")
api = Api(app)


@app.route("/home", methods=["GET"])
def home():
    return render_template('home.html')


@app.route("/", methods=["GET"])
def root():
    return 'Welcome to API resource root.'

def start_app():
    app.run(host="localhost", port=5000, debug=True)

api.add_resource(customers_api.Customer, '/customers/<string:id>')
api.add_resource(customers_api.Customers, '/customers')

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
