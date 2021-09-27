import hid


def main():
    try:
        battery = get_battery()
        print("{}%".format(battery))
    except Exception as ex:
        print(ex)


def get_battery():
    device = hid.device()
    device.open(0x1038, 0x12ad)
    device.write([0x06, 0x18])
    battery = device.read(3)[2]
    device.close()
    return battery


if __name__ == "__main__":
    main()
