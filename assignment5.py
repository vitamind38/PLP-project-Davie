class Smartphone:
    def __init__(self, brand, model, battery_capacity):
        self.brand = brand
        self.model = model
        self.battery_capacity = battery_capacity  # in mAh
        self.battery_level = 100 

    def make_call(self, number):
        return f"Calling {number} from {self.brand} {self.model}..."

    def charge(self, amount):
        self.battery_level = min(100, self.battery_level + amount)
        return f"Battery charged to {self.battery_level}%."

    def use_app(self, app_name, usage_time):
        drain = usage_time * 2  
        self.battery_level = max(0, self.battery_level - drain)
        return f"Used {app_name} for {usage_time} mins. Battery at {self.battery_level}%."

class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery_capacity, cooling_system):
        super().__init__(brand, model, battery_capacity)
        self.cooling_system = cooling_system

    def use_app(self, app_name, usage_time):
        if app_name.lower() == "game":
            drain = usage_time * 5  # gaming drains faster
        else:
            drain = usage_time * 2
        self.battery_level = max(0, self.battery_level - drain)
        return f"Played {app_name} for {usage_time} mins. Cooling system: {self.cooling_system}. Battery at {self.battery_level}%."

phone1 = Smartphone("Samsung", "S22", 4500)
phone2 = GamingPhone("ZTE Nubia", "Redmagic 10 pro", 7050, "Liquid Cooling")

print(phone1.make_call("123-456-789"))
print(phone1.use_app("YouTube", 10))
print(phone1.charge(20))

print(phone2.use_app("Game", 30))
print(phone2.charge(15))
