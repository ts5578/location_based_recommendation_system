from flask import Flask, request, jsonify
from flask_cors import CORS
from recommendation_logic import get_recommendations

app = Flask(__name__)
CORS(app)

CATEGORIES = {
    "Food & Beverage": [
        "Coffee shop", "Bakery", "Restaurant", "Dessert shop", "Tea store", "Ice Cream",
        "Fast Food", "Vegetarian", "Patisserie", "Chocolate shop", "Gourmet grocery store", "Grocery store"
    ],
    "Clothing & Accessories": [
        "Clothing store", "Men's clothing store", "Women's clothing store", "Boutique", "Saree Shop",
        "Designer Clothing Store", "Plus Size Clothing Store", "Youth clothing store", "Lingerie store",
        "T-shirt store", "Costume store"
    ],
    "Shopping": [
        "Shopping mall", "Department store", "Supermarket", "Antique store", "General store", "Toy store",
        "Boutique", "Furniture store", "Jewelry store", "Electronics store", "Book store", "Convenience store",
        "Hypermarket", "Outlet store"
    ],
    "Specialty Shops": [
        "Antique furniture store", "Organic food store", "Perfume store", "Pet store", "Art supply store",
        "Camera store", "Computer store", "Musical instrument store", "Health and beauty shop",
        "Sports nutrition store", "Art gallery"
    ],
    "Health & Wellness": [
        "Pharmacy", "Optician", "Dental supply store", "Beauty supply store", "Health food store",
        "Veterinary pharmacy", "Weight loss service", "Eye care center", "Fitness center"
    ],
    "Leisure & Recreation": [
        "Museum", "Zoo", "National park", "Beach", "Botanical garden", "Hiking area", "Historical landmark",
        "Art center", "Monastery", "Amusement park", "Beach entertainment shop", "Aquarium shop",
        "Wildlife and safari park", "Historical place museum"
    ],
    "Automotive & Hardware": [
        "Auto parts store", "Tire shop", "Motorcycle parts store", "Auto accessories store",
        "Auto electrical service", "Car dealer", "Scooter rental service", "Mechanic", "Battery Store",
        "Car Service Station"
    ],
    "Tourism & Travel": [
        "Travel agency", "Tourist attraction", "Picnic ground", "Hotel", "Resort hotel", "Guest house",
        "Bed & breakfast", "Tourism department", "Taxi service", "Boat tour agency", "Boat dealer",
        "SCUBA tour agency"
    ],
    "Services": [
        "Real Estate", "Builders", "Housing society", "Beauty Parlour", "Tattoo shop", "Barber shop", 
        "Tailor", "Custom tailor", "Astrologer", "Photographer", "Wedding photographer", "Graphic designer",
        "Website designer", "Marketing consultant", "Insurance agency"
    ],
    "Education & Arts": [
        "Art gallery", "Art cafe", "Photography studio", "Art supply store", "Bookbinder", "Library",
        "School supply store", "Museum", "Photography Class"
    ]
}

@app.route('/categories', methods=['GET'])
def get_categories():
    return jsonify(CATEGORIES)

@app.route('/recommendations', methods=['POST'])
def recommendations():
    try:
        # Get data from request
        data = request.get_json()
        location = data.get('location')
        category = data.get('category')
        
        # Validate data
        if not location or not category:
            return jsonify({"error": "Location and category are required"}), 400
        if category not in CATEGORIES:
            return jsonify({"error": "Invalid category"}), 400

        # Call recommendation logic
        recommendations = get_recommendations(location, category)
        return jsonify(recommendations)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)