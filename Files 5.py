fhand = open('Volvo.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith("asd"):
        print(line)
"""
fhand = open('Volvo.txt')
for line in fhand:
    if line.startswith("asd"):
        print(line)
"""
"""
fhand = open('Volvo.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith("asd"):
        continue
    print(line)
"""
