from engine.Engine import Engine
from battery.Battery import Battery
from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine_type, battery_type):
        self.engine = engine_type
        self.battery = battery_type

    def needs_service(self):
        return self.engine.needs_service and self.battery.needs_service