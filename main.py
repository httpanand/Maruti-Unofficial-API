from flask import Flask,request,jsonify
from flask import render_template

app = Flask(__name__)

@app.route('/')
def html():
	return render_template('main.html')

alto = [{
	"Fuel Type":"Petrol,CNG",
	"Mileage":"22-31 km/l",
	"Length":"3445mm",
	"Width":"1490mm",
	"Height":"1475mm",
	"Wheelbase":"2360mm",
	"Ground Clearance":"160mm",
	"Boot Space":"177L",
	"Starting Price":"3.5L"
}]

celerio = [{
	"Fuel Type":"Petrol,Diesel,CNG",
	"Mileage":"22-31 km/l",
	"Length":"3695mm",
	"Width":"1600mm",
	"Height":"1560mm",
	"Wheelbase":"2425mm",
	"Ground Clearance":"165mm",
	"Boot Space":"235L",
	"Starting Price":"4.6L"
}]

baleno = [{
	"Fuel Type":"Petrol,Diesel",
	"Mileage":"20-24 km/l",
	"Length":"3995mm",
	"Width":"1745mm",
	"Height":"1510mm",
	"Wheelbase":"2520mm",
	"Ground Clearance":"170mm",
	"Boot Space":"339L",
	"Starting Price":"5.9L"
}]

@app.route('/api/alto', methods=['GET'])
def al():
    return jsonify(alto)

@app.route('/api/celerio', methods=['GET'])
def cel():
    return jsonify(celerio)

@app.route('/api/baleno', methods=['GET'])
def bal():
    return jsonify(baleno)


if __name__ == '__main__':
  app.debug = True
  app.run(host="0.0.0.0", port=8080)


