class GeometricFigure:
    def __init__(self, area, perimeter) -> None:
        self.area = area
        self.perimeter = perimeter

    def info(self):
        print(f"площадь - {self.area}, периметр - {self.perimeter}")


square=GeometricFigure(4, 8)
square.info()
