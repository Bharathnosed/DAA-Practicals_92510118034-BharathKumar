
num = [int(x) for x in input("Enter the elements using spaces:").split()]
n= len(num)
is_sorted = False
pass_count = 0
while not is_sorted:
    is_sorted = True
    left=0
    while left < (n-1-pass_count):
        right = left + 1

        if num[left] > num[right]:
            num[left],num[right]=num[right],num[left]
            is_sorted=False
        left += 1
    pass_count += 1
print("Total passes done: ",pass_count)
print("Sorted List :",num)

