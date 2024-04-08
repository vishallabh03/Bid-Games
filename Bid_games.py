import os
bid= {} # bid is an empty dictioney
bidding_finished=False
def find_highest_bidder(bidding_record):
    highest_bid=0
    winner={}
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder] 
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
            print (f"The winner is {winner} with a bid of $ {highest_bid}")


while not bidding_finished:
    name=input("What is your name?: ")
    price=input("What is your bid ?:  $")
    bid [name]=price # we are creating key in a empty dictionery 
    more_bidders=input("Are there any other bidders? Type 'Yes' or 'No'").lower()
    
    if more_bidders=="No":
        bidding_finished=True
        find_highest_bidder(bid)
    elif more_bidders=="yes":
        os.system("cls")
    
    
