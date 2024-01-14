from devices_class import AirConditioner, Refrigerator, Television, WashingMachine


class Switch:
    def __init__(self):
        self._device_list = []

    def add_device(self, device_obj):
        if device_obj is not None:
            self._device_list.append(device_obj)
            print("Added device {}".format(device_obj.device_name))
            return True

        print("Device object is None")
        return False

    def get_devices(self):
        return [x.device_name for x in self._device_list]

    def delete_device(self, device_name):
        device_to_be_deleted = None
        for x in self._device_list:
            if x.device_name == device_name:
                device_to_be_deleted = x

        if device_to_be_deleted is None:
            print("Device {} not found".format(device_name))
            return False

        self._device_list.remove(device_to_be_deleted)
        return True

    def modify_device(self, device_name, new_device_obj):
        pass

    def get_device_details(self, device_name):
        for x in self._device_list:
            if x.device_name == device_name:
                return x.get_details()

        print("Device {} not found".format(device_name))
        return None

    def get_device_state(self, device_name):
        for x in self._device_list:
            if x.device_name == device_name:
                return x.get_state()

        print("Device {} not found".format(device_name))
        return None

    def update_device_state(self, device_name, state):
        for x in self._device_list:
            if x.device_name == device_name:
                return x.update_state(state)

        print("Device {} not found".format(device_name))
        return None

    def update_device_parameters(self, device_name, **kwargs):
        for x in self._device_list:
            if x.device_name == device_name:
                return x.update_parameters(**kwargs)

        print("Device {} not found".format(device_name))
        return None


def main():
    # Initialise switch object
    switch_obj = Switch()
    first_refrigerator_name = "refrigerator_1"
    first_television_name = "television_1"
    second_television_name = "television_2"

    # Add refrigerator device
    switch_obj.add_device(Refrigerator(device_name=first_refrigerator_name))

    # Add television device
    switch_obj.add_device(Television(device_name=first_television_name))

    # get list of devices
    print(switch_obj.get_devices())

    # Show refrigerator status
    print(switch_obj.get_device_details(device_name=first_refrigerator_name))

    # Turn ON refrigerator
    switch_obj.update_device_state(device_name=first_refrigerator_name, state=1)

    # Get refrigerator details
    print(switch_obj.get_device_details(device_name=first_refrigerator_name))

    # Set refrigerator temperature to 5
    switch_obj.update_device_parameters(device_name=first_refrigerator_name, temperature=5)

    # Show refrigerator status
    print(switch_obj.get_device_details(device_name=first_refrigerator_name))

    # Turn ON television
    switch_obj.update_device_state(device_name=first_television_name, state=1)

    # Get television details
    print(switch_obj.get_device_details(device_name=first_television_name))

    # Set television channel to 100
    switch_obj.update_device_parameters(device_name=first_television_name, channel=100)

    # Get television details
    print(switch_obj.get_device_details(device_name=first_television_name))

    # Add second television
    switch_obj.add_device(Television(device_name=second_television_name))

    # Get 2nd television details
    print(switch_obj.get_device_details(device_name=second_television_name))

    # Get list of devices
    print(switch_obj.get_devices())

    # get all device's state
    for device_name in switch_obj.get_devices():
        state = switch_obj.get_device_state(device_name=device_name)
        print("State of Device : {} = {}".format(device_name,
                                                 "ON" if state else "OFF"))

    # Turn OFF 1st television
    switch_obj.update_device_state(device_name=first_television_name, state=0)

    # Delete 1st television
    switch_obj.delete_device(device_name=first_television_name)

    # Get list of devices
    print(switch_obj.get_devices())

    # Add washing machine and air conditioner
    washing_machine_name = "washing_machine_1"
    air_conditioner_name = "ac_1"

    switch_obj.add_device(WashingMachine(device_name=washing_machine_name))
    switch_obj.add_device(AirConditioner(device_name=air_conditioner_name))

    # Update washing machine timer to 10 and mode to WASH and turn on washing machine
    print(switch_obj.get_device_details(device_name=washing_machine_name))
    switch_obj.update_device_parameters(device_name=washing_machine_name, timer=10, mode="WASH")
    switch_obj.update_device_state(device_name=washing_machine_name, state=1)
    print(switch_obj.get_device_details(device_name=washing_machine_name))

    # Update AC temperature to 24 and mode to COOL
    print(switch_obj.get_device_details(device_name=air_conditioner_name))
    switch_obj.update_device_parameters(device_name=air_conditioner_name, temperature=24, mode="COOL")
    switch_obj.update_device_state(device_name=air_conditioner_name, state=1)
    print(switch_obj.get_device_details(device_name=air_conditioner_name))

    # get all device's state
    for device_name in switch_obj.get_devices():
        state = switch_obj.get_device_state(device_name=device_name)
        print("State of Device : {} = {}".format(device_name,
                                                 "ON" if state else "OFF"))

    # Turn OFF all devices
    for device_name in switch_obj.get_devices():
        switch_obj.update_device_state(device_name=device_name, state=0)

    # get all device's state
    for device_name in switch_obj.get_devices():
        state = switch_obj.get_device_state(device_name=device_name)
        print("State of Device : {} = {}".format(device_name,
                                                 "ON" if state else "OFF"))


if __name__ == "__main__":
    main()
