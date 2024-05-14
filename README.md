# Temperature_Project
Temperature_project that allow user to perform several functions with a data set of temperatures

This project displays a menu dashboard, where a user can repeatedly select one of the seven menu options.
It also creates an array of sensors with their components, as well as an active sensor array. 
Additionally, a recursive_sort method will sort the lists of the user's choice
Define print_filter() prints the list of sensors, and note which ones are currently active.
Define change_filter() enables the user to search for a sensor by the room number, and
adds sensor to the list of filtered sensors.
New_file() method allows the user to load a new dataset file into the program. Also, process_file
in TempDataSet class was made to read data from a specified file path and populate the dataset with 
the temperature samples found in the file.
Implementation to choose and convert units, as well as get_avg_temperature_day_time function in TempDataSet.py. 
Additionally, prints summary statistics.
