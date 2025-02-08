from app import mongo

# Save movie to MongoDB
def save_movie(movie_data):
    movie = {
        "title": movie_data['title'],
        "original_title": movie_data['original_title'],
        "overview": movie_data['overview'],
        "release_date": movie_data['release_date'],
        "budget": movie_data['budget'],
        "revenue": movie_data['revenue'],
        "runtime": movie_data['runtime'],
        "status": movie_data['status'],
        "vote_average": movie_data['vote_average'],
        "vote_count": movie_data['vote_count'],
        "languages": movie_data['languages']
    }
    return mongo.db.movies.insert_one(movie)

# Fetch movies from MongoDB with pagination and sorting
def get_movies(page, per_page, sort_by, order):
    skip = (page - 1) * per_page
    sort_order = 1 if order == 'asc' else -1
    
    movies = mongo.db.movies.find().skip(skip).limit(per_page).sort(sort_by, sort_order)
    movie_list = list(movies)
    
    for movie in movie_list:
        movie["_id"] = str(movie["_id"])  # Convert ObjectId to string for JSON serialization
    
    return {
        "data": movie_list,
        "total_results": mongo.db.movies.count_documents({}),
        "total_pages": (mongo.db.movies.count_documents({}) + per_page - 1) // per_page
    }
