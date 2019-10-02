from flask import Flask, render_template, request, jsonify, json
import datetime
from ssl import SSLContext, PROTOCOL_SSLv23
from py_scripts.find_astro_sign import find_sign

app = Flask(__name__)

# If GET, display normal page
@app.route('/', methods=['GET'])
@app.route('/', methods=['POST'])
def home():
    if request.method == 'POST':
        first_name = request.form['first_name_input']
        last_name = request.form['last_name_input']
        birthday_date = request.form['birthday_date']


    return render_template('accueil.html', page_title='Horoscope', app_title='Horoscope')

# @app.route('/horoscope')
# def add_numbers():
#     a = request.args.get('a', 0, type=int)
#     b = request.args.get('b', 0, type=int)
#     return jsonify(result=a + b)

@app.route('/horoscope', methods=['GET', 'POST'])
def display_horoscope():
    print(request.form)
    last_name = request.form['last_name_input']
    first_name = request.form['first_name_input']

    date = datetime.datetime.strptime(request.form['birthday_date'], "%m/%d/%Y")

    astro_sign = find_sign(date.month, date.day)
    print(astro_sign)

    # if request.method == "POST":
    #     clicked = request.json['data']

    # return render_template('accueil.html',data='salut', last_name='salut', first_name=first_name, zodiac_sign=astro_sign)
    return jsonify(astro_sign)
    # last_name = request.args.get('last_name_input', 0, type=str)
    # first_name = request.args.get('first_name_input', 0, type=str)
    # birthday_date = request.args.get('birthday_date', 0, type=str)
    # print(last_name)
    # print(first_name)
    # print(birthday_date)
    # date = datetime.datetime.strptime(birthday_date, "%m/%d/%Y")
    #
    # astro_sign = find_sign(date.month, date.day)
    # print(astro_sign)
    #
    # return jsonify(result=astro_sign, result2=last_name)

# If page not found, display this html
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404_error.html", page_name=request.path.split('/')[1])

# When called, run the server
if __name__ == '__main__':
    context = SSLContext(PROTOCOL_SSLv23)
    context.load_cert_chain('./SSL.crt', './SSL.key')
    app.run(host='127.0.0.1', debug=True, port=8080, ssl_context=context)