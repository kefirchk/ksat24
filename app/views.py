from flask import Blueprint, render_template, request, jsonify
from app.services import InputService


main_bp = Blueprint('main', __name__)
input_service = InputService()


@main_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form.to_dict()
        input_service.save(data)
        return jsonify(data)
    return render_template('index.html')


@main_bp.route('/results')
def get_results():
    results = input_service.get_all()
    return render_template('results.html', results=results)
