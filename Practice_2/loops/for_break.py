# Search for a forbidden word
comments = ["Good job", "Great", "SPAM", "Nice work"]
for comment in comments:
    if comment == "SPAM":
        print("Spam detected! Filtering stopped..")
        break
    print(f"Comment posted: {comment}")

# Out of range
for i in range(1, 1000):
    if i == 5:
        print("Enough!")
        break