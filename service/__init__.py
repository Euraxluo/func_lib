from flask import Blueprint
import os
service_route = Blueprint('service', __name__,
                         template_folder=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates'),
                         static_folder=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static')
                         )
import service.server