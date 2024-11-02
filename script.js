document.getElementById("locationBtn").addEventListener("click", getLocation);
document.getElementById("getRecommendationsBtn").addEventListener("click", getRecommendations);

let userLocation = null;

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition((position) => {
            userLocation = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };
            document.getElementById("categorySelection").style.display = "block";
            loadCategories();
        });
    } else {
        alert("Geolocation is not supported by this browser.");
    }
}

function loadCategories() {
    fetch("http://localhost:5000/categories")
        .then(response => response.json())
        .then(categories => {
            const categorySelect = document.getElementById("category");
            categorySelect.innerHTML = "";
            for (let mainCategory in categories) {
                const optGroup = document.createElement("optgroup");
                optGroup.label = mainCategory;
                categories[mainCategory].forEach(subCategory => {
                    const option = document.createElement("option");
                    option.value = subCategory;
                    option.textContent = subCategory;
                    optGroup.appendChild(option);
                });
                categorySelect.appendChild(optGroup);
            }
        });
}

function getRecommendations() {
    const category = document.getElementById("category").value;
    if (!userLocation || !category) {
        alert("Please share your location and select a category.");
        return;
    }

    fetch("http://localhost:5000/recommendations", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            location: userLocation,
            category: category
        })
    })
    .then(response => response.json())
    .then(recommendations => {
        showRecommendations(recommendations);
    });
}

function showRecommendations(recommendations) {
    const map = new google.maps.Map(document.getElementById("map"), {
        center: userLocation,
        zoom: 15
    });

    new google.maps.Marker({
        position: userLocation,
        map: map,
        title: "Your Location"
    });

    const tableBody = document.getElementById("recommendationsTable").querySelector("tbody");
    tableBody.innerHTML = ""; // Clear previous results

    recommendations.forEach(place => {
        // Place markers on the map
        new google.maps.Marker({
            position: { lat: place.latitude, lng: place.longitude },
            map: map,
            title: place.name
        });

        // Populate table with results
        const row = document.createElement("tr");
        row.innerHTML = `<td>${place.name}</td><td>${place.rating}</td><td>${place.address}</td>`;
        tableBody.appendChild(row);
    });

    document.getElementById("recommendationsTable").style.display = "table";
}
