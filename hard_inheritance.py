from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, color, *args):
        self.__color = color
        self.__sides = self.set_sides(args)
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, *args):
        rgb = []
        for i in args:
            if isinstance(i, int) and 0 <= i <= 255:
                rgb.append(True)
            else:
                rgb.append(False)
        if all(rgb):
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
        else:
            print('Введите целое число от 0 до 255')

    def set_sides(self, *sides):
        faces = []
        if self.__is_valid_sides(*sides):
            if len(sides) == 1 and self.sides_count > 2:
                for side in range(self.sides_count):
                    faces.append(*sides)
            else:
                for side in sides:
                    faces.append(side)
        else:
            for side in range(self.sides_count):
                faces.append(1)
        self.__sides = faces
        return self.__sides

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, *sides):
        count = 0
        for side in sides:
            if isinstance(side, int) and side > 0:
                count += 1
            else:
                return False
        if count == self.sides_count or (count == 1 and self.sides_count > 2):
            return True

    def __len__(self):
        if self.sides_count == 1 and len(self.__sides) == 1:
            return self.__sides
        else:
            return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *args):
        super().__init__(color=color, *args)
        self.__radius = self.set_sides() / 2 * pi

    def get_color(self):
        super().get_color()

    def __is_valid_color(self, *args):
        count = 0
        for side in args:
            if isinstance(side, int) and side > 0:
                count += 1
            else:
                return False
        if count == self.sides_count or (count == 1 and self.sides_count > 2):
            return True

    def set_color(self, r, g, b):
        super().set_color(r=r, g=g, b=b)

    def set_sides(self, *quan):
        super().set_sides(quan)

    def __is_valid_sides(self, *sides):
        count = 0
        for side in sides:
            if isinstance(side, int) and side > 0:
                count += 1
            else:
                return False
        if count == self.sides_count or (count == 1 and self.sides_count > 2):
            return True

    def __len__(self):
        super().__len__()

    def get_square(self):
        return pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3
    __height = sides_count / 2 * pi

    def __init__(self, __color, *args):
        super().__init__(__color, *args)

    def get_color(self):
        super().get_color()

    def __is_valid_color(self, *args):
        count = 0
        for side in args:
            if isinstance(side, int) and side > 0:
                count += 1
            else:
                return False
        if count == self.sides_count or (count == 1 and self.sides_count > 2):
            return True

    def set_color(self, r, g, b):
        super().set_color(r=r, g=g, b=b)

    def set_sides(self, *quan):
        super().set_sides()

    def __is_valid_sides(self, *sides):
        count = 0
        for side in sides:
            if isinstance(side, int) and side > 0:
                count += 1
            else:
                return False
        if count == self.sides_count or (count == 1 and self.sides_count > 2):
            return True

    def __len__(self):
        super().__len__()

    def get_square(self):
        pass


# print(dir(Figure))
# print(dir(Circle))
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
# cube1 = Cube((222, 35, 130), 6)
#
# # Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
# cube1.set_color(300, 70, 15)  # Не изменится
print(circle1.get_color())
# print(cube1.get_color())
#
# # Проверка на изменение сторон:
# cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
# circle1.set_sides(15)  # Изменится
# print(cube1.get_sides())
# print(circle1.get_sides())
#
# # Проверка периметра (круга), это и есть длина:
# print(len(circle1))
#
# # Проверка объёма (куба):
# print(cube1.get_volume())
