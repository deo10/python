# create function route_infor that will take dict (one param)
# if dict has key distance and it's value integer return "Distance to your distination is <distance>"
# else if dict have keys speed and time return "Distance to your destination is <speed> * <time>"
# else retunr "No distance info is available"


def route_info(dict):
    if ('distance' in dict) and (type(dict['distance']) is int):
        return f"Distance to your distination is {dict['distance']}"
    if ('speed' in dict and 'time' in dict) and (type(dict['speed']) is int and type(dict['time']) is int):
        return f"Distance to your destination is {dict['speed'] * dict['time']}"
    return "No distance info is available"



print(route_info({'distance': 200}))
#"Distance to your distination is <distance>"
print(route_info({'distance': 200.10, 'speed': 201, 'time': 120}))
#"Distance to your destination is <speed> * <time>"
print(route_info({'distance': 'abc'}))
#"No distance info is available"


#---with isinstance check instead of type

def route_info(route_data):
    if 'distance' in route_data and isinstance(route_data['distance'], int):
        return f"Distance to your distination is {route_data['distance']}"
    if 'speed' in route_data and 'time' in route_data and isinstance(route_data['speed'], int) and isinstance(route_data['time'], int):
        return f"Distance to your destination is {route_data['speed'] * route_data['time']}"
    return "No distance info is available"



print(route_info({'distance': 200}))
#"Distance to your distination is <distance>"
print(route_info({'distance': 200.1, 'speed': 201, 'time': 120}))
#"Distance to your destination is <speed> * <time>"
print(route_info({'distance': 'abc'}))
#"No distance info is available"