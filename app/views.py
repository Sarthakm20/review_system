from flask import Blueprint, request, jsonify
from app.csv_upload import upload_csv
from app.models import get_movies
from app.utils import paginate_data

app = Blueprint('app', __name__)

# API for CSV upload
@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"message": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400

    num_movies = upload_csv(file)
    return jsonify({"message": f"Successfully uploaded {num_movies} movies"}), 200

# API for viewing movies
@app.route('/movies', methods=['GET'])
def movies():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    sort_by = request.args.get('sort_by', 'release_date')
    order = request.args.get('order', 'asc')
    
    # Fetching movies from DB
    movies_data = get_movies(page, per_page, sort_by, order)
    
    return jsonify(movies_data)
