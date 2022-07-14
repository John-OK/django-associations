from django.db import models

# Users can make many posts and many comments
# Post can have one author (user), but many comments
# Comments can have one author (user) and belong to one post

# User to Post= 1:Many
# User to Comment= 1:Many
# Post to Comment= 1:Many


class User(models.Model):
    username = models.CharField(max_length=255)

# Since a user can have many posts, we'll have Post map to User with
# models.ForeignKey. 'User' is the first argument because that's what we're
# mapping to, and related_name will be the name of THIS model pluralized (i.e.,
# 'posts') If a User is deleted, all their posts will be deleted because we have the 'on_delete' argument set to 'CASCADE.'
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

# As wwith Post, comments can have many authors (users) and posts, so we'll Comment map to User and Post with foreign keys, give them related names and have all comments deleted when a User/Post is deleted.
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()


