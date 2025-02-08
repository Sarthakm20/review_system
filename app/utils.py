import pandas as pd

def process_csv(file_path):
    """
    Parses the CSV file, reads the data, and returns it as a list of dictionaries
    """
    df = pd.read_csv(file_path)
    # Here, we can add additional validations or transformations if needed
    movies_list = df.to_dict(orient="records")
    return movies_list

def paginate_data(data, page, per_page):
    """
    Helper function to paginate the data for response
    """
    start = (page - 1) * per_page
    end = start + per_page
    return data[start:end]
