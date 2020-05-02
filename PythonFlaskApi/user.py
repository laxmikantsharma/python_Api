from app import app
from utility.constant import*
from repositories.userRepository import userRepository
from flask import Response, request, jsonify
import json

@app.route("/userlist/", defaults={"pageNumber": 1,"recordsPerPage":10},methods=['GET'])
@app.route("/userlist/<pageNumber>",methods=['GET'])
@app.route("/userlist/<pageNumber>/<recordsPerPage>",methods=['GET'])
def getUserList(pageNumber,recordsPerPage):
	try:
		data = []
		data = userRepository.getUserList(pageNumber,recordsPerPage)
		return Response(json.dumps( data.__dict__), status=201, mimetype='application/json')
	except Exception as e:
		print(e)
	return

@app.route("/user/<path:loginId>/",methods=['GET'])
def getUser(loginId):
	try:
		data = {}
		data = userRepository.getUserDetail(loginId)
		return Response(json.dumps( data.__dict__, default = datetimeCheck), status=201, mimetype='application/json')
	except Exception as e:
		print(e)
	return



@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone

