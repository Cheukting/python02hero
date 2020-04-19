john = {'father' : 'David', 'mother' : 'May'}
lucy = {'father' : 'Geoge', 'mother' : 'Teresa'}
mary = {'father' : john, 'mother' : lucy}

grand_parents_of_mary = [mary['father']['father']]
grand_parents_of_mary.append(mary['mother']['father'])
grand_parents_of_mary.append(mary['father']['mother'])
grand_parents_of_mary.append(mary['mother']['mother'])

this_person = 'David'
that_person = 'Tom'

print(f"{this_person} is Mary's granny? {this_person in grand_parents_of_mary}")
print(f"{that_person} is Mary's granny? {that_person in grand_parents_of_mary}")
