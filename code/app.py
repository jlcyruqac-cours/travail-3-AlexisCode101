from flask import Flask, render_template, request
import datetime
from ssl import SSLContext, PROTOCOL_SSLv23
from py_scripts.find_astro_sign import find_sign
import re

app = Flask(__name__)

# Horoscope dictionnary
horoscope_dict =	{
    "Sagittaire": "Vous serez riche.",
    "Capricorne": "Vous ne serez pas riche.",
    "Verseau": "Vous trouverez l'amour.",
    "Poissons": "Vous ne trouverez pas l'amour.",
    "Bélier": "Vous serez chanceux aujourd'hui.",
    "Taureau": "Vous ne serez pas chanceux aujourd'hui.",
    "Gémeaux": "Vous serez riche.",
    "Cancer": "Vous ne serez pas riche.",
    "Lion": "Vous trouverez l'amour.",
    "Vierge": "Vous ne trouverez pas l'amour.",
    "Balance": "Vous serez chanceux aujourd'hui.",
    "Scorpion": "Vous ne serez pas chanceux aujourd'hui."
}

# If GET, display normal page
@app.route('/', methods=['GET'])
@app.route('/', methods=['POST'])
def home():
    return render_template('accueil.html', page_title='Horoscope', app_title='Horoscope')


@app.route('/horoscope', methods=['POST'])
def display_horoscope():
    # Init var with post request
    last_name = request.form['last_name_input']
    first_name = request.form['first_name_input']
    birthday_date = request.form['birthday_date']

    # Init status var
    status = 'Les paramètres suivants sont manquant : '
    status_arg = ''

    # Check if date is correctly formatted
    check_date = re.match('(\d{2})[/.-](\d{2})[/.-](\d{4})$',birthday_date)

    # Validate input
    if last_name == '':
        status_arg += ' | nom de famille | '

    if first_name == '':
        status_arg += ' | prénom | '

    if birthday_date == '':
        status_arg += ' | date de naissance | '

    # If missing input
    if status_arg:
        status += status_arg
        return render_template('input_error.html', status=status)

    # If date incorrectly formatted
    if not check_date:
        status = 'Veuillez entrer une date sous la forme mm/dd/yyyy'
        return render_template('input_error.html', status=status)

    # Transfert birthdate into datetime
    date = datetime.datetime.strptime(birthday_date, "%m/%d/%Y")

    # Call the script to find the astrology sign using the birthdate
    astro_sign = find_sign(date.month, date.day)

    return render_template('horoscope_display.html', astro_sign=astro_sign, horoscope_dict=horoscope_dict[astro_sign],
                           first_name=first_name, last_name=last_name)

# If page not found, display this html
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404_error.html", page_name=request.path.split('/')[1])

# When called, run the server
if __name__ == '__main__':
    # To run with https
    # context = SSLContext(PROTOCOL_SSLv23)
    # context.load_cert_chain('./SSL.crt', './SSL.key')
    # Start the server
    app.run(host='127.0.0.1', debug=True, port=8080)