from flask import Flask, jsonify, request
import sys
import psycopg2

# Database connection

db_connection = psycopg2.connect(
        dbname='api',
        user='postgres',
        password='helloworld',
        host='localhost',
    )

app = Flask(__name__)

def spcall(qry, param, commit=False):
    try:
        cursor = db_connection.cursor()
        cursor.callproc(qry, param)
        res = cursor.fetchall()
        if commit:
            db_connection.commit()
        return res
    except:
        res = [("Error: " + str(sys.exc_info()[0]) +
                " " + str(sys.exc_info()[1]),)]
    return res

@app.route('/colleges', methods=['GET'])
def get_colleges():
    colleges=spcall('get_colleges', param=None)[0][0]
    return jsonify({"status": "ok",
                    'Message': colleges})

@app.route('/colleges', methods=['POST'])
def create_college():
    data = request.get_json()
    college = data.get('college')
    try:
        if college:
            res=spcall('insert_college', (college, ), commit=True)
            return jsonify({"status": "ok",
                        'message': 'College created successfully'})
    except:
        return {"status":"serverError", "message":str(sys.exc_info()[0]) +
                " " + str(sys.exc_info()[1])}


# Get a specific college by ID
@app.route('/college/<int:college_id>', methods=['GET'])
def get_college(college_id):
    try:
        res = spcall('get_college_by_id', (college_id, ), commit=False)[0][0]
        if res:
            return jsonify({"status": "ok",
                            'message': res})
        else:
            return jsonify({"status": "error",
                            'message': 'College not found'})
    except:
        return {"status":"serverError", "message":str(sys.exc_info()[0]) +
                " " + str(sys.exc_info()[1])}

# Update a College by ID
@app.route('/college/<int:college_id>', methods=['PUT'])
def update_college(college_id):
    try:
        data = request.get_json()
        college = data.get('college')
        if college:
            res = spcall('update_college_by_id', (college_id, college), commit=True)
            return jsonify({"status": "ok",
                            'message': 'College updated successfully'})
    except:
        return {"status":"serverError", "message":str(sys.exc_info()[0]) +
                " " + str(sys.exc_info()[1])}


# Delete a movie by ID
@app.route('/college/<int:college_id>', methods=['DELETE'])
def delete_college(college_id):
    try:
        res = spcall('delete_college_by_id', (college_id, ), commit=True)
        return jsonify({"status": "ok",
                        'message': 'College deleted successfully'})
    except:
        return {"status":"serverError", "message":str(sys.exc_info()[0]) +
                " " + str(sys.exc_info()[1])}

if __name__ == '__main__':
    app.run(debug=True)
