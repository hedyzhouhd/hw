from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
app = Flask(__name__)
api = Api(app)
app.config['testcase'] = []
CORS(app)

class TestCase(Resource):
    def get(self):
        print(request.args)
        if "id" in request.args:
            for item in app.config['testcase']:
                if request.args['id'] == str(item['id']):
                    return item
        else:
            return app.config['testcase']

    def post(self):
        """
        上传测试用例：id name description steps

        :return:
        """
        app.config['testcase'].append(request.json)
        print(app.config['testcase'])
        return "用例添加成功"


    


class Login(Resource):
    def post(self):
        return '{status:"OK",msg:"登录成功"}'


api.add_resource(TestCase, '/testcase')
api.add_resource(Login, '/login')

if __name__ == "__main__":
    app.run(debug=1)
