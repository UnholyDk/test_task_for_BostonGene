import os

from flask import request, jsonify
from server import app, db
from models import Answer


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/create_calc', methods=['POST'])
def create_request_calc():
    try:
        expression = request.json['expression']
        variables = request.json['variables']
        result = eval(expression, variables)

        answer = Answer(result)
        db.session.add(answer)
        db.session.commit()

        return jsonify({'expression_id': answer.id}), 200
    except Exception as err:
        return jsonify({'error': str(err)}), 400


@app.route('/get_result/<int:calc_id>', methods=['GET'])
def get_result(calc_id):
    obj = db.session.query(Answer).filter_by(id=calc_id).first()
    if obj is None:
        return jsonify({'error': 'Expression with given id not found'}), 404
    return jsonify({'result': obj.result}), 200


app.run(host='0.0.0.0', port=int(os.environ.get('HTTP_FLASK_PORT', 80)))
