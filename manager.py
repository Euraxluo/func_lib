# -*- coding: utf-8 -*-
from flask import Flask
from flask_script import Manager
from manage import register_route


if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(register_route, url_prefix='/register')
    manager = Manager(app)
    manager.run()