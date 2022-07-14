from django.db import models

# We want to associate Movies and Actors:
# - Movies can have many actors
# - Actors can be in many movies
# - One, and ONLY one of these models will be used to associate to the other.
# I prefer to use Actor to associate to Movie because they are a part of the movie, but it works either way.
class Movie(models.Model):
    title = models.CharField(max_length=255, default="")

class Actor(models.Model):
    name = models.CharField(max_length=255, default="")

    # - Associate Actor to Movie with "models.ManyToManyFiled".
    # - "related_name" is how the related model will refer to this model (i.e.,
    # how Movie will refer to Actor).
    # - Usually, you name the related_name with the plural of its model name.
    # - If you don't use realted_name, test4 fails when it looks for all the
    # movie's actors "using movie.actors.all()" with "Attribute Error: 'Movie'
    # object has no attribute 'actors'," but this is just because the test was
    # written expecting that 'actors' would be used as a related_name instead
    # of the Django-provided default, 'actor_set' (so use
    # "related_name='actors'" to pass the test).
    # You need 'through='Role' in order to join the Move and Actor tables
    # through the Role table, otherwise Django will create it's own throug
    # table.
    movies = models.ManyToManyField(Movie, through='Role', related_name='actors')


class Role(models.Model):
    # - As above, you need "related_name='roles'" because the test expects it
    # (and it is easier/nicer this way, but not required)
    # Both Actor and Movie will each get an attribute called 'roles' to refer
    # to the Role model.
    # The ForeignKeys make a one-to-many relationship between Role and Actor,
    # and Role and Movie.
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='roles')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='roles')