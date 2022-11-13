from exceptions import *

class Authorizor:
    
    def __init__(self, authenticator) -> None:
        """
        Construct an authorizor to manage users permissions.

        Args:
            authenticator: Authenticator will be managed
        """

        self.authenticator = authenticator
        self.permissions = {}
    
    def add_permission(self, perm_name):
        """
        Create a new permission that users can be added to

        Args:
            perm_name: new permission can add user to it
        
        Raises:
            PermissionError: if permission already exists
        """
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            self.permissions[perm_name] = set()
        else:
            raise PermissionError("Permission Exists")
    
    
    def permit_user(self, perm_name, username):
        """
        Grant the given permission to the user

        Args:
            perm_name: permission will be added to the user

        Raises:
            PermissionError: If permission doesn't exists
            InvalidUsername: If the username isn't valid
        """
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in self.authenticator.users:
                raise InvalidUsername(username)

        perm_set.add(username)


    def check_permission(self, perm_name, username):
        """
        Check if the user has this permission

        Args:
            perm_name: permission will be checked
            username : the user we will check if he has the permission
        
        Returns:
            True: If user has the permission

        Raises:
            NotLoggedInError  : If the user isn't logged in
            PermissionError   : If permission doesn't exists
            NotPermittedError : If the user doesn't have the permission
        """
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedInError(username)
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in perm_set:
                raise NotPermittedError(username)
            else:
                return True