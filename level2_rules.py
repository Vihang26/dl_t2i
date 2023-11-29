import grammar
import map
import random

# level 2: article + property + object + preposition + object

level2 = []
head = []

with open("level1.txt", "r") as level1_file, open("level2.txt", "w") as level2_file:
    level1_file_lines = level1_file.readlines()
    for _ in range(19):
        head.append(random.choice(level1_file_lines))
        head[_] = head[_][:-1]      

    def dl_level2():
        for i in range(5):
            for __ in random.sample(map.objs, 15):
                for obj2 in __:
                    level2_file.write((random.choice(head) + " " + 
                          random.choice(grammar.prepositions) + " " + 
                          obj2))
                    level2_file.write("\n")

    dl_level2()