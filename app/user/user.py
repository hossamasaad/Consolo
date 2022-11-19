import time
import os
import hashlib
from app.exceptions import *

class User:

    def __init__(self, username, email, password) -> None:
        """
        Construct User will manage all users proprites

        Args:
            username: user's name used to login
            email   : user's email
            password: user's password will be encrypted
        """
        self.username = username
        self.email = email
        self.password = self._encrypt_password(password)
        self.posts = []
        self.friends = set()
        self.friend_requests = set()
        self.is_logged_in = False
    
    def _encrypt_password(self, password):
        """
        Encrypt the password with the username and return the sha digest.

        Return:
            Encrupted password
        """
        hash_string = self.username + password
        hash_string = hash_string.encode('utf-8')
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        """
        Check if the password true
        Returns:
            True : If the password is valid for this user
            False: Otherwise.
        """
        encrypted = self._encrypt_password(password)
        return encrypted == self.password


class Login:
    
    def __init__(self, authorizor, authenticator) -> None:
        """
        Create a Login state used when user logging

        Args:
            authorizor: authorizor will manage permissions
            authenticator: authenticator will manage users
        """
        self.authorizor = authorizor
        self.authenticator = authenticator
    
    def login(self):
        """
        login

        Returns:
            username: the username of the registered user            
        """
        logged_in = False
        while not logged_in:
            username = input("username: ")
            password = input("password: ")
            try:
                logged_in = self.authenticator.login(username, password)
            except InvalidUsername:
                print("Sorry, that username does not exist")
            except InvalidPassword:
                print("Sorry, incorrect password")
            else:
                os.system('clear')
                print("-----------------------------")
                print("You Logged in successfully")
                print("-----------------------------")
                time.sleep(2)
                return username


class Register:
    def __init__(self, authorizor, authenticator) -> None:
        """
        Create a Register state used when user registering
        
        Args:
            authorizor: authorizor will manage permissions
            authenticator: authenticator will manage users
        """
        self.authorizor = authorizor
        self.authenticator = authenticator
        self.permissions = ["add post", "add friend", "show home", "show profile", "send message"]

    def register(self):
        """
        Register a user
        """
        registerd = False
        while not registerd:
            username = input("username: ")
            email    = input("Email   : ")
            password = input("Password: ") 

            try:
                registerd = self.authenticator.register(username, email, password)
                for perm in self.permissions:
                    self.authorizor.permit_user(perm, username)

            except UsernameAlreadyExists:
                print("Sorry, This username already exists")
            except EmailAlreadyExists:
                print("Sorry, This email already exists")
            except PasswordTooShort:
                print("The password is too short")
            else:
                os.system('clear')
                print("-----------------------------")
                print("You registered successfully")
                print("-----------------------------")
                time.sleep(2)


class Logout:
    def __init__(self, username, authorizor, authenticator) -> None:
        """
        Create a Logout state used when user log out

        Args:
            authorizor: authorizor will manage permissions
            authenticator: authenticator will manage users
        """
        self.authorizor = authorizor
        self.authenticator = authenticator
        self.username = username
    
    def logout(self):
        """
        logout        
        """
        user = self.authenticator.users[self.username]

        try:
            self.authorizor.check_permission("logout", self.username)
        except PermissionError:
            os.system("clear")
            print("-----------------------------------------")
            print("You don't have the permission to logout")
            print("-----------------------------------------")
            time.sleep(2)
            return self.username
        else:
            user.is_logged_in = False
            os.system('clear')
            print("-----------------------------")
            print("You Logged out successfully")
            print("-----------------------------")
            time.sleep(2)