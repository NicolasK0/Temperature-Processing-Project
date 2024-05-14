from TempDataSet import TempDataSet

docstring = """ CalculateStatistics
    Submitted by Nicolas Kousoulas
    Submitted:  3/27/24
     This project displays a menu dashboard, where a user can repeatedly select one of the seven menu options
    It also creates an array of sensors with their components,
    as well as an active sensor array. 
    Additionally, a recursive_sort method will sort the lists of the user's choice
    Define print_filter() prints the list of sensors, and note which ones are currently active.
    Define change_filter() enables the user to search for a sensor by the room number, and
    adds sensor to the list of filtered sensors.
    Added new_file() method, which allows the user to load a new dataset file into the program. Also, process_file
    in TempDataSet class was made to read data from a specified file path and populate the dataset with 
    the temperature samples found in the file.
    Now, includes function to choose and convert units, as well as new implementation
    for get_avg_temperature_day_time function in TempDataSet.py. Additionally, it now also
    prints the summary statistics.
"""

current_unit = 0

UNITS = {
    0: ("Celsius", "C"),
    1: ("Fahrenheit", "F"),
    2: ("Kelvin", "K"),
}

def convert_units(temp, from_unit, to_unit):
    if from_unit == 'C':
        if to_unit == 'F':
            return (temp * 9/5) + 32
        elif to_unit == 'K':
            return temp + 273.15
        elif to_unit == 'R':
            return (temp + 273.15) * 9/5
        else:
            return temp
    elif from_unit == 'F':
        if to_unit == 'C':
            return (temp - 32) * 5/9
        elif to_unit == 'K':
            return (temp + 459.67) * 5/9
        elif to_unit == 'R':
            return temp + 459.67
        else:
            return temp
    elif from_unit == 'K':
        if to_unit == 'C':
            return temp - 273.15
        elif to_unit == 'F':
            return temp * 9/5 - 459.67
        elif to_unit == 'R':
            return temp * 9/5
        else:
            return temp
    elif from_unit == 'R':
        if to_unit == 'C':
            return (temp - 491.67) * 5/9
        elif to_unit == 'F':
            return temp - 459.67
        elif to_unit == 'K':
            return temp * 5/9
        else:
            return temp
    else:
        return temp
def print_filter(sensor_list, active_sensors):
    sorted_list = recursive_sort(sensor_list)
    for sensor in sorted_list:
        if sensor[2] in active_sensors:
            print(f'{sensor[0]}: {sensor[1]} [ACTIVE]')
        else:
            print(f'{sensor[0]}: {sensor[1]}')


def change_filter(sensor_list, active_sensors):
    print("Called the change_filter() function.")
    sensors = {sensor[0]: sensor[2] for sensor in sensor_list}
    print(f'sensor_dict = {sensors}')
    user_input = ''
    filter_list = []

    while user_input != 'x':
        print("Printing filtered sensor list.")
        print_filter(sensor_list, active_sensors)
        user_input = input("\nType the sensor number to toggle (e.g. 4201) or x to end: ")
        if (user_input == 'x'):
            break
        elif user_input in sensors:
            sensor_number = sensors[user_input]
            print(f'Room {user_input} found {sensor_number} in list.')
            if sensor_number in active_sensors:
                # remove from active sensors
                active_sensors.remove(sensor_number)
            else:
                # add to active sensors
                active_sensors.append(sensor_number)
            if sensor_number in filter_list:
                filter_list.remove(sensor_number)
            else:
                filter_list.append(sensor_number)
            print(f'filter list = {filter_list}')

        else:
            print(f'Invalid sensor {user_input}. Please try again')



def test_sensor_setup(sensor_list, active_sensors):
    print("\nTesting sensor_list length:")
    if len(sensor_list) == 6:
        print("Pass")
    else:
        print("Fail")

    print("Testing sensor_list content:")
    rooms_list = [i[0] for i in sensor_list]
    descriptions_list = [i[1] for i in sensor_list]
    if "4213" not in rooms_list or "Out" not in rooms_list:
        print("Fail - something is wrong with the room numbers")
    elif "Foundations Lab" not in descriptions_list:
        print("Fail - something is wrong with room descriptions")
    else:
        print("Pass")

    print("Testing active_sensors length:")
    if len(active_sensors) == 6:
        print("Pass")
    else:
        print("Fail")

    print("Testing active_sensors content:")
    if sum(active_sensors) == 20:
        print("Pass")
    else:
        print("Fail")


def print_header():
    print("STEM Center Temperature Project")
    print("Nick K")


def print_menu():
    print("Main Menu\n---------")
    print(f'1 - Process a new data file\n2 - Choose units\n3 - Edit room filter\n'
          f'4 - Show summary statistics\n5 - Show temperature by date and time\n'
          f'6 - Show histogram of temperatures\n7 - Quit')


def new_file(dataset):
    file_path = input("Please enter the path and file name of the new dataset: ")

    if dataset.process_file(file_path):
        print(f"Loaded {dataset.get_loaded_temps()} samples.")

        # Ask for a name for the dataset
        while True:
            name = input("Please enter a name for the dataset (3-20 characters): ")
            try:
                dataset.name = name
                break
            except ValueError as e:
                print(e)
    else:
        print("Unable to load the file.")
        return


def choose_units():
    global current_unit

    print("\nChoose the unit you would like to display temperatures in:")
    for key, value in UNITS.items():
        print(f"{key}: {value[0]}")


    current_unit = int(input("Enter the number corresponding to your choice: "))

    while current_unit not in UNITS:
        print("Invalid choice. Please enter a valid number.")
        current_unit = int(input("Enter the number corresponding to your choice: "))
    print("Current units in", UNITS[current_unit][0])  # Print the current units

def print_temp_by_day_time(dataset, active_sensors):
    print("Temperature Printed")


def print_histogram(dataset, active_sensors):
    print("Histogram printed")


def recursive_sort(list_to_sort, key=0):
    list_to_sort_copy = list_to_sort[:]

    count = len(list_to_sort_copy)

    if count <= 1:
        return list_to_sort_copy

    for i in range(count - 1):
        if list_to_sort_copy[i][key] > list_to_sort_copy[i + 1][key]:
            temp = list_to_sort_copy[i]
            list_to_sort_copy[i] = list_to_sort_copy[i + 1]
            list_to_sort_copy[i + 1] = temp

    sorted_sublist = recursive_sort(list_to_sort_copy[:-1], key)
    last_element = list_to_sort_copy[-1]

    sorted_sublist.append(last_element)

    return sorted_sublist



def print_summary_statistics(dataset, active_sensors):
    if dataset is None:
        print("Please load data file.")
        return

    summary_stats = dataset.get_summary_statistics(active_sensors)
    if summary_stats is None:
        print("No summary statistics available.")
        return

    min_temp, max_temp, avg_temp = summary_stats

    # Convert temperatures to the current unit
    unit_name, unit_symbol = UNITS[current_unit]
    min_temp = convert_units(min_temp, 'C', unit_symbol)
    max_temp = convert_units(max_temp, 'C', unit_symbol)
    avg_temp = convert_units(avg_temp, 'C', unit_symbol)

    print(f"Summary statistics for {dataset.name}")
    print(f"Minimum Temperature: {min_temp:.2f} {unit_symbol}")
    print(f"Maximum Temperature: {max_temp:.2f} {unit_symbol}")
    print(f"Average Temperature: {avg_temp:.2f} {unit_symbol}")


def main():

    the_sensor_list = [("4213", "STEM Center", 0), ("4201", "Foundations Lab", 1),
                       ("4204", "CS Lab", 2), ("4218", "Workshop Room", 3), ("4205", "Tilted Room", 4),
                       ("Out", "Outside", 10)]

    the_active_sensors = [sensor[2] for sensor in the_sensor_list]

    # Provides a sorted list of sensors by room number.
    sorted_by_room = recursive_sort(the_sensor_list)
    print(f"sensors by room number {sorted_by_room}")
    print(f"active_list is {the_active_sensors}\n")

    # Create an object of type TempDataSet
    # [Note: Definition of TempDataSet should be in a separate .py file]
    current_set = TempDataSet()

    print_header()

    option = 0
    while (option != 7):
        print_menu()
        print(current_set.get_avg_temperature_day_time(the_active_sensors, 5, 7))
        try:
            option = int(input("Enter [1-7] for the menu option you would like to select:\n"))
        except ValueError:
            print("Please enter a valid number")
            continue
        if (option == 1):
            new_file(current_set)
            continue
        elif option == 2:
            choose_units()
            continue
        elif option == 3:
            change_filter(the_sensor_list, the_active_sensors)
            continue
        elif option == 4:
            print_summary_statistics(current_set, the_active_sensors)
            continue
        elif option == 5:
            print_temp_by_day_time(None, None)
            continue
        elif option == 6:
            print_histogram(None, None)
            continue
        elif option == 7:
            continue
        else:
            print("Invalid Number")
            continue
    print("Thank you for using the STEM Center Temperature Project")




if __name__ == '__main__':
    main()
