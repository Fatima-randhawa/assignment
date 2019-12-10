Cheeses = ['Cheddar','Edam','Goudo']
numbers = [17,123]
empty =[]
print(cheeses,numbers,empty)

numbers = [17,123]
numbers[1] = 5
print(numbers)

a = [1,2,3]
b = [4,5,6,]
c = a+b 
print (c)

[0]*4

t = ['a','b','c','d','e','f']
t[1:3]

t [:4]

t[3:]

t[:]

t=['a','b','c']
t.append('d')
print(t)

t1=['a','b','c']
t2=['d','e']
t1.extend(t2)
print(t1)

t=['d','c','e','b','a']
t.sort()
print(t)

t=['a','b','c']
x=t.pop(1)
print(t)
print(x)

nums=[3,41,12,9,74,15]
print(len(nums))
print(max(nums))
print(sum(nums))
print(sum(nums)/len(nums))
