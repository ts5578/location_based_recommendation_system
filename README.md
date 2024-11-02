
# Project Title

A brief description of what this project does and who it's for

Here's a sample `README.md` for the location-based recommendation system:

---

# Location-Based Recommendation System

This project is a location-based recommendation system that provides users with recommendations for places based on their current location and selected categories. The application utilizes a Google Maps interface with pinned locations and a sortable table of recommended spots, aiming to enhance user experience by delivering highly relevant recommendations.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [File Overview](#file-overview)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Features

- Dynamic location-based recommendations using Google Maps.
- Category selection with subcategories for easier navigation.
- Recommendations are displayed with sorting options (by distance and rating).
- Back-end integration with Flask for processing recommendations.
- Machine learning model integration for personalized recommendations.

## Project Structure

```plaintext
├── app.py                    # Main Flask app with route handling and backend logic
├── final_states_dataset.csv   # Dataset used for location-based recommendations
├── index.html                 # Main HTML template for the web app
├── model_analysis.ipynb       # Jupyter notebook with model analysis for recommendations
├── model_recommender.keras    # Trained recommendation model file
├── recommendation_logic.py    # Logic for recommendation calculations
├── requirements.txt           # Required Python libraries
├── script.js                  # JavaScript for client-side logic
└── style.css                  # CSS for styling the app
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/location-based-recommendation.git
   cd location-based-recommendation
   ```

2. **Install dependencies:**
   Install the required Python packages from `requirements.txt`.
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Google Maps API:**
   - Obtain a Google Maps API key and replace `YOUR_GOOGLE_MAPS_API_KEY` in `script.js`.
   
4. **Run the app:**
   ```bash
   python app.py
   ```
   The app should now be running on `http://127.0.0.1:5000`.

## Usage

1. **Open the Welcome Page:** Start by accessing the app in your browser.
2. **Allow Location Access:** Enable location access to get location-specific recommendations.
3. **Select a Category:** Choose a category from the dropdown to filter recommendations.
4. **View Recommendations:** See the recommended locations on Google Maps and in a sortable table.

## File Overview

- **app.py:** The main Flask application file. Manages routes, loads data, and handles backend recommendation processing.
- **final_states_dataset.csv:** Dataset containing location data and categories for recommendation generation.
- **index.html:** Main HTML template for the application layout, structure, and content.
- **model_analysis.ipynb:** Notebook analyzing the recommendation model's performance and behavior.
- **model_recommender.keras:** Saved machine learning model file, providing recommendation logic.
- **recommendation_logic.py:** Contains custom logic for calculating recommendations based on user location, category selection, and additional model processing.
- **requirements.txt:** Lists the Python packages required to run the app.
- **script.js:** Handles client-side JavaScript, including Google Maps integration and user interaction.
- **style.css:** Stylesheets for the application, defining layout, colors, and fonts for a consistent user interface.

## Overview
![Screenshot 2024-10-27 212347](https://github.com/user-attachments/assets/e000e72c-142a-4916-8705-f33dd4179233)
![Screenshot 2024-10-27 212407](https://github.com/user-attachments/assets/9561cdef-ca1d-4927-ab19-0db7b81ec3e4)
![Screenshot 2024-10-27 212421](https://github.com/user-attachments/assets/62aaa24a-feb2-43c9-9676-ced7eb48f15b)
![Screenshot 2024-10-27 212432](https://github.com/user-attachments/assets/d6c24d5b-4077-4907-b95d-247a3a4f474a)



## Technologies Used

- **Python** (Flask, Pandas): For backend processing and web framework.
- **JavaScript** (Google Maps API): For map integration and location display.
- **HTML & CSS:** For front-end structure and styling.
- **Keras:** For building and deploying the recommendation model.
- **Jupyter Notebook:** For model analysis.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request if you'd like to suggest improvements or fixes.

## License

This project is licensed under the MIT License.

---
