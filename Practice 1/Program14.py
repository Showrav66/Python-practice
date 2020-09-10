#Data structure
#List #Tuple #Set #Dictionary #Stack #Queue

list = [1,2,4]
set =  {5,8,9,4}

dictionary = {
    1 :"Stastisticsl",
    2 :"Quantum",
    3:"Relativistic",
    4:"Thermodynamics"
}
dictionary[2] = 'Classical'
print(dictionary)
print(dictionary.get(2,'Keyword Not Found'))

tuple = ((
    'Showrav',
    'Smrity',
    'Ritu',
    'Ashmi'
), (
    'Sh',
    'Sm',
    'R',
    'A'
),
(
    'Showrav',
    'Smrity',
    'Ritu',
    'Ashmi'
), (
    'Sh',
    'Sm',
    'R',
    'A'
))
print(tuple)
print(tuple[1][1][1])
