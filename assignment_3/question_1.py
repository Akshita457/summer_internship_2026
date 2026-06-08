#1) Practise Dictionary, Tuple and Set

#Dictionary
d1={1:"apple",2:"mango",3:"banana"}

#add element
d1[4]=["cherry"]
print(d1)

#delete element
del(d1[4])
print(d1)

#copy
d2=d1.copy()
print(d2)

#show values or keys individually
d1.keys()
d1.values()

#Tuple
t=("carbon","nitrogen","oxygen")
for x in t:
    print(x)

#concatenation
t1=(10,20,30)
t2=(40,50,60,("a","b","c")) #nested tuples
t3=t1+t2
print(t3)

#tuple methods
tup=(20,40,60,20,80)
print(min(tup))
print(max(tup))
print(tup.count(20))
print(tup.index(40))
print(sum(tup))

#Sets
s={20,"apple","mango",40,89,20,1, True} 
print(s,type(s))
#set operations

#adding elements
s1={"apple","mango","banana"}
s1.add("cherry")
print(s1)

#union
s2={"potatao","tomato","apple"}
print(s1.union(s2))
#method 2 for union
print(s1|s2)

#intersection
print(s1.intersection(s2))

#method 1 for intersection
new_s=s1.intersection(s2)
print(new_s)

#method 2 for intersection
print(s1&s2)

#differnece
print(s1-s2)



