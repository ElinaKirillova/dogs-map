'''
Let's find the nearest cafe by given coordinates
'''
import csv
import math

def find_distance_by_coordinates(lat1, lng1, lat2, lng2):
    '''
    function finds the distance between 2 points by coordinates
    '''

    try:
        lat1 = float(lat1)
        lng1 = float(lng1)
        lat2 = float(lat2)
        lng2 = float(lng2)
    except ValueError:
        print("Введены некорректные данные")
        return False

    # Convert degrees to radians. 
    lat1 = math.radians(lat1)
    lng1 = math.radians(lng1)
    lat2 = math.radians(lat2)
    lng2 = math.radians(lng2)
 
    # Calculate delta longitude and latitude. 
    delta_lat = (lat2 - lat1)
    delta_lng = (lng2 - lng1)
 
    return round(6378137 * math.acos(math.cos(lat1) * math.cos(lat2) * math.cos(lng2 - lng1) + math.sin(lat1) * math.sin(lat2)))


def find_nearest_cafe(cafes, lat_user, lng_user):
    try:
        lat_user = float(lat_user)
        lng_user = float(lng_user)
    except ValueError:
        print('Введены некорректные данные')
        return False


    nearest_cafe = {'distance': 0, 'cafe': None}

    for cafe in cafes:
        lat_raw = cafe.latitude
        lng_raw = cafe.longitude

        distance = find_distance_by_coordinates(lat_user, lng_user, lat_raw, lng_raw)

        if not distance:
            return False
    
        # If this cafe is the nearest let's write it to nearest_cafe var
        if (nearest_cafe['distance'] == 0) or (distance < nearest_cafe['distance']):
            nearest_cafe = {'distance': distance, 'cafe': cafe}

    return nearest_cafe

