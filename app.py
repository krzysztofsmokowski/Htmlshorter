from flask import Flask
from flask_restful import Resource, Api, reqparse
from shorter import html_paragraphs

app = Flask(__name__)
api = Api(app)

class Paragrapher(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('url', type=str)
        args = parser.parse_args()
        data = html_paragraphs(url=args['url'])
        return data


api.add_resource(Paragrapher, '/paragrapher')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
