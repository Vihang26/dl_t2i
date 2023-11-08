import map
import grammar
import properties
import level1_rules

# association rules using description logics

# level 1: article + property + object 
# level 2: article + property + object + preposition + object
# level 3: article + property + object + preposition + article + property + object

art = ''
head1 = []
head2 = []

with open("level3.txt", "w") as level3_file, open("level1.txt", "r") as level1_file:
    level1_file_lines = level1_file.readlines()
    for i in range(19):
        if i % 2 == 0:
            head1.append(level1_file_lines[i][:-1])

    for j in range(80, 99):
        if j % 2 == 0:
            head2.append(level1_file_lines[j][:-1])

    def dl_level3():
        for phrase1 in head1:
            for preposition in grammar.prepositions:
                for phrase2 in head2:
                    level3_file.write(phrase1 + " " + preposition + " " + phrase2)
                    level3_file.write("\n")
                    
    dl_level3()