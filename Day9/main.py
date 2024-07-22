# programming_dictionary  = {
#     "Bug": "Ab error",
#     "Loop":"A code again and again",
#     123 : "Number"
# }

# # print(programming_dictionary[123])
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

# Nesting
capitals = {
    "France": "Paris",
    "Nepal":"Kathmandu",
    "Germany": "Berlin",
}

# Nesting a List in a dictionary

travel_log = {
    "France":["Paris","Lille","Dijon"],
    "Germany":["Berlin","Hamburg","Stuttgart"]
}

# Nesting a dictionary in a dictionary
travel_log = {
    "France":{"cities_visted":["Paris","Lille","Dijon"],"total_visits":12},
    "Germany":{"cities_visited":["Berlin","Hamburg","Stuttgart"],"total_visits":5}
}

# Nesting dictionary in a list
travel_log = [
    {
        "country":"France",
        "cities_visted":["Paris","Lille","Dijon"],"total_visits":12
        },
    {
        "country":"Germany",
        "cities_visited":["Berlin","Hamburg","Stuttgart"],"total_visits":5
        },
]