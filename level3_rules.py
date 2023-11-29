import grammar
import random

# association rules using description logics

# level 1: article + property + object 
# level 2: article + property + object + preposition + object
# level 3: article + property + object + preposition + article + property + object

art = ''
head1 = []
head2 = []

with open("level3.txt", "w") as level3_file, open("level1.txt", "r") as level1_file:
    level1_file_lines = level1_file.readlines()
    for i in range(50):
        if i % 2 == 0:
            head1.append(random.choice(level1_file_lines)[:-1])
        # head1[i] = head1[i][:-1]  

    for j in range(60, 99):
        if j % 2 == 0:
            head2.append(random.choice(level1_file_lines)[:-1])
        # head2[j] = head2[j][:-1] 

    def dl_level3():
        for i in range(600):
            level3_file.write((random.choice(head1) + " " + 
                          random.choice(grammar.prepositions) + " " + 
                          random.choice(head2)))
            level3_file.write("\n")

    dl_level3()