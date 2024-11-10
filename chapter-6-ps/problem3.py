'''3. A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
to detect these spams.'''

str = ["Make a lot of money", "buy now", "subscribe this", "click this"]

if("Make a lot of money" or "buy now" or "subscribe this" or "click this" in str):
    print("This is a spam messages are in str list")
else:
    print("Not a spam comments")