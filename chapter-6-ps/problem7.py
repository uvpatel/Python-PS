# 7. Write a program to find out whether a given post is talking about “Harry” or not.


#  Write a post whatever you want to like
post = input("Enter Your Post").capitalize

if("Harry" in post):
    print("This post is talking about Harry")
else:
    print("This post is not talking about Harry")