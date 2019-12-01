from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cdc560b831cc390eea9f869a6699ec05'

from statsapp import routes