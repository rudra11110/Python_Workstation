#list
fruits = []

while True:
    userentered = input("Enter a fruit (or 'done' to stop): ")

    if userentered.lower() == "done":
        break

    fruits.append(userentered)

print("Fruits:", fruits)