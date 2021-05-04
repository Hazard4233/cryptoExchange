from flask import Flask, render_template
# from flask_fontawesome import FontAwesome

flaskApp = Flask(__name__)
# fa = FontAwesome(flaskApp)

@flaskApp.route('/dashboard')
def index():
   title = "CryptoCurrency Bot" 
   return render_template('dashboard.html', title = title)
   # return title

@flaskApp.route('/buy')
def buy():
   return 'Buy'


@flaskApp.route('/sell')
def sell():
   return 'sell...'


@flaskApp.route('/settings')
def settings():
   return 'settings'
