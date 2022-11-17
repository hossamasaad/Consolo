import os

class Home:
    """
    Construct Home class to build home page for user
    """

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
        self.user = self.authenticator.users[username]

    def load_posts(self):
        """
        Load user and his friends posts to load it in home page
        
        Returns:
            posts: user and his friends posts sorted according to post date
        """
        posts = []
        friends = self.user.friends

        for post in self.user.posts:
            posts.append(post)

        for friend in friends:
            for post in friend.posts:
                posts.append(post)
        
        posts.sort(reverse=True)
        
        return posts
    
    def show_homepage(self):
        """
        Show Home Page to user
        """
        self.posts = self.load_posts()
        os.system("clear")
        print("====================================================")
        print("\t\t   Home Page")
        print("====================================================\n")

        for post in self.posts:
            print("{} posted {} on {}".format(post.owner, post.subject, post.date.date()))
            print("---")
            print(post.body)
            print("----------------------------------------------------")

