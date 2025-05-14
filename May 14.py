#day 11
#we just practiced multiplying in the code, not much learinging. Only puttin g a bunch of knowledge together.
# im prety sure they menat for me to do it differently but oh well.
answer = input ("Do you want know how many seconds are in year?")
if answer == "yes":
    print("Ok!")
elif answer == "no":
    print("Too bad")
else:
    print ("here we go anyway")
seconds = 60*60*24*365
print("There are", seconds, "seconds in a year")
print ("but in a leap year...")
leapseconds = seconds + 60*60*24
print ("There is", leapseconds)
print ("wow, that's a lot.")
