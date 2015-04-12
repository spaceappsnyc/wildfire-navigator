from flask import Flask, request
from flask_restful import Resource, Api
import pyupm_i2clcd as lcd


app = Flask(__name__)
api = Api(app)

msgs = {}

def alert_lcd():
	x = lcd.Jhd1313m1(0, 0x3E, 0x62)
	tempstr="                  "
	x.setCursor(0,0)
	x.setColor(255,0,0)
	x.write('High Temp!!!')

def norm_lcd():
	x = lcd.Jhd1313m1(0, 0x3E, 0x62)
	tempstr="                  "
	x.setCursor(0,0)
	x.setColor(0,0,255)
	x.write('Normal Temp')

class TodoSimple(Resource):
    def get(self, msg_id):
        return {msg_id: msgs[msg_id]}

    def put(self, msg_id):
        msgs[msg_id] = request.form['data']
        if msgs[msg_id]=='alert':
        	alert_lcd()
        else:
        	norm_lcd()
        return {msg_id: msgs[msg_id]}

api.add_resource(TodoSimple, '/<string:msg_id>')

if __name__ == '__main__':
    app.run(host='192.168.0.112', debug=False)
