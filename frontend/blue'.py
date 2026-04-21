from django.shortcuts import render

# ---------------------------------------
# TEMPORARY CAFE DATA (you can replace later)
# ---------------------------------------
CAFES = {
    "north": [
        {"id": 1, "name": "North Cafe 1", "intro": "Quiet study nook with reliable Wi-Fi and comfortable seating.", "price": "₹200"},
        {"id": 2, "name": "North Cafe 2", "intro": "Warm interiors and hearty snacks — great for late study sessions.", "price": "₹250"},
    ],
    "south": [
        {"id": 3, "name": "South Cafe 1", "intro": "Artisan coffee and picture-perfect decor for cosy hangs.", "price": "₹180"},
        {"id": 4, "name": "South Cafe 2", "intro": "Pocket-friendly bites and refreshing drinks under ₹150.", "price": "₹150"},
    ],
    "off": [
        {"id": 5, "name": "Off Campus Cafe 1", "intro": "Lively neighbourhood spot with sharable plates and chilled playlists.", "price": "₹220"},
        {"id": 6, "name": "Off Campus Cafe 2", "intro": "Low-noise corner ideal for focused work and long reads.", "price": "₹170"},
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


