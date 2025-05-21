import art
print(art.logo)

other_bidders = 'yes'
bids = {}

while other_bidders == 'yes':
    name = input("What is your name?:")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    other_bidders = input("Are there any others bidders? Type 'yes' or 'no'.\n")
    print("\n"*20)

winner = max(bids, key=bids.get)
max_price = bids[winner]

print(f"The winner is {winner} with a bid of ${max_price}.")