from backpack import Backpack
from factory import Factory
from flashlight import Flashlight
from rope import Rope


class ConcreteFactory(Factory):
    def create_equipment(self, equipment_type):
        if equipment_type == 'backpack':
            return Backpack()
        elif equipment_type == 'flashlight':
            return Flashlight()
        elif equipment_type == 'rope':
            return Rope()
        else:
            super().create_equipment(equipment_type)
