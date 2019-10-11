import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_nav import Nav, register_renderer
from App.Navbar.NavbarRenderer import AppRenderer

app = Flask(__name__, template_folder=os.path.normpath("../templates"), static_folder=os.path.normpath("../static"))
nav = Nav()
boot = Bootstrap()

boot.init_app(app)
nav.init_app(app)
register_renderer(app, 'app_renderer', AppRenderer)
