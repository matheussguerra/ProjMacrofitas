from flask import Flask, render_template
from web.landingPage.controller import index_blueprint
from web.dataSummarizerController.summarizer import summarizer_blueprint
from web.dataSummarizerController.indexController import index_dataBlueprint

app = Flask(__name__)

app.register_blueprint(index_blueprint)
app.register_blueprint(summarizer_blueprint)
app.register_blueprint(index_dataBlueprint)