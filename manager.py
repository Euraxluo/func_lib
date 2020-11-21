# -*- coding: utf-8 -*-
from flask import Flask
from flask_script import Manager
from manage import register_route,build_from_database
from service import service_route
from conf import REGISTER_ROUTE,SERVICE_ROUTE,SERVER_HOST,SERVER_PORT
def run_before(handler:list):
    for h in handler:
        h()
    return Flask(__name__)

app = run_before([build_from_database])
app.register_blueprint(register_route, url_prefix=REGISTER_ROUTE)
app.register_blueprint(service_route, url_prefix=SERVICE_ROUTE)
manager = Manager(app)


if __name__ == '__main__':
    manager.run()
