# Day 7
# We learned how to branch off "if statments" if they answer a certain way. It took me a while to procces this, but I evenetually ot it.
print ("Are you a true Shera fan? Let's find out.")
Swiftwind = input("What is the name of the alicorn (the winged unicorn)")
if Swiftwind == "Swiftwind":
  print ("Correct!")
elif Swiftwind == "swiftwind":
    print ("Correct! Although his name isn't capitalized...")
elif Swiftwind == "Catra":
  print ("It has the word CAT in the name!")
else:
  print ("Wrong! Its Swiftwind!")

print ()

thing = input("What does Adora say when she transforms into Shera?")
if thing == "For the honor of Greyskull!":
  print ("Correct!")
  sword = input ("What does she say it to?")
  if sword == "Sword":
    print ("Correct!")
  else:
    print ("Nop")
else:
  print ("Wrong! It's for the honor of Greyskull!")
