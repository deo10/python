# example of the class inheritance + super to create class object

class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email
        

class AdminUser(User):
    def __init__(self, username: str, email: str, role: str):
        super().__init__(username, email) # using super to create object User
        self.role = role
        self.is_admin = True
        
class Post:
    def __init__(self, title: str, content: str, author: User):
        self.title = title
        self.content = content       
        self.author = author

class Forum:
    def __init__(self):
        self.users = [] # create empty lists to capture results
        self.posts = []
        
    def register_user(self, username: str, email: str):
        user = User(username, email) # creating instance of User class
        self.users.append(user) # adding new user into list
        return user
        
    def create_post(self, title: str, content: str, author: User):
        post = Post(title, content, author) # creating instance of Post class
        self.posts.append(post) # adding new post into list
        return post
    
    def find_user_by_username(self, username: str):
        for user in self.users:
            if user.username == username:
               return user 
    
    def find_user_by_email(self, email: str):
        for user in self.users: 
            if user.email == email:
                return user
    
    def find_posts_by_author(self, author: User): # getting link on instance of the user
        found_posts = [] #creating empty list
        for post in self.posts: # looking post with condition
            if post.author == author:
                found_posts.append(post) # adding post into new list
        return found_posts
    
    
    def delete_user(self, author: User):
        user_to_delete = self.find_user_by_username(username)
        if user_to_delete:
            self.users.remove(user_to_delete)
            posts_to_delete = self.find_posts_by_author(user_to_delete)
            for post in posts_to_delete:
                self.posts.remove(post)
            return True
        return False

    def delete_post(self, title: str):
        for post in self.posts:
            if post.title == title:
                self.posts.remove(post)
                return True
        return False

    
        
#creating Forum (no atributes required)
forum = Forum()

# creating new user
andrei = forum.register_user('Andrei', 'email@email.com')
alice = forum.register_user('Alicei', 'alice@email.com')
print(forum.users)
print(andrei.__dict__)
# {'username': 'Andrei', 'email': 'email@email.com'}

#creating post using registered user
post1 = forum.create_post("my first post", 'post content', andrei)
forum.create_post("my second post", 'post content', andrei)

print(post1.__dict__)        
# {'title': 'my first post', 'content': 'post content', 'author': <__main__.User object at 0x0000025225A17770>}

# not recommended way to search - use function forum.find_by_...
print(forum.posts[0].__dict__)
# {'title': 'my first post', 'content': 'post content', 'author': <__main__.User object at 0x00000213C2F277A0>}
print(forum.posts[0].title) # getting by index
# my first post
print(forum.posts[0].content)
# post content
print(forum.posts[0].author.username) # as user(author) is an object of user that has own attributes
# Andrei
print(forum.posts[0].author.email)
# email@email.com


#find user
print(forum.find_user_by_username('Kolya'))
# None
print(forum.find_user_by_username('Andrei'))
# <__main__.User object at 0x000001FFDF858170>
print(forum.find_user_by_username('Andrei').__dict__)
# {'username': 'Andrei', 'email': 'email@email.com'}
print(forum.find_user_by_username('Andrei').email)
# email@email.com


#find post by user
print(forum.find_posts_by_author(andrei))
# [<__main__.Post object at 0x000001B9B6ABD070>, <__main__.Post object at 0x000001B9B6ABD0A0>]

# getting titles of all found posts
found_posts = forum.find_posts_by_author(andrei)

found_post_titles = [post.title for post in found_posts]
print(found_post_titles)
# ['my first post', 'my second post']


#find post by email

user_email = 'email@email.com'
found_user = forum.find_user_by_email(user_email)
if found_user:
    print(forum.find_posts_by_author(found_user))
else:
    print(f"User with email {user_email} doesn't exist!")
# [<__main__.Post object at 0x000002283718D310>, <__main__.Post object at 0x000002283718D340>]


# delete user
forum.delete_user('Alicei')
print(forum.users)


# delete post
forum.delete_post("my second post")
print(forum.posts)