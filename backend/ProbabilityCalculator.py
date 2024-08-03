import geopy
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

geolocator = Nominatim(user_agent="distanceCalculation")

def get_location(city):
    location = geolocator.geocode(city, timeout=10)
    #if location is None:
    #    return avg
    return (location.latitude, location.longitude)

def calculate_distance(city1, city2):
    location1 = get_location(city1)
    location2 = get_location(city2)
    return geodesic(location1, location2).miles

def calculate_accidents_per_hour():
    total_accidents = 246633
    hours_per_year = 365 * 24
    return (total_accidents / hours_per_year) 

def calculate_highway_value(distance, accidents_per_hour):
    time_traveling = (distance / 75)  # Assuming 75 mph; 
    return (time_traveling * accidents_per_hour)/(distance*(1-.25)) # Assuming you have to be within 10% of your distance to an accident to be delayed 

def calculate_city_value(city_count):
    return (city_count / (365*24)) *3#assuming 3 hours on the highway in each city

def calculate_probability(city1_name, city2_name, city1_count, city2_count):
    distance = calculate_distance(city1_name, city2_name)
    accidents_per_hour = calculate_accidents_per_hour()
    highway_value = calculate_highway_value(distance, accidents_per_hour)
    
    city1_value = calculate_city_value(city1_count) 
    city2_value = calculate_city_value(city2_count) 
    
    final_value = (city1_value + city2_value) + highway_value
    return final_value, distance