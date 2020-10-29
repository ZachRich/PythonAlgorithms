# 1. Iterate from arr[1] to  arr[n] over the array
# 2. Compare the current element (key) to its predecessor
# 3. If the key element is smaller than its predecessor, compare it to the element
#    before. Move the greater elements one position up to make space for the swapped element

def insertionSort(arr):

    for i in range(1, len(arr)):
        
        #Current Element
        key = arr[i]

        #Previous Element
        pred = i-1

        # When your key isnt at arr[0] and the key is less than the previous element
        while pred >= 0 and key < arr[pred]:
            
            #Set key element = to previous element
            arr[pred + 1] = arr[pred]

            #Decrement predecessor to compare further backwards
            pred = pred - 1

        #Set new key to one after inserted algorithm
        arr[pred + 1] = key



def printList(arr):
    for i in range(len(arr)):
        print("%d" % arr[i])


arr = [12, 11, 13, 5, 6]
print("\nBefore Insertion Sort")
printList(arr)

insertionSort(arr)

print("\nAfter Insertion Sort")
printList(arr)

