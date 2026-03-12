file = open('jecrc.txt', 'a+')

# file.write('JECRC is the best uni')
# file.write('JECRC is also popular for placements!')
file.writelines([
    '\nHere Food is good! \n',
    'ECOo system is good! \n',
    'Faculties are very supportive! \n'
])
file.seek(0)
print(file.read())




file.close()
