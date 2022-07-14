from django.db import models

# Based on the tests:
# Shop to User (owner)= 1:1
# Shop to Product= 1:Many
# Product to Review= 1:Many
# Review to User (author)= 1:1 (really M:1, but there are no tests for this)

# I had the User model defined last and got the error, "NameError: name 'User'
# is not defined". So I had to move the User class above any model that used
# User as an FK.
class User(models.Model):
    username = models.CharField(max_length=255)

# Although an owner is an element of a shop and not really the other way around,
# if we delete a shop, we may not want to delete the owner, but if we delete
# an owner, we probably want to delete the shop, so we'll use Shop to associate
# to the owner with a ForeignKey.
class Shop(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shop')

# A product is an element of a shop, and if the shop is deleted, we'll want to
# delete the products, so our FK will go here.
class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='products')

# A review is an element of a product, and we'll delete the reviews if a product
# is deleted, so our FK will go here.
# An author (user) is an element of a review, but if we delete an author, we'll
# want to delete the review, so we'll put the FK here.
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')