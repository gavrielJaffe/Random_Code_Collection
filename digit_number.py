import math

def distance_on_earth(lon1, lat1, lon2, lat2):
    # Convert latitude and longitude to radians
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])

    # Haversine formula
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r * 1000 # Convert kilometers to meters

def calculate_distance(lon1, lat1, lon2, lat2):
    R = 6371  # radius of the Earth in kilometers
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])  # convert to radians

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    distance = R * c * 1000  # convert to meters
    return distance

def main():
    lat1 = 31.84773061844485
    lon1 = 34.68503878875027

    lat2 = 31.847699286584252
    lon2 = 34.685039459302516

    distance = distance_on_earth(lon1, lat1, lon2, lat2)
    # distance = calculate_distance(34.68503878875027, 31.84773061844485, 34.685039459302516, 31.847699286584252)
    print('distance', distance)

if __name__ == '__main__':
    main()
