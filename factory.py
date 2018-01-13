from abc import abstractmethod


class Factory:
    @abstractmethod
    def create_equipment(self, equipment_type):
        raise NotImplementedError()
