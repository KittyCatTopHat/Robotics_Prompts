#we learned how to do math. With code. Cuz we needed more of that. I'm tired. Anyways, ya, we learned how to make the code do math and print out the answer.
bill = float(input("What was the total bill? $ "))
tip = int(input("What percent of a tip did you give? "))
peeps = int(input("How many people are there?"))
answer1 = tip / 100 * bill
answer2 = answer1 + bill
answer3 = answer2 / peeps
answer3 = round(answer3, 2)
print ("you each owe $" + str(answer3))
