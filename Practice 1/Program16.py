from collections import deque

bank = deque(["Ashmi", "Smrity", "Showrav"])
print(bank)
bank.popleft()
print(bank)
bank.popleft()
bank.popleft()

if not bank:
    print('No person left')