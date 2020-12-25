from flask_restful import Resource, reqparse
import sys

customers = {}

class Customers(Resource):
    def get(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('size', type=int, location='args')
        args = parser.parse_args()
        size=args['size']
        return {k: customers[k] for k in list(customers)[:size]}

class Customer(Resource):
    def get(self, id):
        return {id: customers[id]}, 200

    def put(self, id):
        try:
            parser = reqparse.RequestParser(bundle_errors=True)
            parser.add_argument('name', required=True, nullable=False, type=str, location='form', help='name should be present')
            parser.add_argument('age', required=True, nullable=False, type=int, location='form', help='age as an int should be present')
            parser.add_argument('type', required=True, nullable=False, type=str, choices=('RETAIL', 'PRIVATE'),location='form', help='type should be present')
            parser.add_argument('phones', required=True, nullable=False, type=str, action='append', location='form', help='phones are mandatory and can be many')
            parser.add_argument('user-agent', type=str, location='headers')
            args = parser.parse_args()
            customers[id] = { 'name' : args['name'],
                              'age': args['age'],
                              'type': args['type'],
                              'phones': args['phones'],
                              'user-agent': args['user-agent'],
                              }
            return {id: customers[id]}, 201, {'x-resp-header-1' : 'custom-value'}
        except Exception as e:
            print('some error occured', sys.exc_info()[0])
            print('some Exception occured', e)
            raise Exception('some error occured')

    def delete(self, id):
        del customers[id]
        return {}, 204, {'x-resp-header-1' : 'custom-value'}

