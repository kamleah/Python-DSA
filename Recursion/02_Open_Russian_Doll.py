def openRussianDoll(doll):
    if doll == 1:  # Base Condition
        print("all dolls are opened")
    else:
        print(f"Doll {doll} is opened.")
        openRussianDoll(doll - 1)  # Recursive Call


openRussianDoll(5)
