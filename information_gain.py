
def get_information_gain(entrophy_values, class_entrophy):
    info = dict()
    for attribute, entrophy in entrophy_values.items():
        column_elements = entrophy.pop("count")
        for k, v in entrophy.items():
            if attribute not in info:
                info[attribute] = 0
            info[attribute] += v["count"] / column_elements * v["entrophy"]
    # INFORMATION GAIN
    gain = dict()
    for k, v in info.items():
        gain[k] = class_entrophy["entrophy"] - v
    return gain