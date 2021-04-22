from flask import Flask, request
from flask_restful import Resource, Api, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/test?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
CORS(app)  # 允许跨域请求
db = SQLAlchemy(app)
api = Api(app)


class Case(db.Model):
    name = db.Column(db.String(80), primary_key=True)
    content = db.Column(db.String(200))
    description = db.Column(db.String(100))
    file_name = db.Column(db.String(20))


class CaseSaveAsFile(Resource):
    def post(self):
        if "file" in request.files:
            print(request.files)


# 测试请求curl -F "file=@tmp.json" 127.0.0.1:5000/testcase?name=test01
# curl -d "a=1&name=2" 127.0.0.1:5000/testcase?name=test01
class TestCase(Resource):
    def post(self):
        # 文件方式提交
        print(type(request.json))
        print(request.json)
        if 'name' in request.args and 'file' in request.files:
            f = request.files['file']
            file_name = f.filename
            print(file_name)
            content = f.read()
            print(len(content))
            name = request.args['name']
            case = Case(name=name, file_name=file_name, content=content, description='')
            db.session.add(case)
            db.session.commit()
            return {'status': 0}
        # 提交
        elif 'name' in request.json:
            name = request.json.get('name')
            file_name = request.json.get('file_name')
            content = request.json.get('content')
            description = request.json.get('description')
            case = Case(name=name, file_name=file_name, content=content, description=description)
            db.session.add(case)
            db.session.commit()
        else:
            abort(404)

    def get(self):
        if 'name' in request.args:
            res = Case.query.filter_by(name=request.args['name'])
        else:
            res = Case.query.all()
        data = []
        print(res)
        for item in res:
            tmp = {}
            tmp['name'] = item.name
            tmp['content'] = item.content
            tmp['file_name'] = item.file_name
            tmp['description'] = item.description
            data.append(tmp)
        return data

    def put(self):
        print(request.json)
        print(type(request.json))
        if 'name' in request.json:
            name = request.json.get('name')
            case = Case.query.filter_by(name=name).first()
            case.content = request.json.get('content')
            case.file_name = request.json.get('file_name')
            case.description = request.json.get('description')
            db.session.commit()
            return "change ok"
        else:
            abort('404')

    def delete(self):
        if 'name' in request.args:
            name = request.args['name']
            case = Case.query.filter_by(name=name).first()
            if case is not None:
                print("11")
                db.session.delete(case)
                db.session.commit()
                return "delete ok"
            else:
                return "数据已删除，请刷新"


api.add_resource(CaseSaveAsFile, '/CaseSaveAsFile')
api.add_resource(TestCase, '/testcase')
if __name__ == "__main__":
    # db.drop_all()
    # db.create_all()
    app.run(debug=True)
