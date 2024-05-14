docstring = """
    The purpose of this class is to create a dataset that stores temperature
    and is able to be implemented into the main program.
"""

import math
class TempDataSet:
    num_dataset_objects = 0

    def __init__(self):
        self.data_set = None
        self._name = "Unnamed"
        TempDataSet.num_dataset_objects += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) < 3 or len(value) > 20:
            raise ValueError("Name length must be between 3 and 20 characters.")
        self._name = value

    def process_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                self.data_set = []
                for line in file:
                    data = line.strip().split(',')
                    if len(data) >= 4 and data[3] == "TEMP":
                        day = int(data[0])
                        time = int(math.floor(float(data[1]) * 24))
                        sensor = int(data[2])
                        temp = float(data[4])
                        self.data_set.append((day, time, sensor, temp))
            return True
        except FileNotFoundError:
            return False

    def get_summary_statistics(self, active_sensors):
        if not self.data_set:
            return None

        active_temperatures = [temp for temp in self.data_set if temp[1] in active_sensors]

        if not active_temperatures:
            return None

        min_temp = min(active_temperatures, key=lambda x: x[2])[2]
        max_temp = max(active_temperatures, key=lambda x: x[2])[2]
        avg_temp = sum(temp[2] for temp in active_temperatures) / len(active_temperatures)

        return min_temp, max_temp, avg_temp

    def get_avg_temperature_day_time(self, active_sensors, day, time):

        if self.data_set is None:
            return None

        relevant_temps = [sample[3] for sample in self.data_set
                          if sample[0] == day and sample[1] == time and sample[2] in active_sensors]

        if relevant_temps:
            return sum(relevant_temps) / len(relevant_temps)
        else:
            return None

    def get_num_temps(self, active_sensors, lower_bound, upper_bound):
        if self.data_set is None:
            return None
        return 0

    def get_loaded_temps(self):
        if self.data_set is not None:
            return len(self.data_set)
        else:
            return None

    @classmethod
    def get_num_objects(cls):
        return cls.num_dataset_objects
