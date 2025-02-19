#We praccticed variables and inputs in the print function by writing a short story. We learned how to change the text colour in the Console.
food = input("List a food:")
noun = input("List an object:")
name = input("List a name:")
action = input("List an action:")
action1 = input("List another action:")

print("\033[35m","You walk around a corner of a busy street. Seeing a shop,you walk in. You are surised to see the shop selling only one iteam, which just so happens to be your favourite food:", food, ". The clerk, who's name is", name," - which you can see on there nametag - asks for your order. As you ", action, "to the waiting section, you nock over a", noun, ". ", name, action1, " over and cleans the mess. Feeling embarrassed, you decide to sneak out befor making a bigger mess.")
