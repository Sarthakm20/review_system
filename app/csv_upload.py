import os
from app import mongo
from app.models import save_movie
from app.utils import process_csv

def upload_csv(file):
    """
    Handles the upload and parsing of the CSV file, stores the data into MongoDB
    """
    file_path = os.path.join(os.getcwd(), 'uploads', file.filename)
    
    # Save the uploaded CSV file to disk
    file.save(file_path)
    
    # Process CSV file and store the data in MongoDB
    movies_data = process_csv(file_path)
    
    # Insert each movie record into MongoDB
    for movie in movies_data:
        save_movie(movie)
    
    # Optionally, remove the uploaded file after processing
    os.remove(file_path)
    return len(movies_data)  # Return number of records processed
