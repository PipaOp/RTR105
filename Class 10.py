#7,2,bob,10,4.
largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
try:
    
    if num == "bob":
        print("Invalid input")
        continue
    if num > largest:
        largest=num
    if smallest is None:
        smallest=num
    elif num < smallest:
        smallest=num
    if num == "done" : break
    print(num)

print("Maximum", largest)
print("Minimum",smallest)
