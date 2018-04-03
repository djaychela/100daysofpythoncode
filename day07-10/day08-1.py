cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps():
    """return a comma separated string of jeep models (original order)"""
    return ', '.join(cars['Jeep'])


def get_first_model_each_manufacturer():
    """return a list of matching models (original ordering)"""
    first_models = []
    for maker in cars.keys():
        first_models.append(cars[maker][0])
    return first_models


def get_all_matching_models(grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    match_list = []
    for maker in cars.keys():
        for model in cars[maker]:
            if grep.lower() in model.lower():
                match_list.append(model)
    match_list.sort()
    return match_list


def sort_car_models():
    """sort the car models (values) and return the resulting cars dict"""
    for maker in cars.keys():
        model_list = cars[maker]
        model_list.sort()
        cars[maker]=model_list
    return cars


# print(get_all_jeeps())
# print(get_first_model_each_manufacturer())
print(get_all_matching_models('CO'))
# print(sort_car_models())
