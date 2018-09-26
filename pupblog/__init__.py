from flask import Flask 

app = Flask(__name__)

from pupblog.core.views import core
app.register_blueprint(core)


from pupblog.error_pages.handlers import error_pages
app.register_blueprint(error_pages)