#program to genrate 5 random number between 1-20
import random

qn=("Q1.who was the first Billionare?",
    "Q2.Which youtube channel has the most subscribers?",
    "Q3.Which is the largest star?",
    "Q4.Which is the biggest black hole")


ans=("John.D Recklefeller",
    "T-Series",
    "Stephenson 2-18",
    "TON-618")


user_option = input("Do you want to play this trivia (y/n)?:")
if user_option.lower == 'n':
    exit
for lap in range(1,3):
    rnd_qn=random.randint(1,3)
    user_ans= input(qn[rnd_qn])
    
    if (user_ans == ans[rnd_qn]):
        print("Correct Answer")
    else:
        print("Incorrect Answer")    











 