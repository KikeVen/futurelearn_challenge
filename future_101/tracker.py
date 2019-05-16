guess = input("guess my name ")
counter = 0
while guess != "Martin":
    guess = input("wrong - guess again ")
    counter += 1
print("well done")
print("You made", counter, "guesses before landing on", guess)
