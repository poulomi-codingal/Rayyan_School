import time
def print_slow(text, delay=0.15):
    print(text)
    time.sleep(delay)

print_slow("Hello")
name=str(input("What is your name)")).lower()
print_slow(f"{name}, that is a nice name. be prepared for more questions")
mood=str(input("Enter your mood, happy/excited or sad/angry")).lower()
while True:
    if mood=="happy":
     print_slow("Good. may you be happy for the rest of your life")
     break
    elif mood=="angry":
      print_slow("Cool down, and let your soul relax with you")
      break
    elif mood=="sad":
      print_slow("Do something you like, and may you be blessed")
      break
    elif mood=="excited":
      print_slow("good. stay that way, and you will forever be excited")
      break
    elif mood=="tired":
       print_slow("Rest and relaxation brings your soul closer to you")
       break
    else:
       print_slow("Huh. incorrect input. enter again, and may nothing be with you")
       continue
num=int(input("Enter a number you want"))
num2=int(input("enter a numbr you want"))
operation=str(input("Enter operation with number1 and number 2"
""))
while True:
 if operation=="addition":
   add=num+num2
   print_slow(f"{add}here is your answer")
   break
 elif operation=="subtraction":
   p=int(input(f"Enter the which number you want to minus.1={num}-{num2} or 2={num2}-{num}"))
   if p==1:
     sub1=num-num2
     print_slow(f"Here is your number sum{sub1}")
     break
   else:
     sub2=num2-num
     print_slow(F"here is your sum{sub2}")
     break
 elif operation=="multiplication":
   tot=num*num2
   print_slow(f"sum={tot}")
   break
 elif operation=="division":
   o=int(input(f"Enter number oder you wnat to divide.1={num} divided by{num2}.2={num2} divided by{num}"))
   if o==1:
     ty=num/num2
     print_slow(f"Answer={ty}")
     break
   else:
     yt=num2/num
     print_slow(f"Here is answer{yt}")
     break
 else:
   print_slow("Incorrect. try again")
   break
food=str(input("Enter your fav food"))
while True:
  if "pizza" in food or "pasta" in food:
    print_slow("Huh an italian classique. pasto felice! ")
    break
  elif "salad" in food or "protein shake" in food:
    print_slow("A buff guy.Live a little bro")
    break
  elif "chips" in food or "candy" in food:
    print_slow("A junkie eh. Say 👋bye to your teeth")
    break
  else:
    print_slow(f"yoooooooooo. i also like that food({food}),{name}")
    break
while True:
  print_slow("Welcome to the final part of the test.")
  print_slow("These three questions will be hard, ranging from math, to general knowledge and english")
  score=0
  math=int(input("Answer this: A train leaves a station and travels at a constant speed of 60 miles per hour. How many minutes will it take for the train to travel 45 miles?(do working out in books, we will only accept final answer)"))
  if math == 45:
    print_slow("Good job. you have succced")
    score +=1


  else:
    print("BOOOOOOOOOOO you are in the negatives")
    score-=1
  
  general=str(input("Here answer this:What gas do plants absorb from the atmosphere to perform photosynthesis?")).lower()
  if general in ("Carbon" ,"carbon dixode" , "Co2"):
    print_slow("Good")
    score+=1
  else:
    print_slow("incorrect ... ")
    score-=1

  english=str(input("Answer this: Identify the adverb in the following sentence:The exhausted runner crossed the finish line yesterday.")).lower()
  if english=="yesterday":
    print_slow("Goood")

    score+=1
    break

  else:



    print("NOOB!NOOB!NOOB!!!!!")
    score-=1
    break

print_slow(f"Here is your score:{score}")
print_slow("Thank you and goodbye")