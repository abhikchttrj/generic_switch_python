from abc import ABC, abstractmethod


class Devices(ABC):
    def __init__(self, device_name, device_type):
        self._state = 0  # 0 for OFF and 1 for ON
        self.device_name = device_name
        self.device_type = device_type

    def update_state(self, state):
        if self._state == state:
            print("State of {} is already : {}".format(self.device_name, "ON" if state else "OFF"))
            return False

        self._state = state
        return True

    def get_state(self):
        return self._state

    @abstractmethod
    def update_parameters(self, **kwargs):
        pass

    @abstractmethod
    def get_details(self):
        pass


class Refrigerator(Devices):
    def __init__(self, device_name):
        super(Refrigerator, self).__init__(device_name=device_name, device_type="refrigerator")
        self._temperature = 0
        self._mode = "AUTO"

    def update_parameters(self, **kwargs):
        for attributes in ["temperature", "mode"]:
            if kwargs.get(attributes):
                setattr(self, "_{}".format(attributes), kwargs[attributes])
                print("Updated {} to {}".format(attributes, getattr(self, "_{}".format(attributes))))

    def get_details(self):
        return self.__dict__


class Television(Devices):
    def __init__(self, device_name):
        super(Television, self).__init__(device_name=device_name, device_type="television")
        self._channel = 0
        self._mode = "AUTO"

    def update_parameters(self, **kwargs):
        for attributes in ["channel", "mode"]:
            if kwargs.get(attributes):
                setattr(self, "_{}".format(attributes), kwargs[attributes])
                print("Updated {} to {}".format(attributes, getattr(self, "_{}".format(attributes))))

    def get_details(self):
        return self.__dict__


class AirConditioner(Devices):
    def __init__(self, device_name):
        super(AirConditioner, self).__init__(device_name=device_name, device_type="air_conditioner")
        self._temperature = 0
        self._mode = "AUTO"

    def update_parameters(self, **kwargs):
        for attributes in ["temperature", "mode"]:
            if kwargs.get(attributes):
                setattr(self, "_{}".format(attributes), kwargs[attributes])
                print("Updated {} to {}".format(attributes, getattr(self, "_{}".format(attributes))))

    def get_details(self):
        return self.__dict__


class WashingMachine(Devices):
    def __init__(self, device_name):
        super(WashingMachine, self).__init__(device_name=device_name, device_type="washing_machine")
        self._timer = 0
        self._mode = "AUTO"

    def update_parameters(self, **kwargs):
        for attributes in ["timer", "mode"]:
            if kwargs.get(attributes):
                setattr(self, "_{}".format(attributes), kwargs[attributes])
                print("Updated {} to {}".format(attributes, getattr(self, "_{}".format(attributes))))

    def get_details(self):
        return self.__dict__
