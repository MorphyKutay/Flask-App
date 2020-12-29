from flask import Flask, url_for,render_template,request
from markupsafe import escape
from werkzeug.middleware.proxy_fix import ProxyFix


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html') 





@app.errorhandler(404)
def page_not_found(error):
    return render_template('hata.html'), 404



app.logger.debug('A value for debugging')
app.logger.warning('A warning occurred (%d apples)', 42)
app.logger.error('An error occurred')

app.wsgi_app = ProxyFix(app.wsgi_app)




