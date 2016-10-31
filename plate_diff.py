# Dictionary to give the value of any alpha plate character
from string import ascii_uppercase
from collections import OrderedDict
plates_alpha_value = OrderedDict((character, index) for index, character in enumerate(ascii_uppercase, 1))

def vehicleCount(latest_plate, older_plate):
    diff_alpha_second = plates_alpha_value[latest_plate[1]] - plates_alpha_value[older_plate[1]]
    if diff_alpha_second >= 1:
        num_vehicles_iter1 = (diff_alpha_second - 1) * 676000
        num_vehicles_older_plate = ((26 - plates_alpha_value[older_plate[2]]) * 26000) + ((26 - plates_alpha_value[older_plate[-1]]) * 1000) + (1000 - int(older_plate[-4:6]))
        num_vehicles_latest_plate = ((plates_alpha_value[latest_plate[2]] - 1) * 26000) + ((plates_alpha_value[latest_plate[-1]] - 1) * 1000) + (int(latest_plate[-4:6]))
        num_vehicles = num_vehicles_older_plate + num_vehicles_latest_plate + num_vehicles_iter1
    else:
        diff_alpha_third = plates_alpha_value[latest_plate[2]] - plates_alpha_value[older_plate[2]]
        num_vehicles_iter2 = (diff_alpha_third - 1) * 26000
        num_vehicles_older_plate = ((26 - plates_alpha_value[older_plate[-1]]) * 1000) + (1000 - int(older_plate[-4:6]))
        num_vehicles_latest_plate = ((plates_alpha_value[latest_plate[-1]] - 1) * 1000) + (int(latest_plate[-4:6]))
        num_vehicles = num_vehicles_older_plate + num_vehicles_latest_plate + num_vehicles_iter2

    return num_vehicles-1


latest_plate1 = raw_input("Enter the latest place for which number you want ,eg: 'KAC000A' " + " : ")
older_plate2 = raw_input("Enter the older plate, eg: 'KAA000A' " + " : ")
print vehicleCount(latest_plate1, older_plate2)
