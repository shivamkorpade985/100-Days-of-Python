
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"Winner is {winner},with the bid of ${highest_bid}.")

bids = {}
countinue_bidding = True
while countinue_bidding:
    name = input("Enter name:")
    price = int(input("Enter bid:$"))
    bids[name] = price
    should_continue = input("Type 'yes' or 'no' whether the next bidder wants to bid?").lower()
    if should_continue == 'no':
        countinue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        print("\n" * 20)
