from user import User
from exceptions import *

class Authenticator:

    def __init__(self) -> None:
        """
        Construct an authenticator to manage users logging in and out.
        """
        self.users = {}
        self.emails = []


    def register(self, username, email, password):
        """
        Add new user to Application 

        Args:
            username: user's name used to login
            email   : user's email
            password: user's password will be encrypted
        
        Returns:
            True: If the registration is successful
        
        Raises:
            UsernameAlreadyExists: if the username already exists
            EmailAlreadyExists   : if the email already exists
            PasswordTooShort     : if the password too short 
        """

        if username in self.users:
            raise UsernameAlreadyExists(username)   
        elif email in self.emails:
            raise EmailAlreadyExists(email)
        elif len(password) < 6:
            raise PasswordTooShort(username)
        
        
        self.users[username] = User(username, email, password)        # Create user and add it to the users
        self.emails.append(email)                                     # Add email to uses emails

        return True
        

    def login(self, username, password):
        """
        Login to the app, check username and password befor logging
        
        Args:
            username: user's name used to login
            password: user's password will be encrypted
        
        Returns:
            True: If logged in successfully
        
        Raises:
            InvalidUsername: if the username is not valid
            InvalidPassword: if the password is not true
        """

        try:
            user = self.users[username]
        except:
            raise InvalidUsername(username)
        
        if not user.check_password(password):
            raise InvalidPassword(username, password)
        
        user.is_logged_in = True      # Update user state
        
        return True
    

    def is_logged_in(self, username):
        """
        Check if user logged in or not

        Args:
            username: user's name used to login
        
        Returns:
            True : if user logged in
            False: if not 
        """
        if username in self.users:
            return self.users[username].is_logged_in
        return False