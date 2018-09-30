from flask import render_template, request, Blueprint, abort

core = Blueprint('core', __name__)

@core.route('/')
def index():
  return render_template('index.html')

@core.route('/info')
def info():
  return render_template('info.html')

# @core.route('/someerror')
# def some():
#   return abort(500)