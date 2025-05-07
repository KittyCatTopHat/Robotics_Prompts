#we learned how to respond and use numbers (int and float).
generation = int (input("what year were you born?"))
if generation >= 1925 and generation <= 1946 :
  print("You're a Traditionalist")
elif generation >= 1947 and generation <= 1964 :
  print("You're a Baby Boomer")
elif generation >= 1965 and generation <= 1981 :
  print("You're a Gen X")
elif generation >= 1982 and generation <= 1995 :
  print("You're a Millenial")
elif generation >= 1996 and generation <= 2015 :
  print("You're a Gen Z")
else :
  print("You lived with the dinasours then. Or you shouldn't own a phone yet")
