import csv
import email_sender
from flask import Flask, render_template,request,redirect

app = Flask(__name__)

@app.route("/<page_name>")
def html_page(page_name):
    return render_template(page_name)

@app.route("/")
def hello_world2():
    return render_template('index.html')

@app.route("/submit_form",methods = ['POST','GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_database(data)
            email_sender.send_mail(data['name'],data['email'])
            return redirect('thank_you.html')
        except:
            return 'Didn\'t save to database'
    else:
        return 'Something went wrong!!!'
    
def write_to_database(data):
    with open('database.csv', mode="+a",newline='') as db:
        csvwriter = csv.DictWriter(db,fieldnames=['name','email','message'])
        csvwriter.writerow(data)

        
        
