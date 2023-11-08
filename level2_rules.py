import grammar
import map

# level 2: article + property + object + preposition + object

level2 = []
head = []

with open("level1.txt", "r") as level1_file, open("level2.txt", "w") as level2_file:
    level1_file_lines = level1_file.readlines()
    for i in range(19):
        if i % 2 == 0:
            head.append(level1_file_lines[i][:-1])           

    def dl_level2():
        for phrase1 in head:
            for preposition in grammar.prepositions:
                for __ in map.objs:
                    for obj2 in __:
                        level2_file.write(phrase1 + " " + preposition + " " + obj2)
                        level2_file.write("\n")

    dl_level2()