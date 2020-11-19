from flask import Blueprint
import os
register_route = Blueprint('register', __name__,
                         template_folder=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates'),
                         static_folder=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static')
                         )
import manage.register