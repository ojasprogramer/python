print("Hi, Welcome to my quiz!")

 

ans=input("Are you ready to play the quiz (yes/no):  ")
score=0
total_q=4

 

if ans.lower() == 'yes':
  ans=input("1.Who created Python?")
  if ans == "Guido Van Russom":
      score += 1
      print("Correct!")
  else:    
      print("Incorrect, Guido Van Russom")

 


          
  ans=input("2.Who is the current President of USA?")
  if ans == "Joe Biden":
      score += 1
      print("Correct!")
  else:  
          print("Incorrect, Joe Bide")

 


          
  ans=input("3.Which is the biggest star in the solar system?")
  if ans == "Sun":
      score += 1
      print("Correct!")
  else:    
          print("Incorrect, Sun")

 

  
                      
    
          
  ans=input("4.Which is the latest Python Version?")
  if ans == "Python 3.9.1":
      score += 1
      print("Correct!")
  else:    
          print("Incorrect, Python 3.9.1")

 

 

          ans=input("5.Who is the Current Vice President of India?")
  if ans == "Venkaiah Naidu":
      score += 1
      print("Correct!")
  else:    
          print("Incorrect, Venkaiah Naidu")

 

 

          ans=input("6.What is the shortcut key for opening Windows Explorer?")
  if ans == "Windows+E":
      score += 1
      print("Correct!")
  else:    
          print("Incorrect, Windows+E")

 

 

          ans=input("7.Who created Face Book?")
  if ans == "Mark Zuckerberg":
      score += 1
      print("Correct!")
  else:    
          print("Incorrect, Mark Zuckerberg")

 

 

          ans=input("8.Who is the Prime Minister of India?")
  if ans == "Narendra Modi":
      score += 1
      print("Correct!")
  else:    
          print("Incorrect, Narendra Modi")

 

 

          ans=input("9.Who are the original authors of Whatsapp?")
  if ans == "Brian Acton and Jan Koum":
      score += 1
      print("Correct!")
  else:    
          print("Incorrect, Brian Acton and Jan Koum")

 

 

          ans=input("Thank you! Please press Enter key to exit from the quiz ...")
