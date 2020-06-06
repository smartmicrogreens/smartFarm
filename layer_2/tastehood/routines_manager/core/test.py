# Dependencies
from routines_manager.core.constants import *
from routines_manager.core.iot_device import *

# Routines manager
from routines_manager.routines.resource_rountines import switch_status
def test_routines_manager():
    device = IotDevice('myDevice', 'This is my device', TEST_DEVICE)
    switch_status(LIGHT, SHELF_2, OFF, device)

def main():
    return

if __name__ == "__main__":
    main()