# Adding Dictionary to a List of Dictionaries 

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


# Write the function that will allow new countries to be added to the travel_log. 
def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}            # created an empty dictionary
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)
        
   
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



