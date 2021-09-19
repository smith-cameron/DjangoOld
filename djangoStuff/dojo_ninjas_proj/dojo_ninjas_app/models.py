from django.db import models

class Dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"<Dojo id:{self.id}, name:{self.name}, city:{self.city}, state:{self.state}, description:({self.desc})>"
class Ninjas(models.Model):
    dojo = models.ForeignKey(Dojos, related_name="ninja", on_delete = models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"<Ninja id:{self.id}, dojo:{self.dojo}, name:{self.first_name} {self.last_name}, created at:({self.created_at})>"