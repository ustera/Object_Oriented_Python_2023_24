from dataclasses import dataclass
import copy


@dataclass
class Parameters:
    x: float
    y: float
    z: float


@dataclass
class Coordinates:
    near_lower_left: Parameters
    far_lower_left: Parameters
    near_lower_right: Parameters
    far_lower_right: Parameters
    near_upper_left: Parameters
    far_upper_left: Parameters
    near_upper_right: Parameters
    far_upper_right: Parameters


class Item:

    def __init__(self, dimensions: Parameters, coordinates: Coordinates):
        self.dimensions = dimensions
        self.coordinates = coordinates

    def is_intersect(self, other):
        min_x = self.coordinates.near_lower_left.x
        max_x = self.coordinates.near_lower_left.x
        min_y = self.coordinates.near_lower_left.y
        max_y = self.coordinates.near_lower_left.y
        min_z = self.coordinates.near_lower_left.z
        max_z = self.coordinates.near_lower_left.z
        for point in self.coordinates.__dict__.values():
            x, y, z = point.x, point.y, point.z
            if x < min_x:
                min_x = x
            if x > max_x:
                max_x = x
            if y < min_y:
                min_y = y
            if y > max_y:
                max_y = y
            if z < min_z:
                min_z = z
            if z > max_z:
                max_z = z
        vertexes = other.coordinates.__dict__.values()
        for point in vertexes:
            if min_x <= point.x <= max_x and min_y <= point.y <= max_y and min_z <= point.z <= max_z:
                return True
        return False


class Box(Item):
    """ Класс для создания кухонного шкафа """

    def __init__(self, material, dimensions: Parameters, coordinates: Coordinates):
        super().__init__(dimensions, coordinates)
        self.material = material


    def __str__(self):
        return ' Материал мебели: {} \n Координаты: {} \n Габариты: {}'.format(self.material, self.coordinates, self.dimensions)

class Appliances(Item):
    def __init__(self, name, dimensions: Parameters, coordinates: Coordinates):
        super().__init__(dimensions, coordinates)
        self.active = False
        self.name = name

    def __str__(self):
        return ' Техника: {} \n Координаты: {} \n Габариты: {}'.format(self.name, self.coordinates, self.dimensions)

    def activate(self, activation=True):
        if activation:
            self.active = True
        else:
            pass


class Kitchen:
    def __init__(self, dimensions: Parameters, items: list):
        self.dimensions = dimensions
        self.items = items

    def check(self):
        cond1 = False  # проверка на пересечения
        for i in range(len(self.items)):
            for j in range(len(self.items)):
                if i != j:
                    if self.items[i].is_intersect(self.items[j]):
                        cond1 = True

        cond2 = False  # проверка на материал
        for i in range(len(self.items)):
            for j in range(len(self.items)):
                if isinstance(self.items[i], Box) and isinstance(self.items[j], Box):
                    # растягиваем один из шкафов на два метра с каждой стороны
                    item_ = copy.deepcopy(self.items[i])
                    item_.coordinates.near_lower_left = Parameters(item_.coordinates.near_lower_left.x - 2,
                                                                   item_.coordinates.near_lower_left.y - 2,
                                                                   item_.coordinates.near_lower_left.z + 2)
                    item_.coordinates.far_lower_left = Parameters(item_.coordinates.far_lower_left.x - 2,
                                                                  item_.coordinates.far_lower_left.y - 2,
                                                                  item_.coordinates.far_lower_left.z - 2)
                    item_.coordinates.near_lower_right = Parameters(item_.coordinates.near_lower_right.x + 2,
                                                                    item_.coordinates.near_lower_right.y - 2,
                                                                    item_.coordinates.near_lower_right.z + 2)
                    item_.coordinates.far_lower_right = Parameters(item_.coordinates.far_lower_right.x + 2,
                                                                   item_.coordinates.far_lower_right.y - 2,
                                                                   item_.coordinates.far_lower_right.z - 2)
                    item_.coordinates.near_upper_left = Parameters(item_.coordinates.near_upper_left.x - 2,
                                                                   item_.coordinates.near_upper_left.y + 2,
                                                                   item_.coordinates.near_upper_left.z + 2)
                    item_.coordinates.far_upper_left = Parameters(item_.coordinates.far_upper_left.x - 2,
                                                                  item_.coordinates.far_upper_left.y + 2,
                                                                  item_.coordinates.far_upper_left.z - 2)
                    item_.coordinates.near_upper_right = Parameters(item_.coordinates.near_upper_right.x + 2,
                                                                    item_.coordinates.near_upper_right.y + 2,
                                                                    item_.coordinates.near_upper_right.z + 2)
                    item_.coordinates.far_upper_right = Parameters(item_.coordinates.far_upper_right.x + 2,
                                                                   item_.coordinates.far_upper_right.y + 2,
                                                                   item_.coordinates.far_upper_right.z - 2)
                    intersect = item_.is_intersect(self.items[j])
                    if self.items[i].material != self.items[j].material and intersect == True:
                        cond2 = True

        cond3 = False   # грань техники находится на полу
        room_coordinates = Coordinates(near_lower_left=Parameters(0, 0, self.dimensions.z),
                                       far_lower_left=Parameters(0, 0, 0),
                                       near_lower_right=Parameters(self.dimensions.x, self.dimensions.y, 0),
                                       far_lower_right=Parameters(self.dimensions.x, 0, 0),
                                       near_upper_left=Parameters(0, self.dimensions.y, self.dimensions.z),
                                       far_upper_left=Parameters(0, self.dimensions.y, 0),
                                       near_upper_right=Parameters(self.dimensions.x, self.dimensions.y, self.dimensions.z),
                                       far_upper_right=Parameters(self.dimensions.x, 0, self.dimensions.z))

        # на полу - любые четыре точки имеют по y 0
        for i in range(len(self.items)):
            if isinstance(self.items[i], Appliances):
                count = 0
                for coord in self.items[i].coordinates.__dict__.values():
                    if coord.y == 0:
                        count += 1
                if count != 4:
                    cond3 = True

        if cond1:
            print('Мебель или техника пересекается!')
        elif cond2:
            print('Не соответствует условиям взаиморасположения мебели из разных материалов!')
        elif cond3:
            print('Техника находится не на полу!')
        else:
            print('Мебель не пересекается, расстояние соблюдается, техника находится на полу.')

