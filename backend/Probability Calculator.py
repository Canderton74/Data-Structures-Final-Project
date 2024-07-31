import geopy
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

geolocator = Nominatim(user_agent="geoapiExercises")

def get_location(city):
    location = geolocator.geocode(city)
    #if location is None:
    #    return avg
    return (location.latitude, location.longitude)

def calculate_distance(city1, city2):
    location1 = get_location(city1)
    location2 = get_location(city2)
    return geodesic(location1, location2).miles

def calculate_accidents_per_hour():
    total_accidents = 246000
    hours_per_year = 365 * 24
    return (total_accidents / hours_per_year) * 0.2 #20% weight

def calculate_highway_value(distance, accidents_per_hour):
    time_traveling = (distance / 75)*0.8  # Assuming 75 mph; 80% weight
    return (time_traveling * accidents_per_hour) / 10

def calculate_city_value(city_count):
    return (city_count / 365) * 10

def calculate_probability(city1_name, city2_name, city1_count, city2_count):
    distance = calculate_distance(city1_name, city2_name)
    accidents_per_hour = calculate_accidents_per_hour()
    highway_value = calculate_highway_value(distance, accidents_per_hour)
    
    city1_value = calculate_city_value(city1_count) * 0.5
    city2_value = calculate_city_value(city2_count) * 0.5
    
    final_value = (city1_value + city2_value) / 2 + highway_value
    return final_value