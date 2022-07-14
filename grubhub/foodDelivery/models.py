from django.db import models

# From docs:
# A user has many orders
# An order belongs to a user
# A restaurant has many orders
# An order belongs to a restaurant
# An order has many order_food_items
# An order_food_item belongs to an order
# A food item has many order_food_items
# An order_food_item belongs to a food_item
# And finally if you have set up your associations correctly a user should have many food items through orders.

# The docs don't specify, but it seems like an order can have many food items,
# and food items can be in many orders, so we have a many-to-many relationship
# that will be joined through OrderFoodItem.

class User(models.Model):
    pass

class Restaurant(models.Model):
    pass

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name=
    'orders')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name=
    'orders')

class FoodItem(models.Model):
    orders = models.ManyToManyField(Order, through='OrderFoodItem', related_name='food_items')

class OrderFoodItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name=
    'order_food_items')
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE, related_name=
    'order_food_items')