from django.shortcuts import render

# ---------------------------------------
# TEMPORARY CAFE DATA (you can replace later)
# ---------------------------------------
# frontend/views.py — replace the CAFES dict with this
CAFES = {
    "north": [
        {
            "id": 1,
            "name": "North Cafe 1",
            "intro": "Quiet study nook with reliable Wi-Fi and comfy seating.",
            "price": "200",
            "campus": "north",
            "menu_items": [
                {"item": "Cappuccino", "price": "₹80"},
                {"item": "Cheese Sandwich", "price": "₹90"},
                {"item": "Chocolate Brownie", "price": "₹70"}
            ],
            "menu_images": ["frontend/images/cafes/north/north_cafe1_menu/m1n1.jpg", "frontend/images/cafes/north/north_cafe1_menu/m2n1.jpg", "frontend/images/cafes/north/north_cafe1_menu/m3n1.jpg", "frontend/images/cafes/north/north_cafe1_menu/m4n1.jpg"],
            "cafe_images": ["frontend/images/cafes/north/north_cafe1_images/imgn1.jpg"]
        },
        {
            "id": 2,
            "name": "North Cafe 2",
            "intro": "Warm interiors and hearty snacks — great for late study sessions.",
            "price": "250",
            "campus": "north",
            "menu_items": [
                {"item": "Flat White", "price": "₹100"},
                {"item": "Veg Wrap", "price": "₹120"},
                {"item": "Iced Tea", "price": "₹70"}
            ],
            "menu_images": ["frontend/images/cafes/north/north_cafe2_menu/bp.jpg", "frontend/images/cafes/north/north_cafe2_menu/in.jpg", "frontend/images/cafes/north/north_cafe2_menu/home_back.jpg"],
            "cafe_images": ["frontend/images/cafes/north/north_cafe2_images/bp.jpg", "frontend/images/cafes/north/north_cafe2_images/in.jpg", "frontend/images/cafes/north/north_cafe2_images/home_back.jpg"]
        }
    ],
    "south": [
        {
            "id": 3,
            "name": "South Cafe 1",
            "intro": "Artisan coffee and picture-perfect decor for cosy hangs.",
            "price": "180",
            "campus": "south",
            "menu_items": [
                {"item": "Latte", "price": "₹90"},
                {"item": "Pasta Bowl", "price": "₹160"},
                {"item": "Brown Sugar Cookie", "price": "₹60"}
            ],
            "menu_images": ["frontend/images/cafes/south/south_cafe1_menu/bp.jpg", "frontend/images/cafes/south/south_cafe1_menu/in.jpg", "frontend/images/cafes/south/south_cafe1_menu/home_back.jpg"],
            "cafe_images": ["frontend/images/cafes/south/south_cafe1_images/bp.jpg", "frontend/images/cafes/south/south_cafe1_images/in.jpg", "frontend/images/cafes/south/south_cafe1_images/home_back.jpg"]
        },
        {
            "id": 4,
            "name": "South Cafe 2",
            "intro": "Pocket-friendly bites and refreshing drinks under ₹150.",
            "price": "150",
            "campus": "south",
            "menu_items": [
                {"item": "Espresso", "price": "₹60"},
                {"item": "Paneer Roll", "price": "₹110"},
                {"item": "Lemonade", "price": "₹50"}
            ],
            "menu_images": ["frontend/images/cafes/south/south_cafe2_menu/bp.jpg", "frontend/images/cafes/south/south_cafe2_menu/in.jpg", "frontend/images/cafes/south/south_cafe2_menu/home_back.jpg"],
            "cafe_images": ["frontend/images/cafes/south/south_cafe2_images/bp.jpg", "frontend/images/cafes/south/south_cafe2_images/in.jpg", "frontend/images/cafes/south/south_cafe2_images/home_back.jpg"]
        }
    ],
    "off": [
        {
            "id": 5,
            "name": "Off Campus Cafe 1",
            "intro": "Lively neighbourhood spot with sharable plates and chilled playlists.",
            "price": "220",
            "campus": "off",
            "menu_items": [
                {"item": "Cold Brew", "price": "₹120"},
                {"item": "Nachos", "price": "₹180"},
                {"item": "Cheesecake Slice", "price": "₹160"}
            ],
            "menu_images": ["frontend/images/cafes/off/off_campus_cafe1_menu/m1o1.jpg", "frontend/images/cafes/off/off_campus_cafe1_menu/m2o1.jpg"],
            "cafe_images": ["frontend/images/cafes/off/off_campus_cafe1_images/imgs1.jpg"]
        },
        {
            "id": 6,
            "name": "Off Campus Cafe 2",
            "intro": "Low-noise corner ideal for focused work and long reads.",
            "price": "170",
            "campus": "off",
            "menu_items": [
                {"item": "Matcha Latte", "price": "₹110"},
                {"item": "Club Sandwich", "price": "₹140"},
                {"item": "Blueberry Muffin", "price": "₹70"}
            ],
            "menu_images": ["frontend/images/cafes/off/off_campus_cafe2_menu/bp.jpg", "frontend/images/cafes/off/off_campus_cafe2_menu/in.jpg", "frontend/images/cafes/off/off_campus_cafe2_menu/home_back.jpg"],
            "cafe_images": ["frontend/images/cafes/off/off_campus_cafe2_images/bp.jpg", "frontend/images/cafes/off/off_campus_cafe2_images/in.jpg", "frontend/images/cafes/off/off_campus_cafe2_images/home_back.jpg"]
        }
    ]
}

# ---------------------------------------
# FIRST PAGE → EXPLORE DU CAFÉS
# ---------------------------------------
def explore(request):
    # Take 1–2 highlights from each campus
    highlights = []
    for key in ("north", "south", "off"):
        highlights += CAFES.get(key, [])[:1]

    return render(request, "explore.html", {"highlights": highlights})


# ---------------------------------------
# SECOND PAGE → CAMPUS OVERVIEW (3 BOXES)
# ---------------------------------------
def campuses_overview(request):
    return render(request, "campuses_overview.html", {
        "intro": "Browse campus-wise cafes",
    })


# ---------------------------------------
# PAGE 3 → LIST OF CAFES IN THAT CAMPUS
# ---------------------------------------
def campus_list(request, campus):
    cafes = CAFES.get(campus, [])
    return render(request, "campus_list.html", {
        "campus": campus,
        "cafes": cafes,
    })


# ---------------------------------------
# PAGE 4 → CAFE DETAIL PAGE
# ---------------------------------------
def cafe_detail(request, cafe_id):
    # find the cafe by ID
    found = None
    for group in CAFES.values():
        for c in group:
            if c["id"] == cafe_id:
                found = c
                break

    return render(request, "cafe_detail.html", {
        "cafe": found
    })


# ---------------------------------------
# (OPTIONAL) FINDER PAGE
# ---------------------------------------
def finder_home(request):
    return render(request, "finder.html")


