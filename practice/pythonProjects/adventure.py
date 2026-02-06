name = input("Type your name:")
print("Welcom", name, "to this adventure!")

print("You are on a dirt road, it has come to an end and you can go Left or Right. Which way you like to go ?")

answer = input().lower()

if answer == "left":
    ans = ("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ").lower()
    if ans == "swim":
        print("You swim across and face an alligator.")
    elif ans == "walk":
        print("You walked for many miles in forest, you got miss directed and huntted by a Tiger and you lost the game. ")
    else:
        print("Not a valid option.")

elif answer == "right":
    ans = input("You come to a bridge, it looks wobbly, do you want to cross it or head back(c/b)").lower()
    if ans == "b":
        print("You go back and loose")
    elif ans == "c":
        ans = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

        if answer == "yes":
            print("You talk to the stanger and they give you gold. You WIN!")
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose.")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

else:
    print("Not a valid option. Try again!")


print("Thank you for trying ", name )