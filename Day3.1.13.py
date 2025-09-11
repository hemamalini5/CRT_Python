#Declare two list of numbers and concantenate the given list of numbers and sorted in ascending order
list1=[10,20,30]
list2=[15,25,35]
list=list1+list2
list.sort()          #ascending order
print(list)
list.sort(reverse=True) #Descending order
print(list)