#cows_tables_classes.py
# Здесь описаны классы для таблиц "Cow", "Raw_data", "Processed_data"
# Данные классы созданы для упрощения данных в базы
# далее в библиотеке будут описаны функции для быстрой загрузки и выгрузки данных



# class Cow_class: # Класс для основной базы коров
#     """ Cows main table class """

#     def __init__(self, id, rf_id, weight, spray_period, next_spray_time, last_drink_duration):
#         self.id = id
#         self.rf_id = rf_id
#         self.weight = weight
#         self.spray_period = spray_period
#         self.next_spray_time = next_spray_time
#         self.last_drink_duration = last_drink_duration

#     def __repr__(self):
#         return "Cow('{}', '{}', '{}', '{}', '{}', '{}')".format(self.id, self.rf_id, self.weight, self.spray_period, self.next_spray_time, self.last_drink_duration )

class Cow_class: # Класс для основной базы коров
    """ Cows main table class """

    def __init__(self, rf_id, weight, spray_period, next_spray_time, last_drink_duration):
        self.rf_id = rf_id
        self.weight = weight
        self.spray_period = spray_period
        self.next_spray_time = next_spray_time
        self.last_drink_duration = last_drink_duration

    def __repr__(self):
        return "Cow('{}', '{}', '{}', '{}', '{}')".format(self.rf_id, self.weight, self.spray_period, self.next_spray_time, self.last_drink_duration )


class Raw_data_class: # Класс для базы сырых данных
    """ Cows raw_data table class """ 

    def __init__(self, id, cow_id,  weight, timestamp):
        self.id = id
        self.cow_id = cow_id
        self.weight = weight
        self.timestamp = timestamp

    def __repr__(self):
        return "Cow('{}', '{}', '{}')".format(self.id, self.cow_id, self.weight, self.timestamp)

class Processed_data_class: # Класс для базы обработанных данных
    """ Cows raw_data table class """

    def __init__(self, id, cow_id,  weight, timestamp):
        self.id = id
        self.cow_id = cow_id
        self.weight = weight
        self.timestamp = timestamp

    def __repr__(self):
        return "Cow('{}', '{}', '{}')".format(self.id, self.cow_id, self.weight, self.timestamp)