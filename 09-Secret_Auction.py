
# Day 7 - Hangman
# Dictionaries and Nesting

from os import system, name
# import sleep to show output for some time period
from time import sleep
# define our clear function
def clear():
  # for windows
  if name == 'nt':
    _ = system('cls') 

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  highest_bid_key = ""
  for bidder in bidding_record:
    # Compares bidder's bid with current highest
    if bidding_record[bidder] > highest_bid: 
      highest_bid = bidding_record[bidder]
      highest_bid_key = bidder
  print(f"The winner is {highest_bid_key} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()
  
