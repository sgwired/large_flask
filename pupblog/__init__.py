from flask import Flask 

app = Flask(__name__)

from pupblog.core.views import core
app.register_blueprint(core)
