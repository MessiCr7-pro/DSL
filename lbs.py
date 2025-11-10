def linearsearch (numbers,target):
    for i in range (len(numbers)):
        if numbers[i] == target:
            print(f"element found at index {i}")
            return
    print ("no element found")

def binarysearch (numbers,target):
    l=0
    h=len(numbers)-1

    while (l<=h):
        m =( h+l )//2 
        if (numbers[m] == target):
            print (f"element found at index {m}")
            return
        elif (numbers[m] < target):
            l= m+1
        else:
            h=m-1
    print("element not found") 

numbers = [12,14,15,17,45,78,90]
target = 45

print("linear search")
linearsearch (numbers,target)

print ("binary search")
binarysearch (numbers,target)
