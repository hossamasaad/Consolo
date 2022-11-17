import os
from exceptions import *
import time

class Friend:
    def __init__(self, username, authorizor, authenticator) -> None:
        """
        Crater Adapter to add users to friend users
        
        Args:
            username: name of the user who will add a friend
            authorizor: authorizor will manage permissions
            authenticator: authenticator will manage users
        """
        self.authorizor = authorizor
        self.authenticator = authenticator
        self.username = username
        self.user = self.authenticator.get_user(self.username)


    def send_friend_request(self):
        """
        Add friend to user friends

        Args:
            friendname: friend's name we will add
        """
        friendname = input("Enter friend name: ")
        try:
            friend = self.authenticator.get_user(friendname)
            friend.friend_requests.add(self.user)
        except InvalidUsername:
            os.system("clear")
            print("---------------------------------")
            print("The name isn't valid")
            print("---------------------------------")
        else:
            os.system("clear")
            print("---------------------------------")
            print("Your friend request was sent successfully")
            print("---------------------------------")
    

    def show_friends(self):
        """
        Show user friends
        """
        if not len(self.user.friends):
            os.system("clear")
            print("---------------------------------") 
            print("You are still ALONE ;(")

        os.system("clear")
        for friend in self.user.friends:    
            print("---------------------------------") 
            print("Friend: {}".format(friend.username))
        print("---------------------------------")


    def show_friend_requests(self):
        """
        Show user friend requests
        """

        if not len(self.user.friend_requests):
            os.system("clear")
            print("---------------------------------") 
            print("No friend requests ;(")
            print("---------------------------------")
            return

        os.system("clear")
        for request in self.user.friend_requests:
            print("---------------------------------") 
            print("request: {}".format(request.username))
        print("---------------------------------")

        # get the friend user want to accept
        answer = input("Enter the name you want to accept or click `Enter` to skip: ").lower()
        
        if answer:
            try:
                friend = self.authenticator.get_user(answer)
            except InvalidUsername:
                os.system("clear")
                print("---------------------------------")
                print("The name isn't valid")
                print("---------------------------------")
            else:
                self.accept_friend(friend)


    def accept_friend(self, friend):
        """
        Accept a friend request

        Args:
            user object of the friend the user want to accept
        """
        self.user.friend_requests.remove(friend)
        self.user.friends.add(friend)
        friend.friends.add(self.user)
        
        os.system("clear")
        print("---------------------------------")
        print("Friend added successfully")
        print("---------------------------------")
        time.sleep(2)
        self.show_friend_requests()