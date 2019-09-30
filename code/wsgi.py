from app import app
from ssl import SSLContext, PROTOCOL_SSLv23

if __name__ == '__main__':
    context = SSLContext(PROTOCOL_SSLv23)
    context.load_cert_chain('./SSL.crt', './SSL.key')
    app.run(host='127.0.0.1', debug=True, port=8080, ssl_context=context)
#
#
# # def application(env, start_response):
# #     start_response('200 OK', [('Content-Type','text/html')])
# #     return [b"Hello World"]