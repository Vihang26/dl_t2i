import objects

'''
properties: colors, shapes, sizes, food_properties, emotions, numbers, quantity

objects: body_part, planet, constellation, star, other_bodies, party, holiday, 
game, concert, vegetable, fruit, beverage, dish, furniture, terrain, building, 
monument, season, stationery, vehicle, weather
'''

# mapping properties with objects:
'''
colors: body_part, planet, constellation, star, other_bodies, vegetable, fruit, beverage, dish, furniture,
        terrain, building, monument, season, stationery, vehicle  
shapes: planet, constellation, other_bodies, vegetable, fruit, dish, furniture, terrain, building, monument, stationery
sizes: body_part, planet, constellation, star, other_bodies, party, holiday, game, concert, vegetable, fruit, 
        beverage, dish, furniture, terrain, building, monument, stationery, vehicle
food_properties: vegetable, fruit, beverage, dish
emotions: party, holiday, game, concert, season, weather
numbers: body_part, planet, constellation, star, other_bodies, game, concert, vegetable, fruit,
        beverage, dish, furniture, terrain, building, monument, stationery, vehicle
quantity: beverage, dish 

'''

objs = [
    objects.planet, 
    objects.star, 
    objects.party, 
    objects.holiday, 
    objects.game, 
    objects.concert, 
    objects.vegetable, 
    objects.fruit, 
    objects.beverage, 
    objects.dish, 
    objects.furniture, 
    objects.terrain, 
    objects.building, 
    objects.monument, 
    objects.season, 
    objects.stationery, 
    objects.vehicle, 
    objects.weather
]

objs_with_color = [
    objects.planet,
    objects.star, 
    objects.vegetable, 
    objects.fruit, 
    objects.beverage, 
    objects.dish, 
    objects.furniture, 
    objects.terrain, 
    objects.building, 
    objects.monument, 
    objects.season, 
    objects.stationery, 
    objects.vehicle  
]

objs_with_shape = [
    objects.planet, 
    objects.vegetable, 
    objects.fruit, 
    objects.dish, 
    objects.furniture, 
    objects.terrain, 
    objects.building, 
    objects.monument, 
    objects.stationery
]

objs_with_size = [
    objects.planet,
    objects.star,
    objects.party, 
    objects.holiday, 
    objects.game, 
    objects.concert, 
    objects.vegetable, 
    objects.fruit, 
    objects.beverage, 
    objects.dish, 
    objects.furniture, 
    objects.terrain, 
    objects.building, 
    objects.monument, 
    objects.stationery, 
    objects.vehicle
]

objs_with_food_properties = [
    objects.vegetable, 
    objects.fruit
]

objs_with_emotions = [
    objects.party, 
    objects.holiday, 
    objects.game, 
    objects.concert, 
    objects.season, 
    objects.weather
]

objs_with_numbers = [
    objects.planet, 
    objects.star, 
    objects.game, 
    objects.concert, 
    objects.vegetable, 
    objects.fruit,
    objects.beverage, 
    objects.dish, 
    objects.furniture, 
    objects.terrain, 
    objects.building, 
    objects.monument, 
    objects.stationery, 
    objects.vehicle
]

objs_with_quantity = [
    objects.beverage, 
    objects.dish 
]