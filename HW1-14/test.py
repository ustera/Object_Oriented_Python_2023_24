from main import Box, Parameters, Coordinates, Appliances, Kitchen

a = Box(material='дуб',
        dimensions=Parameters(1, 1, 1),
        coordinates=Coordinates(Parameters(0, 0, 1), Parameters(0, 0, 0), Parameters(1, 0, 1), Parameters(1, 0, 0),
                                Parameters(0, 1, 1), Parameters(0, 1, 0), Parameters(1, 1, 1), Parameters(1, 1, 0)))

b = Box(material='дуб',
        dimensions=Parameters(1, 1, 1),
        coordinates=Coordinates(Parameters(2, 2, 3), Parameters(2, 2, 2), Parameters(3, 2, 3), Parameters(3, 2, 2),
                                Parameters(2, 3, 3), Parameters(2, 3, 2), Parameters(3, 3, 3), Parameters(3, 3, 2)))

c = Appliances(name='плита',
               dimensions=Parameters(1, 1, 1),
               coordinates=Coordinates(Parameters(5, 0, 6), Parameters(5, 0, 5), Parameters(6, 0, 6),
                                       Parameters(6, 0, 5),
                                       Parameters(5, 1, 6), Parameters(5, 1, 5), Parameters(6, 1, 6),
                                       Parameters(6, 1, 5)))

k = Kitchen(Parameters(10, 10, 10), items=[a, b, c])
print('Test 1')
print('Objects: ')
print(a)
print(b)
print(c)
print('Result:')
k.check()

print('----------')

a = Box(material='дуб',
        dimensions=Parameters(1, 1, 1),
        coordinates=Coordinates(Parameters(0, 0, 1), Parameters(0, 0, 0), Parameters(1, 0, 1), Parameters(1, 0, 0),
                                Parameters(0, 1, 1), Parameters(0, 1, 0), Parameters(1, 1, 1), Parameters(1, 1, 0)))

b = Box(material='сосна',
        dimensions=Parameters(1, 1, 1),
        coordinates=Coordinates(Parameters(2, 2, 3), Parameters(2, 2, 2), Parameters(3, 2, 3), Parameters(3, 2, 2),
                                Parameters(2, 3, 3), Parameters(2, 3, 2), Parameters(3, 3, 3), Parameters(3, 3, 2)))

c = Appliances(name='плита',
               dimensions=Parameters(1, 1, 1),
               coordinates=Coordinates(Parameters(5, 0, 6), Parameters(5, 0, 5), Parameters(6, 0, 6),
                                       Parameters(6, 0, 5),
                                       Parameters(5, 1, 6), Parameters(5, 1, 5), Parameters(6, 1, 6),
                                       Parameters(6, 1, 5)))

k = Kitchen(Parameters(10, 10, 10), items=[a, b, c])
print('Test 2')
print('Objects: ')
print(a)
print(b)
print(c)
print('Result:')
k.check()

print('----------')

a = Box(material='дуб',
        dimensions=Parameters(1, 1, 1),
        coordinates=Coordinates(Parameters(0, 0, 1), Parameters(0, 0, 0), Parameters(1, 0, 1), Parameters(1, 0, 0),
                                Parameters(0, 1, 1), Parameters(0, 1, 0), Parameters(1, 1, 1), Parameters(1, 1, 0)))

b = Box(material='дуб',
        dimensions=Parameters(1, 1, 1),
        coordinates=Coordinates(Parameters(2, 2, 3), Parameters(2, 2, 2), Parameters(3, 2, 3), Parameters(3, 2, 2),
                                Parameters(2, 3, 3), Parameters(2, 3, 2), Parameters(3, 3, 3), Parameters(3, 3, 2)))

c = Appliances(name='плита',
               dimensions=Parameters(1, 1, 1),
               coordinates=Coordinates(Parameters(5, 1, 6), Parameters(5, 1, 5), Parameters(6, 1, 6),
                                       Parameters(6, 1, 5),
                                       Parameters(5, 2, 6), Parameters(5, 2, 5), Parameters(6, 2, 6),
                                       Parameters(6, 2, 5)))

k = Kitchen(Parameters(10, 10, 10), items=[a, b, c])
print('Test 3')
print('Objects: ')
print(a)
print(b)
print(c)
print('Result:')
k.check()

print('----------')

a = Box(material='дуб',
        dimensions=Parameters(1, 1, 1),
        coordinates=Coordinates(Parameters(0, 0, 1), Parameters(0, 0, 0), Parameters(1, 0, 1), Parameters(1, 0, 0),
                                Parameters(0, 1, 1), Parameters(0, 1, 0), Parameters(1, 1, 1), Parameters(1, 1, 0)))

b = Box(material='дуб',
        dimensions=Parameters(1, 1, 1),
        coordinates=Coordinates(Parameters(2, 2, 3), Parameters(2, 2, 2), Parameters(3, 2, 3), Parameters(3, 2, 2),
                                Parameters(2, 3, 3), Parameters(2, 3, 2), Parameters(3, 3, 3), Parameters(3, 3, 2)))

c = Appliances(name='плита',
               dimensions=Parameters(1, 2, 1),
               coordinates=Coordinates(Parameters(5, 0, 6), Parameters(5, 0, 5), Parameters(6, 0, 6),
                                       Parameters(6, 0, 5),
                                       Parameters(5, 2, 6), Parameters(5, 2, 5), Parameters(6, 2, 6),
                                       Parameters(6, 2, 5)))

k = Kitchen(Parameters(10, 10, 10), items=[a, b, c])
print('Test 4')
print('Objects: ')
print(a)
print(b)
print(c)
print('Result:')
k.check()
