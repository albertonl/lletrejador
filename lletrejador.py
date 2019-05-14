# Lletrejador de Català
# Alberto Navalon Lillo (C) May 2019
# This software is subject to the GNU General Public License
# For further information and details, visit the repository page:
# https://github.com/albertonl/lletrejador


import random # To use the random.randint() function to generate a random index to give a word

# We parse all elements in Catalan dictionary
xmldoc = minidom.parse('apertium-cat.cat.dix')
elist = xmldoc.getElementsByTagName('e')

dicts = []
for e in elist:
    d = {}
    for a in e.attributes.values():
        d[a.name] = a.value
    dicts.append(d)



finished = False
answer = 's'
# Main loop
while finished==False:
    print(dicts[random.randint(0,len(dicts)-1)]['lm']);

    answer = input("Vols continuar? (s/n): ")
    if answer=='n':
        finished = True
        quit()
