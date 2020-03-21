# TO WORK ON SERVER:
# SET ENTIRE FOLDER (with py/html/css) AS VIRTUAL NETWORK - python -m venv ResumeWebsite
# scripts\activate
# set FLASK_APP=server.py
# turn debug mode on to automatically keep changes without restarting server - set FLASK_ENV=development
# flask run


# allows us to send HTML files
from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def about(page_name):
    return render_template(page_name)  # the html file


def write_to_file(data):
    # opening database text file and appending with 'mode=a'
    with open('database.txt', mode='a') as database:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f"\n{name},{email},{subject},{message}")


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        name = data['name']  # from HTML 'name' attribute!
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()  # get email/name/subject as dictionary in terminal
            # pass in the GET data to write_to_file where it will be put into database
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'error!'


# A server sends data, can send data through API endpoints

# @app.route('/')  # return this at the root directory
# def hello_world():
#     # turn debug mode on to automatically keep changes without restarting server - set FLASK_ENV=development
#     return render_template('index.html')
#     # this is used to refer to the HTML file in templates folder


# # make URL more specific, need /aaliyan/2 and it will output
# @app.route('/<username>/<int:post_id>')
# # use this to show outputs based on inputs on html with {{ name }}
# def specific(username=None, post_id=None):
#     return render_template('index.html', name=username, post_id=post_id)
