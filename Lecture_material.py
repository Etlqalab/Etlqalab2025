tweet = input("enter your tweet: ")

length = len(tweet)

max_len = 10

if length <= max_len:
    print(f"That {length} char tweet will work!")
else:
    print(f" Your {length} chat tweet is {length - max_len} chars too long")











