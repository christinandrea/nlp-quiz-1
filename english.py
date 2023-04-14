import os
eng = os.chdir('english')
engFiles = os.listdir(eng)

for j in engFiles:
    if j.endswith('.txt'):
        files = open(j,'r')
       
        print(files.read())

