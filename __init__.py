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

@app.route('/courses', methods=['GET'])
def get_courses():
    courses=spcall('get_courses', param=None)[0][0]
    return jsonify({"status": "ok",
                    'Message': courses})

@app.route('/course', methods=['POST'])
def create_course():
    data = request.get_json()
    course = data.get('course')
    try:
        if course:
            res=spcall('insert_course', (course, ), commit=True)
            return jsonify({"status": "ok",
                        'message': 'course created successfully'})
    except:
        return {"status":"serverError", "message":str(sys.exc_info()[0]) +
                " " + str(sys.exc_info()[1])}


# Get a specific course by ID
@app.route('/course/<int:course_id>', methods=['GET'])
def get_course(course_id):
    try:
        res = spcall('get_course_by_id', (course_id, ), commit=False)[0][0]
        if res:
            return jsonify({"status": "ok",
                            'message': res})
        else:
            return jsonify({"status": "error",
                            'message': 'course not found'})
    except:
        return {"status":"serverError", "message":str(sys.exc_info()[0]) +
                " " + str(sys.exc_info()[1])}

# Update a course by ID
@app.route('/course/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    try:
        data = request.get_json()
        course = data.get('course')
        print(course, course_id)
        
        if course:
            res = spcall('update_course_by_id', (course_id, course), commit=True)
            
            # Check if the update was successful
            if res:  # Assuming 'spcall' returns something meaningful upon success
                return jsonify({"status": "ok", 'message': 'course updated successfully'})
            else:
                return jsonify({"status": "error", 'message': 'course update failed'})

    except Exception as e:
        return jsonify({"status": "serverError", "message": str(e)})

# Delete a movie by ID
@app.route('/course/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    try:
        res = spcall('delete_course_by_id', (course_id, ), commit=True)
        return jsonify({"status": "ok",
                        'message': 'course deleted successfully'})
    except:
        return {"status":"serverError", "message":str(sys.exc_info()[0]) +
                " " + str(sys.exc_info()[1])}

if __name__ == '__main__':
    app.run(debug=True)
