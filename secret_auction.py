import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
from art import logo
print(logo)
    
def highest_bidding(bidding_records):
    highest_bid=0
    winner=""
    for bidder in bidding_records:
        bid_amount=bidding_records[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")
    
bids={}
bidding_finished=False

while not bidding_finished:
    name=input("What is your name: ")
    price=int(input("Enter your bid: "))
    
    bids[name]=price
    
    should_continue=input("Are there any other bidders? (Type 'yes' or 'no'.)")
    if should_continue=="no":
        bidding_finished=True
        highest_bidding(bids)
        
    elif should_continue=="yes":
        clear_console()
        
    else:
        print("Invalid input")
        