from functools import reduce

a=lambda n:n*n
print(a(5))

#lambda filter map reduce

nums=[2,23,56,3,34,5,3,34,4]

#filter
evens = list(filter(lambda n : n%2==0,nums))
print(evens)

#map
doubles = list(map(lambda n : n**2,evens))
print(doubles)

#reduce
sum = reduce(lambda a,b : a+b,doubles)
print(sum)