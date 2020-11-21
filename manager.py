# -*- coding: utf-8 -*-
from flask import Flask
from flask_script import Manager
from manage import register_route
from service import service_route

app = Flask(__name__)
app.register_blueprint(register_route, url_prefix='/register')
app.register_blueprint(service_route, url_prefix='/service')
manager = Manager(app)


if __name__ == '__main__':
    manager.run()
