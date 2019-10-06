from flask import Flask, render_template, request, jsonify, json, flash
import datetime
from ssl import SSLContext, PROTOCOL_SSLv23
from py_scripts.find_astro_sign import find_sign

import re

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

@app.route('/horoscope', methods=['POST'])
def display_horoscope():
    last_name = request.form['last_name_input']
    first_name = request.form['first_name_input']
    birthday_date = request.form['birthday_date']
    status = ''

    check_date = re.match('(\d{2})[/.-](\d{2})[/.-](\d{4})$',birthday_date)

    # Validate input
    if last_name == '':
        status += 'Il manque le nom de famille \n'

    if first_name == '':
        status += 'Il manque le prénom \n'

    if birthday_date == '':
        status += 'Il manque la date de naissance \n'

    if not check_date:
        status += 'Veuillez entrer une date sous la forme mm/dd/yyyy'

    print(status)
    if status:
        return render_template('horoscope_display.html', status=status)

    date = datetime.datetime.strptime(birthday_date, "%m/%d/%Y")

    print(last_name)
    print(first_name)
    print(date)

    #
    astro_sign = find_sign(date.month, date.day)
    print(astro_sign)

    return render_template('horoscope_splay.html', astro_sign=astro_sign)
    # return jsonify(astro_sign)
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
    app.run(host='127.0.0.1', debug=True, port=8080)
    # app.run()