#read the list of words as input from the user and return the length of each word for the list
size = int(input("Enter the size of the list : "))
wordlist=[]
for i in range(size):
    val = input("Enter the word: ")
    wordlist.append(val)
print("user entered list is : ",wordlist)
len=list(map(lambda w:len(w),wordlist))