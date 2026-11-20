
num = [int(x) for x in input("Enter the values separated by space: ").split()]
target = int(input("Enter the target value: "))
num.sort()
print("Sorted array is: ", num)

left =0
right = len(num) -1
found = False
while left <= right:
    mid = (left+right) // 2

    if num[mid] == target:
        print("The element is found at index: ",mid)
        found = True
        break
    elif num[mid] < target:
        left = mid+1
    else:
        right = mid - 1

if not found:
    print("Element is not found (-1)")
