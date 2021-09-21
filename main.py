# instructions
import turtle as trtl
print("Please type in the letter that best suits you")

# Screen
screen = trtl.Screen() 

# points system for house display
points = 0

# Question 1
userinput1 = input("Do you prefer (A) a large, spatial house or (B) a small, cozy house? ")
if userinput1.lower() == "a":
  #print(userinput1)
  points = points + 2
elif userinput1.lower() == "b":
  #print(userinput1)
  points = points + 1
else:
  import Loading_Screen
  print("Your dream house is a Cardboard Box!")
  import Cardboard
  exit()

# Question 2
userinput2 = input("Do you prefer (A) a popular lifestyle or (B) a quiet lifestlye? ")
if userinput2.lower() == "a":
  #print(userinput2)
  points = points + 2
elif userinput2.lower() == "b":
  #print(userinput2)
  points = points + 1
else:
  import Loading_Screen
  print("Your dream house is a Cardboard Box!")
  import Cardboard
  exit()

# Question 3
userinput3 = input("Do you favor (A) urban areas or (B) rural areas? ")
if userinput3.lower() == "a":
  #print(userinput3)
  points = points + 2
elif userinput3.lower() == "b":
  #print(userinput3)
  points = points + 1
else:
  import Loading_Screen
  print("Your dream house is a Cardboard Box!")
  import Cardboard
  exit()

# Question 4
userinput4 = input("Do you (A) favor industrialization or (B) favor nature? ")
if userinput4.lower() == "a":
  #print(userinput4)
  points = points + 2
elif userinput4.lower() == "b":
  #print(userinput4)
  points = points + 1
else:
  import Loading_Screen
  print("Your dream house is a Cardboard Box!")
  import Cardboard
  exit()

# Question 5
userinput5 = input("Do you (A) love technology or (B) hate technology? ")
if userinput5.lower() == "a":
  #print(userinput5)
  points = points + 2
elif userinput5.lower() == "b":
  #print(userinput5)
  points = points + 1
else:
  import Loading_Screen
  print("Your dream house is a Cardboard Box!")
  import Cardboard
  exit()

# System for displaying the correct house
if points == 10:
  # insert code for white house
  import Loading_Screen
  print("Your dream house is the White House!")
  import White_House
  exit()
if points == 5:
  # insert code for river house
  import Loading_Screen
  print("Your dream house is a river house!")
  import River_House
  exit()

else:
  if userinput1.lower() == "a":
    if userinput3.lower() == "b":
      # insert code for isolated castle
      import Loading_Screen
      print("Your dream house is an isolated castle!")
      import Castle
    
    elif userinput3.lower() == "a":
      # insert code for large mansion
      import Loading_Screen
      print("Your dream house is a large mansion!")
      import Large_Mansion
  elif userinput1.lower() == "b":
    if userinput4.lower() == "a" or userinput5.lower() == "a":
      # insert code for car house
      import Loading_Screen
      print("Your dream house is a car house!")
      import Car_House
    else: 
      # insert code for cardboard box
      import Loading_Screen
      print("Your dream house is a Cardboard Box!")
      import Cardboard

#Debug
#print(points)
