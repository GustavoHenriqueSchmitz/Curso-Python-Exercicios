nome = input('Digite algo')
print('O tipo primitivo desse valor é',(type)(nome))
print('É númerico?',nome.isnumeric())
print('É alfabético?',nome.isalpha())
print('É minusculo?',nome.islower())
print('É maiusculo',nome.isupper())
print('É decimal?',nome.isdecimal())
print('Tem somente espaços?',nome.isspace())
print('É capitalizado?',nome.istitle())
