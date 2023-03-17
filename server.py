from flask import Flask, render_template, request, url_for, redirect
import csv

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template('index.html')


@app.route('/<string:page_name>')
def page_route(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'Something went wrong.'


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database:
        name = data['name']
        email = data['email']
        message = data['message']
        csv_write = csv.writer(
            database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow([name, email, message])


if __name__ == '__main__':
    app.run(debug=True)
