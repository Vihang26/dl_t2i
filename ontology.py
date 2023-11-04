from owlready2 import *

onto = get_ontology("http://test.org/onto.owl") # dummy link to store existing local/web-based ontology to the variable "onto"

with onto:
    # objects

    class Food(Thing):
        pass
    class Fruit(Food):
        pass
    class Vegetable(Food):
        pass
    class Beverage(Food):
        pass
    class Dish(Food):
        pass

    class Animal(Thing):
        pass
    class Land_Animal(Animal):
        pass
    class Water_Animal(Animal):
        pass
    class Aerial_Animal(Animal):
        pass

    class Furniture(Thing):
        pass

    class Stationery(Thing):
        pass

    class Vehicle(Thing):
        pass
    class Land_Vehicle(Vehicle):
        pass
    class Water_Vehicle(Vehicle):
        pass
    class Aerial_Vehicle(Vehicle):
        pass

    class Place(Thing):
        pass
    class City(Place):
        pass
    class Country(Place):
        pass
    class Terrain(Place):
        pass
    class Ocean(Place):
        pass
    class River(Place):
        pass
    class Mountain(Place):
        pass
    class Building(Place):
        pass
    class Monument(Place):
        pass

    class People(Thing):
        pass
    class Celebrity(People):
        pass
    class Historical_Figure(People):
        pass
    class Profession(People):
        pass
    class Gender(People):
        pass
    class Race(People):
        pass

    class Body_Part(Thing):
        pass

    class Season(Thing):
        pass

    class Climate(Thing):
        pass

    class Gadget(Thing):
        pass
    class Portable(Gadget):
        pass
    class Unportable(Gadget):
        pass

    class Event(Thing):
        pass
    class Party(Event):
        pass
    class Holiday(Event):
        pass
    class Exam(Event):
        pass
    class Game(Event):
        pass
    class Concert(Event):
        pass

    class Celestial_Body(Thing):
        pass
    class Planet(Celestial_Body):
        pass
    class Asteroid(Celestial_Body):
        pass
    class Star(Celestial_Body):
        pass
    class Constellation(Celestial_Body):
        pass
    class Satellite(Celestial_Body):
        pass

    # properties

    class Color(Thing):
        pass
    class Shape(Thing):
        pass
    class Size(Thing):
        pass
    class Taste(Thing):
        pass
    class Emotion(Thing):
        pass

    # action, position

    class Action(Thing):
        pass
    class Position(Thing):
        pass

    # defining roles and relationships

    class has_color(ObjectProperty):
        domain = [Food, Animal, Furniture, Stationery, Vehicle, Place, People, Climate, Gadget]
        range = [Color]
    class has_shape(ObjectProperty):
        domain = [Food, Furniture, Stationery, Celestial_Body]
        range = [Shape]
    class has_size(ObjectProperty):
        domain = [Food, Animal, Furniture, Stationery, Vehicle, Place, People, Body_Part, Gadget, Celestial_Body]
        range = [Size]
    class has_taste(ObjectProperty):
        domain = [Food]
        range = [Taste]
    class has_emotion(ObjectProperty):
        domain = [Animal, People]
        range = [Emotion]
    class performs_action(ObjectProperty):
        domain = []
        range = [Action]
    class has_position(ObjectProperty):
        omain = []
        range = [Position]

    # defining possible colors

    purple = Color('purple')
    pink = Color('pink')
    neon_pink = Color('neon_pink')
    pastel_pink = Color('pastel_pink')
    dark_blue = Color('dark_blue')
    light_blue = Color('light_blue')
    neon_blue = Color('neon_blue')
    pastel_blue = Color('pastel_blue')
    teal = Color('teal')
    dark_green = Color('dark_green')
    light_green = Color('light_green')
    neon_green = Color('neon_green')
    pastel_green = Color('pastel_green')
    yellow = Color('yellow')
    amber = Color('amber')
    orange = Color('orange')
    red = Color('red')
    maroon = Color('maroon')
    brown = Color('brown')
    black = Color('black')
    gray = Color('gray')
    white = Color('white')
    gold = Color('gold')
    silver = Color('silver')
    beige = Color('beige')

    # defining possible shapes

    square = Shape('square')
    rectangular = Shape('rectangular')
    circular = Shape('circular')
    triangular = Shape('triangular')
    round = Shape('round')
    blocky = Shape('blocky')
    pointy = Shape('pointy')
    pear_shaped = Shape('pear_shaped')
    conical = Shape('conical')
    cone = Shape('cone')
    cylindrical = Shape('cylindrical')
    spherical = Shape('spherical')
    solid = Shape('solid')
    liquid = Shape('liquid')
    oblate = Shape('oblate')

    # defining possible sizes

    big = Size('big')
    broad = Size('broad')
    bulky = Size('bulky')
    fat = Size('fat')
    giant = Size('giant')
    heavy = Size('heavy')
    huge = Size('huge')
    lanky = Size('lanky')
    large = Size('large')
    little = Size('little')
    narrow = Size('narrow')
    plump = Size('plump')
    short = Size('short')
    slim = Size('slim')
    small = Size('small')
    stout = Size('stout')
    tall = Size('tall')
    thick = Size('thick')
    thin = Size('thin')
    tiny = Size('tiny')
    wide = Size('wide')

    # defining possible tastes

    bitter = Taste('bitter')
    fishy = Taste('fishy')
    fruity = Taste('fruity')
    grassy = Taste('grassy')
    herbal = Taste('herbal')
    juicy = Taste('juicy')
    sweet = Taste('sweet')
    sour = Taste('sour')
    salty = Taste('salty')
    spicy = Taste('spicy')
    pungent = Taste('pungent')
    meaty = Taste('meaty')
    woody = Taste('woody')
    crisp = Taste('crisp')
    mushy = Taste('mushy')
    bland = Taste('bland')

    # defining possible emotions

    attractive = Emotion('attractive')
    bold = Emotion('bold')
    brave = Emotion('brave')
    cheerful = Emotion('cheerful')
    comfortable = Emotion('comfortable')
    excited = Emotion('excited')
    festive = Emotion('festive')
    optimistic = Emotion('optimistic')
    proud = Emotion('proud')
    wonderful = Emotion('wonderful')
    happy = Emotion('happy')
    joyful = Emotion('joyful')
    serene = Emotion('serene')
    upbeat = Emotion('upbeat')
    dirty = Emotion('dirty')
    dejected = Emotion('dejected')
    irritated = Emotion('irritated')
    pessimistic = Emotion('pessimistic')
    tearful = Emotion('tearful')
    tense = Emotion('tense')
    tired = Emotion('tired')
    weak = Emotion('weak')
    angry = Emotion('angry')
    gloomy = Emotion('gloomy')
    grumpy = Emotion('grumpy')
    mad = Emotion('mad')
    nervous = Emotion('mad')
    sad = Emotion('sad')
    guilty = Emotion('guilty')
    anxious = Emotion('anxious')
    cautious = Emotion('cautious')
    shy = Emotion('shy')
    calm = Emotion('calm')
    confident = Emotion('confident')
    surprised = Emotion('surprised')

    # defining possible action words

    being = Action('being')
    having = Action('having')
    doing = Action('doing')
    saying = Action('saying')
    going = Action('going')
    getting = Action('getting')
    making = Action('making')
    thinking = Action('thinking')
    taking = Action('taking')
    seeing = Action('seeing')
    coming = Action('coming')
    using = Action('using')
    giving = Action('giving')
    working = Action('working')
    calling = Action('calling')
    asking = Action('asking')
    holding = Action('holding')
    putting = Action('putting')
    pushing = Action('pushing')
    pulling = Action('pulling')
    placing = Action('placing')
    walking = Action('walking')
    running = Action('running')
    dancing = Action('dancing')
    singing = Action('singing')
    keeping = Action('keeping')
    eating = Action('eating')
    cooking = Action('cooking')
    finding = Action('finding')
    moving = Action('moving')
    bringing = Action('bringing')
    writing = Action('writing')
    sitting = Action('sitting')
    sleeping = Action('sleeping')
    standing = Action('standing')
    meeting = Action('meeting')
    watching = Action('watching')
    winning = Action('winning')
    losing = Action('losing')
    buying = Action('buying')
    wearing = Action('wearing')
    baking = Action('baking')

    # defining possible positions

    on = Position('on')
    above = Position('above')
    below = Position('below')
    inside = Position('inside') # not 'in' since it is a keyword
    outside = Position('outside')
    near = Position('near')
    far_away_from = Position('far_away_from')
    before = Position('before')
    after = Position('after')
    to_the_left_of = Position('to_the_left_of')
    to_the_right_of = Position('to_the_right_of')
    beside = Position('beside')
    over = Position('over')
    under = Position('under')
    on_top_of = Position('on_top_of')
    in_between = Position('in_between')
    next_to = Position('next_to')
    behind = Position('behind')
    in_front_of = Position('in_front_of')

    # defining vegetables

    carrot = Vegetable("carrot",
                        has_shape=[long, conical, cylindrical, pointy],
                        has_size=[big, giant, huge, slim, small, tall, thick, thin, tiny],
                        has_color=[yellow, orange],
                        has_taste=[sweet, woody, crisp])
    eggplant= Vegetable("eggplant",
                        has_shape=[long, pear_shaped],
                        has_size=[big, bulky, fat, giant, heavy, huge, large, little, small, thick, thin, tiny]
                        has_color=[purple],
                        has_taste=[crisp, bitter])
    cucumber = Vegetable("cucumber",
                        has_shape=[long, cylindrical],
                        has_size=[big, bulky, fat, giant, heavy, huge, large, little, short, slim, small, thick, thin, tiny]
                        has_color=[green],
                        has_taste=[juicy, crisp, bitter])
    zucchini = Vegetable("zucchini",
                        has_shape=[long, cylindrical],
                        has_size=[big, bulky, fat, giant, heavy, huge, large, little, short, slim, small, thick, thin, tiny]
                        has_color=[green],
                        has_taste=[crisp, bland])
    potato = Vegetable("potato",
                        has_shape=[round, blocky],
                        has_size=[big, broad, bulky, fat, giant, heavy, huge, large, little, plump, small, stout, thick, thin, tiny]
                        has_color=[yellow, white],
                        has_taste=[sweet, woody])
    pumpkin = Vegetable("pumpkin",
                        has_shape=[round, oblate],
                        has_size=[big, bulky, fat, giant, heavy, huge, large, little, plump, small, stout, tiny]
                        has_color=[yellow, orange],
                        has_taste=[sweet, mushy])
    avocado = Vegetable("avocado",
                        has_shape=[pear_shaped],
                        has_size=[big, fat, giant, heavy, huge, large, little, plump, small, stout, tiny]
                        has_color=[green],
                        has_taste=[sweet, mushy, woody])
    mushroom = Vegetable("mushroom",
                        has_shape=[round],
                        has_size=[big, bulky, fat, giant, heavy, huge, large, little, plump, small, stout, tiny]
                        has_color=[gray],
                        has_taste=[meaty, woody])
    lettuce = Vegetable("lettuce",
                        has_shape=[round],
                        has_size=[big, giant, heavy, huge, large, little, small, tiny]
                        has_color=[green],
                        has_taste=[grassy, crispy, sweet, bitter])
    cabbage = Vegetable("cabbage",
                        has_shape=[round],
                        has_size=[big, giant, heavy, huge, large, little, small, tiny]
                        has_color=[green],
                        has_taste=[crispy, sweet, grassy])
    broccoli = Vegetable("broccoli",
                        has_shape=[round],
                        has_size=[big, giant, heavy, huge, large, little, small, tiny]
                        has_color=[green],
                        has_taste=[grassy, bitter])
    asparagus= Vegetable("asparagus",
                        has_shape=[cone, long],
                        has_size=[big, fat, giant, heavy, huge, large, little, short, slim, small, tall, thick, thin, tiny]
                        has_color=[green],
                        has_taste=[grassy, bitter, sweet])
    bell_pepper = Vegetable("bell_pepper",
                            has_shape=[blocky],
                            has_size=[big, broad, bulky, fat, giant, heavy, huge, large, little, plump, slim, small, stout, tiny]
                            has_color=[green, red, yellow],
                            has_taste=[spicy, crisp, sweet])
    chilli = Vegetable("chilli",
                        has_shape=[pointy, long],
                        has_size=[big, fat, giant, huge, large, little, short, slim, small, thick, thin, tiny]
                        has_color=[green, red, yellow],
                        has_taste=[spicy, crisp])
    onion = Vegetable("onion",
                        has_shape=[round],
                        has_size=[big, bulky, fat, giant, heavy, huge, large, little, small, tall, tiny]
                        has_color=[white, purple],
                        has_taste=[pungent, sweet, crisp])
    spring_onion = Vegetable("spring_onion",
                            has_shape=[long],
                            has_size=[giant, heavy, huge, little, slim, small, thick, thin, tiny]
                            has_color=[white, green],
                            has_taste=[pungent])
    garlic = Vegetable("garlic",
                        has_shape=[round, spherical],
                        has_size=[big, broad, bulky, fat, giant, heavy, huge, large, little, small, tiny]
                        has_color=[white],
                        has_taste=[sweet])
    leek = Vegetable("leek",
                    has_shape=[long, cylindrical],
                    has_size=[big, giant, large, little, slim, small, stout, tall, thick, thin, tiny]
                    has_color=[green],
                    has_taste=[sweet, crispy])
    parsley = Vegetable("parsley",
                        has_shape=[long],
                        has_size=[big, giant, huge, large, little, short, small, thin, tiny, wide]
                        has_color=[green],
                        has_taste=[herbal, woody])
    
    # defining fruits

    apple 
    mango 
    banana 
    strawberry 
    pineapple 
    lime 
    watermelon 
    pomegranate

    # defining beverages

    water 
    coffee
    tea
    hot_chocolate
    milkshake
    juice

    # defining dishes

    sandwich
    burger
    
    pizza
    cake
    pie
    meatball
    soup

    
    