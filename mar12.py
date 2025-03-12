#day 8
#we practiced using inputs and else/if statments today. I learned how to accept multiple inputs for a if/elif statment.
name = input("What is your name? ")
print(name + "...Yes. Yes I remeber you now.")
print("Let's see what else we can include here...")

food = input("What food brings you joy?")
print("Interesting... I'll see what I can do with this...")

animal = input("What creature do you find delight in? ")
print("Hmmm. Okay. Let's see what happens.")

day = input("Tell me, which day of the week is it today? ")
if day == "Monday" or day == "monday":
  print("Today is... No, that can't be! it's to soon. NOOOOO!!!")
elif day == "Tuesday" or day == "tuesday":
  print ("So, we're not there yet? Good... good.")
elif day == "Wednesday" or day == "wednesday":
  print("""Halfway trough... halfway through what? Wahat's going on? Who are you again? Have we met?""")
elif day == "Thursday" or day == "thursday":
  print("We're almost through. Almost done. Almost free.")
elif day == "Friday" or day == "friday":
 print("It's alamost complete. We'll make it, I'll be there.")
else:
  print("No, no. That's... that's not right.")

print("Wait... I over reacted. Or perhaps I under-reacted? Whatever, it's just an " + animal + " eating some " + food + ". Everything is OKAY!!!")
