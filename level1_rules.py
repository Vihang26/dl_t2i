import map
import properties
import random

# association rules using description logics

# level 1: article + property + object
# level 2: article + property + object + preposition + object
# level 3: article + property + object + preposition + article + property + object

art = ''

with open("level1.txt", "w") as level1_file:

    def dl_level1(property, property_map):

        for _ in property_map:
            for obj in _:
                prop = random.choice(property[:6])
                if prop[0] in ['a', 'e', 'i', 'o', 'u']:
                    art = 'an'
                else:
                    art = 'a'

                level1_file.write(art + " " + prop + " " + obj)
                level1_file.write("\n")

    dl_level1(properties.colors, map.objs_with_color)
    dl_level1(properties.shapes, map.objs_with_shape)
    dl_level1(properties.sizes, map.objs_with_size)
    dl_level1(properties.colors, map.objs_with_color)
    dl_level1(properties.food_properties, map.objs_with_food_properties)
    dl_level1(properties.colors, map.objs_with_color)
    dl_level1(properties.emotions, map.objs_with_emotions)

    for _ in map.objs_with_numbers:
        for obj in _:
            number = random.choice(properties.numbers)
            level1_file.write(number + " " + obj)
            level1_file.write("\n")
