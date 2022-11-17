import os
from datetime import datetime
from exceptions import *

class Post:
    def __init__(self, subject, body, username) -> None:
        """
        Construct a Post

        Args:
            subject: post subject
            body   : post body
        """
        self.subject = subject
        self.body = body
        self.date = datetime.now()
        self.owner = username

    def __lt__(self, other):
         """
         Define less than to sort posts according to post date
         """
         return self.date < other.date

    def show_post(self):
        """
        Show the post
        """
        print("-----------------------------")
        print("Subject: {}".format(self.subject))
        print("-------- ")
        print(self.body)
    
    
class AddPost:
    def __init__(self, username, authorizor, authenticator) -> None:
        """
        Create Adapter to add posts

        Args:
            username: namd of the user who will add the post
            authorizor: authorizor will manage permissions
            authenticator: authenticator will manage users
        """
        self.username = username
        self.authorizor = authorizor
        self.authenticator = authenticator

    def post(self):
        """
        Create Post and check if the post added successfully

        Raises:
            NotLoggedInError: If the user isn't logged in
            PermissionError : If permission doesn't exists
        """
        os.system("clear")
        subject = input("Enter the subject: ")
        body    = input("Enter post body  : ")
        post    = Post(subject, body, self.username)

        try:
            self.authorizor.check_permission("add post", self.username)
            self.authenticator.users[self.username].posts.append(post)
            os.system("clear")
            print("-----------------------------")
            print("Your post added successfully")
            print("-----------------------------")
            
        except NotLoggedInError:
            print("You should login first")
        except PermissionError:
            print("You don't have the permission to add post")