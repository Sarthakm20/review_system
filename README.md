This project is a movie content management system allowing the content team to upload movie-related data using a CSV file and providing APIs to fetch and manage the data.

**Tech Stack**

Backend: Python (Flask)

Database: MongoDB

Dependencies: Flask, pandas, pymongo

**Features**

CSV Upload API - Uploads movie data from a CSV file (up to 1GB)

Movies List API - Fetches paginated movie data with filtering & sorting options

Filtering: Year of release, Language

Sorting: Release Date (asc/desc), Rating (asc/desc)

**Setup Instructions**

1. Clone the Repository
git clone https://github.com/Sarthakm20/review_system.git
cd review_system
2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Mac/Linux

venv\Scripts\activate  # On Windows
4. Install Dependencies
pip install -r requirements.txt
5. Configure MongoDB
Ensure MongoDB is installed and running.
Update config.py with the MongoDB connection URI.
6. Run the Application
python run.py
Server should start at http://127.0.0.1:5000/.

**API Endpoints**

1. Upload CSV
   Endpoint: POST http://127.0.0.1:5000/upload
   
   Description: Uploads a CSV file containing movie data.

2. Fetch Movies
   Endpoint: GET http://127.0.0.1:5000/movies

   Query Parameters:

   page (default: 1)

   limit (default: 10)

   year (optional, filters by release year)

   language (optional, filters by language)

   sort_by (options: release_date or rating)

   order (values: asc or desc)

**Testing the APIs**

Use Postman to test the APIs.

1) Upload the CSV file
   
   POST and enter the Endpoint:http://127.0.0.1:5000/upload

   In the "Body" tab, select "form-data"

   Add a key named file and upload your CSV file and Type="File" and upload the file from the local computer and it should be in CSV format or else, error will be thrown

2) View Movies:
   
   Endpoint: http://127.0.0.1:5000/movies

   Method: GET

      A) to Test pagination
   
         Enter Url: http://127.0.0.1:5000/movies?page=1&limit=10

      B) to Test Filtering
   
         Enter Url: http://127.0.0.1:5000/movies?year=2020 (for year)
   
         Enter Url: http://127.0.0.1:5000/movies?language=English (for language)

      C) to Test Sorting
   
         Enter Url: http://127.0.0.1:5000/movies?sort=release_date&order=asc (ascending order)
   
         Enter Url: http://127.0.0.1:5000/movies?sort=rating&order=desc (descending order)
