import os
import auction_art

print(auction_art.logo)
print("Welcome to the secret auction program. ")


bid_again = True
bidder_list=[]

def add_bidder(name, bid):
    new_dict = {}
    new_dict["name"] = name
    new_dict["bid"] = bid
    bidder_list.append(new_dict)

def find_highest_bidder():
    highest_bid = 0
    for key in bidder_list:
        position = bidder_list.index(key)
        current_bid = bidder_list[position]["bid"]
        if current_bid > highest_bid:
            highest_bid = current_bid
        if bidder_list[position]["bid"] == highest_bid:
            name = bidder_list[position]["name"]
            bid = bidder_list[position]["bid"]

    print(f"The winner is {name} with a bid of ${bid}")


while bid_again:
    name = input("What is your name? ")
    bid = int(input("How much would you like to bid? "))
    add_bidder(name,bid)
    continue_bidding = input("Are there any other bidders? Type 'yes' or 'no'.")
    if continue_bidding == "no":
        bid_again = False
        find_highest_bidder()
    else:
        os.system('cls')
