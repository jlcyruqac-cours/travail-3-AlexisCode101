from flask import Flask, render_template, request, jsonify
import hashlib
from ssl import SSLContext, PROTOCOL_SSLv23

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
def test():
    clicked = None
    print(request.form)
    # if request.method == "POST":
    #     clicked = request.json['data']
    return render_template('accueil.html')

# If page not found, display this html
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404_error.html", page_name=request.path.split('/')[1])

# When called, run the server
if __name__ == '__main__':
    context = SSLContext(PROTOCOL_SSLv23)
    context.load_cert_chain('./SSL.crt', './SSL.key')
    app.run(host='127.0.0.1', debug=True, port=8080, ssl_context=context)