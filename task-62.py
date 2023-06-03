class Robot:
    _main_attrs = ["name", "speed"]
    _opt_attrs = []

    def __init__(self, *args):
        attrs = self._main_attrs + self._opt_attrs
        if len(args) < len(attrs):
            raise TypeError("missing argument")
        if len(args) > len(attrs):
            raise TypeError(f"{self.__class__.__name__} takes {len(attrs)} arguments but {len(args)} were given")
        for attr, arg in zip(attrs, args):
            setattr(self, attr, arg)

    def movement(self, time):
        print(f"{self.name} covered {self.speed * time} units of distance in {time} units of time.")


class CaterpillarRobot(Robot):
    _opt_attrs = ["territory"]


class WheelRobot(Robot):
    _opt_attrs = ["car_model"]

