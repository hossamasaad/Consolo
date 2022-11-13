import os
from exceptions import *

class Profile:

    def __init__(self, user) -> None:
        """
        Construct user profile 

        Args:
            user: user we will create his profile
        """
        self.user = user
    
    def show_profile(self):
        """
        Show the profile of the user
        """
        os.system('clear')
        print("---------------------------------------------")
        print("Profile:")
        print("---------------------------------------------")
        print("Name : {}". format(self.user.username))
        print("email: {}". format(self.user.email   ))
        print("---------------------------------------------")
        print("Posts: ")
        for post in self.user.posts:
            post.show_post()


class ShowProfile:

    def __init__(self, username, authorizor, authenticator) -> None:
        """
        Create Adapter to show user profile
        
        Args:
            username: name of the user who will show his profile
            authorizor: authorizor will manage permissions
            authenticator: authenticator will manage users
        """
        self.username = username
        self.authorizor = authorizor
        self.authenticator = authenticator

    def show(self):
        """
        Show the profile and check if the user valid

        Raises:
            NotLoggedInError: If the user isn't logged in
            PermissionError : If permission doesn't exists
        """
        try:
            self.authorizor.check_permission("show profile", self.username)
            prof = Profile(self.authenticator.users[self.username])
            prof.show_profile()
        except NotLoggedInError:
            print("You should login first")
        except PermissionError:
            print("You don't have the permission to add post")