from flask import Flask, render_template,request,redirect

app = Flask(__name__)

@app.route("/<page_name>")
def html_page(page_name):
    print(page_name)
    return render_template(page_name)

@app.route("/")
def hello_world2():
    return render_template('index.html')

@app.route("/submit_form",methods = ['POST','GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        return redirect('thank_you.html')
    



