##############tuple################
#1 . immutable, reassign is possible, item assignment is not possible   , fixed data ,elements are accessed with indexes

a=(10,20,30,40)
#accesng indexing
print(a[1])   #o/p=20
print(a[-1])  #o/p=40

# slicing
print(a[1:4])   #0/p=(20,30,40)
print(a[ :6])    #0/p=(10,20,30,40) out of index value no error

print(a[-1:-3:-1]) #0/p=(40,30) ####negative index
print(a[-3:-1])  #0/p=(20,30)

print(a[::-1]) #reverse a tuple 0/p=(40,30,20,10) it prints the whole element
  
  ###skipping elements/ jump 
print(a[-1:-4:-2])  #o/p=(40,20) it skips the indexes 1 #### by negative
print(a[-1:-4:-3])  #o/p=(40) it skips the indexes two

print(a[::2])   #o/p=   (10,30)  it skips the 1 element  

# a[1]="frits"    #o/p=does not support fot item assignmnent
# print(a)

a=("fruits",40,True,3.5) #o/p reassign is possible
print(a)

############list#############
#1.ordered, mutable,reassingn && item assign is poosible, heterogeneous--can access different datatypes,dynamic data, elements are accesed with indexes,

list1=["army",20,4.5,True,]
#can access with indexes -ve and+ve
print(list1[3]) #o/p=True
print(list1[-3]) #0/p=20


#can access with slicing negative and +ve 
#jumping or skips
print(list1[0:4:2])  #0/p=["army, 4.5"]
print(list1[-1:-5:-2]) #o/p=[True,20]


list1[1]=[1,2.2]  #o/p =['army', [1, 2.2], 4.5, True]   item assinged is possible in list
print(list1)

list1=[1,2,[2,4.5]] #0/p=[1, 2, [2, 4.5]]  reassingned is possible
print(list1)


