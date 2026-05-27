from faker import Faker


class Utils:
    faker_en = Faker("en_US")
    faker_ru = Faker("ru_RU")


utils = Utils()
