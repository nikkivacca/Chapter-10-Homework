infile = open('book of John text.txt', 'r')

BookofJohn = []

num_Father = 0 
num_God = 0 
num_Christ = 0 
num_Spirit = 0
num_spirit = 0 
num_life = 0 
num_man = 0 

for line in infile:
    for word in line.split():
        if word == 'Father':
            num_Father += 1 
        if word == 'God':
            num_God += 1 
        if word == 'Christ':
            num_Christ += 1 
        if word == 'Spirit':
            num_Spirit += 1
        if word == 'spirit':
            num_spirit += 1 
        if word == 'life':
            num_life += 1 
        if word == 'man':
            num_man += 1 


BookofJohn = {'Father': num_Father,
'God': num_God,
'Christ': num_Christ,
'Spirit': num_Spirit,
'spirit': num_spirit,
'life': num_life,
'man': num_man}


for key, value in BookofJohn.items():
    print(key, value, sep=': ')


infile.close()