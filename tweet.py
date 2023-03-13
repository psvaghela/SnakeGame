from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")
ladd1 = "texarkana"
print("Location address:",ladd1)
location = geolocator.geocode(ladd1)
print("Latitude and Longitude of the said address:")
print((location.latitude, location.longitude))