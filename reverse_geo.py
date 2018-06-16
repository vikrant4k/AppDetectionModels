import requests
import google
from pprint import pprint
from geopy import distance
import pandas

KEY = "AIzaSyBh5n3r3q5mb4o7dC3ZU7acUlvaBcDROrQ"
IN_VEHICLE = 0
ON_BICYCLE = 1
ON_FOOT = 2
RUNNING = 8
STILL = 3
TILTING = 5
UNKNOWN = 4
WALKING = 7
URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={},{}&rankby=distance&type={}&key={}"
LOC_TYPE = ["accounting", "airport", "amusement_park", "aquarium", "art_gallery", "atm", "bakery", "bank", "bar",
            "beauty_salon", "bicycle_store", "book_store", "bowling_alley", "bus_station", "cafe", "campground",
            "car_dealer", "car_rental", "car_repair", "car_wash", "casino", "cemetery", "church", "city_hall",
            "clothing_store", "convenience_store", "courthouse", "dentist", "department_store", "doctor", "electrician",
            "electronics_store", "embassy", "fire_station", "florist", "funeral_home", "furniture_store", "gas_station",
            "gym", "hair_care", "hardware_store", "hindu_temple", "home_goods_store", "hospital", "insurance_agency",
            "jewelry_store", "laundry", "lawyer", "library", "liquor_store", "local_government_office", "locksmith",
            "lodging", "meal_delivery", "meal_takeaway", "mosque", "movie_rental", "movie_theater", "moving_company",
            "museum", "night_club", "painter", "park", "parking", "pet_store", "pharmacy", "physiotherapist", "plumber",
            "police", "post_office", "real_estate_agency", "restaurant", "roofing_contractor", "rv_park", "school",
            "shoe_store", "shopping_mall", "spa", "stadium", "storage", "store", "subway_station", "supermarket",
            "synagogue", "taxi_stand", "train_station", "transit_station", "travel_agency", "veterinary_care", "zoo"]


def get_respone_google(lat, long):
    to_call = URL.format(lat, long, ",".join(LOC_TYPE), KEY)
    data_raw = requests.get(to_call)
    data_list = data_raw.json()["results"]

    least_coords = ()
    current_least = 1000
    for loc in data_list:
        loc_lat = loc["geometry"]["location"]["lat"]
        loc_long = loc["geometry"]["location"]["lng"]
        loc_type = loc["types"]
        distnce = find_distance((lat, lng), (loc_lat, loc_long))
        if current_least > distnce:
            current_least = distnce
            least_coords = (loc_lat, loc_long)

    return current_least, least_coords


# TODO top 5 location, app used with time

def find_distance(coords_1, coords_2):
    return distance.vincenty(coords_1, coords_2).meters


def find_n_update_location(loc, lat, lng):
    _lat = float(lat)
    _lng = float(lng)
    lat_lng_list = list()
    for val in loc:
        lt = float(val[0])
        lg = float(val[1])

        if round(lt, 3) == round(_lat, 3):
            if round(lg, 3) == round(_lng, 3):
                pass
        else:
            lat_lng_list.append((round(_lat, 3), round(_lng, 3)))

    else:
        lat_lng_list.append((round(_lat, 3), round(_lng, 3)))

    return lat_lng_list


app_rank = dict()


def rank_application(app_name, lat, lng, time, act):
    if app_name not in app_rank:
        app_rank[app_name] = dict()
        # app_rank[app_name]["location"] = find_n_update_location([], lat, lng)
        app_rank[app_name]["data"] = [(time, act, lat, lng)]
        app_rank[app_name]["count"] = 0

    else:
        # app_rank[app_name]["location"] = find_n_update_location(app_rank[app_name]["location"], lat, lng)
        app_rank[app_name]["data"].append((time, act, lat, lng))
        app_rank[app_name]["count"] = app_rank[app_name]["count"] + 1


def process_rank_location():

    list_uniq_location = list()
    list_time_quarter = list()
    for app,app_data in app_rank.iteritems():

        print(app,app_data)
        for lc in app_data["data"]:
            print (lc)
            if list_uniq_location:
                for pos,loc in enumerate(list_uniq_location,0):
                    dist = find_distance(loc["coord"],(lc[2],lc[3]))
                    if dist < 15:
                        list_uniq_location[pos]["count"]=list_uniq_location[pos]["count"]+1
                        break
                    else:
                        list_uniq_location.append({"coord":(lc[2],lc[3]),"count":0})

            else:
                print
                list_uniq_location.append({"coord":(lc[2],lc[3]),"count":0})

        app_rank[app]["uniq_location"] = list_uniq_location


def process_top_locations(dat):

    dict_loc = dict()
    list_all_location_occurance = list()
    for k, v in dat.iteritems():
        lat = v["lat"]
        lng = v["lng"]
        if list_all_location_occurance:
            for pos, loc in enumerate(list_all_location_occurance, 0):
                dist = find_distance(loc["coord"], (lat, lng))
                if dist > 30:
                    list_all_location_occurance.append({"coord": (lat, lng), "count": 0})
                else:
                    list_all_location_occurance[pos]["count"] = list_all_location_occurance[pos]["count"] + 1
                    break
        else:
            print
            list_all_location_occurance.append({"coord": (lat, lng), "count": 0})

    first = None
    first_val = None
    second = None
    second_val = None

    print (dict_loc)

    for val in list_all_location_occurance:
        number =  val["count"]#,val["coord"]
        number_val = val["coord"]
        if first is None:
            first = number
            first_val = number_val
        elif number > first:
            second = first
            second_val = first_val
            first = number
            first_val = number_val
        else:
            if second is None:
                second = number
                second_val = number_val
            elif number > second:
                second = number
                second_val = number_val

    print(first,second)
    print(first_val,second_val)


def read_file_user(user_file_name):
    _data_dict = dict()
    file_datat = open(user_file_name, "r").readlines()
    for line in file_datat:
        dat = line.rstrip().split(",")
        _time = dat[0]
        _app_name = dat[1]
        _lat = dat[3]
        _lng = dat[4]
        _type_act = dat[2]
        # if float(_lat) and float(_lng):
        _data_dict[_time] = {"lat": _lat, "lng": _lng, "act_type": _type_act, "app_name": _app_name}

    return _data_dict


def process_data(data_dict):
    for k, v in data_dict.iteritems():
        lat = v["lat"]
        lng = v["lng"]
        act = v["act_type"]
        app_name = v["app_name"]
        rank_application(app_name, lat, lng, k, act)
        print(lat, lng, act)
        # get_respon?e_google(lat, lng)


lat = 52.3732353
lng = 4.8340443

# print find_near_same_location((lat,lng),(52.37323,4.834023))
data = read_file_user("/home/vik1/Downloads/data/vikrant/11-Jun-2018.csv")
# pprint(data)
# find_top_location(data)
# process_data(data)
# print app_rank
# process_rank_location()
process_top_locations(data)
# resp = get_respone_google(lat,lng)
# process_data(resp,(lat,lng))