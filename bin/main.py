import os
import sys
import time
sys.path.append(os.path.realpath('..'))
from app import (AddPost, Home, Friend, Login, Logout, Register,
                 ShowProfile, Authenticator, Authorizor)


# Start authenticator
authenticator = Authenticator()

# Start authorizor
authorizor = Authorizor(authenticator)

class App:
    def __init__(self):
        """
        Start the app
        """
        self.username = None
        self.permissions = ["add post", "send friend request", "logout", "show home", "show profile", "send message"]
        self.add_permissions()
        self.start_menu = {
            "login"   : Login(authorizor, authenticator).login,
            "register": Register(authorizor, authenticator).register,
            "quit"    : self.quit
        }
        
        self.user_menu = {}

    def add_permissions(self):
        """
        Add all permissions can be added to users
        """
        for perm in self.permissions:
            authorizor.add_permission(perm)
            

    def quit(self):
        """
        Exit app
        """
        raise SystemExit()
    

    def new_user(self):
        """
        Show command list for new users, get user command and excute the function
        """
        os.system("clear")
        print("-----------------------------")
        print("CONSOLO: Welcome Back :)")
        print("-----------------------------")
        
        answer = ""
        print(
        """
        Please enter a command:
        login   \tLogin
        register\tCreate new account
        quit    \tQuit
        """
        )

        answer = input("enter a command: ").lower()
        try:
            func = self.start_menu[answer]
        except KeyError:
            print("{} is not a valid option".format(answer))
        else:
            if answer == 'login':
                self.username = func()
                self.user_menu = {
                    "post"      : AddPost(self.username, authorizor, authenticator).post,
                    "profile"   : ShowProfile(self.username, authorizor, authenticator).show,
                    "add-f"     : Friend(self.username, authorizor, authenticator).send_friend_request,
                    "show-f"    : Friend(self.username, authorizor, authenticator).show_friends,
                    "show-rf"   : Friend(self.username, authorizor, authenticator).show_friend_requests,
                    "home"      : Home(self.username, authorizor, authenticator).show_homepage,
                    "message"   : None,
                    "logout"    : Logout(self.username, authorizor, authenticator).logout,
                }
            else:
                func()


    def logged_user(self):
        """
        Show command list for new users, get user command and excute the function
        """
        answer = ""
        print(
            """
            Please enter a command:
            \thome    \tTo show homepage
            \tpost    \tTo add a post
            \tprofile \tTo show a profile
            \tadd-f   \tTo add a friend
            \tshow-f  \tTo Show your friends
            \tshow-rf \tTo Show your friend requests
            \tlogout  \tTo logout
            """
        )

        answer = input("enter a command: ").lower()
        try:
            func = self.user_menu[answer]
        except KeyError:
            os.system("clear")
            print("--------------------------------------")
            print("{} is not a valid option".format(answer))
            print("--------------------------------------")
        else:
            if answer == "logout":
                self.username = func()
            else:
                func()


    def start(self):
        """
        Start the application
        """
        try:
            while True:
                if not self.username:
                    self.new_user()
                else:
                    self.logged_user()
        finally:
            os.system("clear")
            print("--------------------------------------")
            print("Thank you for using Consolo")
            print("--------------------------------------")
            time.sleep(2)
            os.system("clear")

  
if __name__ == '__main__':
    App().start()