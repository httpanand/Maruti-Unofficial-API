from flask import Flask,request,jsonify
from flask import render_template

app = Flask(__name__)

@app.route('/')
def html():
	return render_template('main.html')

@app.route('/api')
def noaccess():
	return render_template('cars.html')

alto = [{
	"Fuel Type":"Petrol,CNG",
	"Mileage":"22-31 km/l",
	"Length":"3445mm",
	"Width":"1490mm",
	"Height":"1475mm",
	"Wheelbase":"2360mm",
	"Ground Clearance":"160mm",
	"Boot Space":"177l",
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
	"Boot Space":"235l",
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
	"Boot Space":"339l",
	"Starting Price":"5.9L"
}]

ciaz = [{
	"Fuel Type":"Petrol,Diesel",
	"Mileage":"20-21 km/l",
	"Length":"4490mm",
	"Width":"1730mm",
	"Height":"1485mm",
	"Wheelbase":"2650mm",
	"Ground Clearance":"170mm",
	"Boot Space":"510l",
	"Starting Price":"8.6L"
}]

dzire  = [{
	"Fuel Type":"Petrol,Diesel",
	"Mileage":"23-24 km/l",
	"Length":"3995mm",
	"Width":"1735mm",
	"Height":"1515mm",
	"Wheelbase":"2450mm",
	"Ground Clearance":"163mm",
	"Boot Space":"378l",
	"Starting Price":"5.9L"
}]

ertiga  = [{
	"Fuel Type":"Petrol,Diesel,CNG",
	"Mileage":"18-26 km/l",
	"Length":"4395mm",
	"Width":"1735mm",
	"Height":"1690mm",
	"Wheelbase":"2740mm",
	"Ground Clearance":"185mm",
	"Boot Space":"209l",
	"Starting Price":"7.9L"
}]

ignis  = [{
	"Fuel Type":"Petrol,Diesel",
	"Mileage":"20 km/l",
	"Length":"3700mm",
	"Width":"1690mm",
	"Height":"1595mm",
	"Wheelbase":"2435mm",
	"Ground Clearance":"180mm",
	"Boot Space":"260l",
	"Starting Price":"5.1L"
}]

ignis  = [{
	"Fuel Type":"Petrol,Diesel",
	"Mileage":"20 km/l",
	"Length":"3700mm",
	"Width":"1690mm",
	"Height":"1595mm",
	"Wheelbase":"2435mm",
	"Ground Clearance":"180mm",
	"Boot Space":"260l",
	"Starting Price":"5.1L"
}]

scross  = [{
	"Fuel Type":"Petrol,Diesel",
	"Mileage":"18-19 km/l",
	"Length":"4300mm",
	"Width":"1785mm",
	"Height":"1595mm",
	"Wheelbase":"2600mm",
	"Ground Clearance":"180mm",
	"Boot Space":"375l",
	"Starting Price":"8.5L"
}]

@app.route('/api/alto', methods=['GET'])
def alt():
    return jsonify(alto)

@app.route('/api/celerio', methods=['GET'])
def cel():
    return jsonify(celerio)

@app.route('/api/baleno', methods=['GET'])
def bal():
    return jsonify(baleno)

@app.route('/api/ciaz', methods=['GET'])
def cia():
    return jsonify(ciaz)

@app.route('/api/dzire', methods=['GET'])
def dzi():
    return jsonify(dzire)

@app.route('/api/ertiga', methods=['GET'])
def ert():
    return jsonify(ertiga)

@app.route('/api/ignis', methods=['GET'])
def ign():
    return jsonify(ignis)

@app.route('/api/scross', methods=['GET'])
def scr():
    return jsonify(scross)

if __name__ == '__main__':
  app.debug = True
  app.run(host="0.0.0.0", port=8080)


