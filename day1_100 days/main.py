import time
print("""Peter Manda
20 October 2022
I am signing up for Replit's 100 days of Python challenge!
I will make sure to spend some time every day coding along, for a minimum of 10 minutes a day.
I'll be using Replit, an amazing online IDE so I can do this from my phone wherever I happend to be. No excuses for not coding from the middle of a field!
I am feeling 😎 
You can follow my progress at replit.com/@PeterManda19""")

def endGame():
  while True:
    print()
    x= input("""Thank you for reading!
To read again please click Stop on top right page and click Run """)
    print()
    continue


if __name__ == "__main__":
  time.sleep(2)
  endGame()
