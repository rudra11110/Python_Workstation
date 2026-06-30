#For loop
l = ["raja", "sonam", "ram", "sonu"]

found = False
for i in l:
    if i.startswith("s"):
        print(i)
        found = True

if not found:
    print("No name starts with s")