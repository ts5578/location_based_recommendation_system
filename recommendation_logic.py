import pandas as pd
from geopy.distance import geodesic

# Load dataset (ensure the path is correct)
data = pd.read_csv("final_states_dataset.csv")

def get_recommendations(user_location, category):
    user_lat, user_lng = user_location['lat'], user_location['lng']
    
    # Filter dataset based on the selected category
    filtered_data = data[data['category'] == category].copy()

    # Calculate geodesic distance to each place
    filtered_data['distance'] = filtered_data.apply(
        lambda row: geodesic((user_lat, user_lng), (row['latitude'], row['longitude'])).km, axis=1
    )

    # Get the top 5 closest locations
    recommendations = filtered_data.nsmallest(5, 'distance').to_dict('records')

    return {
        'user_lat': user_lat,
        'user_lng': user_lng,
        'recommendations': recommendations
    }
