# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting a List in a Dictionary
travel_log = {
    "France": ["A", "B", "C"],
    "Germany": ["A", "B", "C"]
}

# Nesting Dictionary in a Dictionary
travel_log = {
    "France": { 
        "cities_visited": ["A", "B", "C"], 
        "total_visits": 5, 
        },
    "Germany": { 
        "cities_visited": ["A", "B", "C"] , 
        "total_visits":6 
        },
}

# Nesting Dictionary in a List
travel_log = [
  {
      "country": "France", 
      "cities_visited": ["A", "B", "C"], 
      "total_visits": 5, },
  {
      "country": "Germany", 
      "cities_visited": ["A", "B", "C"] , 
      "total_visits":6 
    },
]