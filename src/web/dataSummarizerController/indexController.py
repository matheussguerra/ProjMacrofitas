from flask import Blueprint, render_template
import os
index_dataBlueprint = Blueprint('index_dataBlueprint', __name__)

@index_dataBlueprint.route('/tabelas', methods=['GET'])
def index():
    return render_template(os.path.join('data','index.html'))
