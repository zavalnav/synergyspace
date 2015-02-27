from django.db import models

# Commenting out all the "primary keys" for now, because Django automatically
# REMAINING TODO:
# -Add __str__ methods for any models that are missing them


class User(models.Model):
    MALE = 'm'
    FEMALE = 'f'
    GENDER_CHOICES = ((MALE, 'Male'), (FEMALE, 'Female'))
    
    #user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20,null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=1, 
                              choices=GENDER_CHOICES,
                              default=MALE)
    location = models.CharField(max_length=40,null=True, blank=True)
    email = models.CharField(max_length=40,null=True, blank=True)
    rating = models.FloatField()
    
    def __str__(self):
        return self.user_name
    
    class Meta:
        unique_together = (("user_name", "password"),)


class InterestedSpace(models.Model):
    # interested_space_id = models.IntegerField(primary_key=True)
    user_id = models.OneToOneField(User)
    space_id = models.ForeignKey('Space')
    leasing = models.BooleanField(default=True)
    renting = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.id)
        
    class Meta:
        unique_together = (("user_id", "space_id"),)
  
  
class Space(models.Model):
    #space_id = models.IntegerField(primary_key=True)
    owner_id = models.ForeignKey(User)
    space_name = models.CharField(max_length=20)
    # network_id = TODO: IMPLEMENT ONETOONEFIELD HERE
    address = models.TextField()
    description = models.TextField()
    price = models.FloatField()
    # TODO: Create choices for space types according to our design
    space_type = models.CharField(max_length=20)
    rules = models.TextField()
    total_spaces = models.IntegerField()
    
    def __str__(self):
        return self.space_name
    
    class Meta:
        unique_together = (("id","owner_id"),)
        
 
class Amenity(models.Model):
    WIFI = 'w'
    VENDING_MACHINE = 'v'
    COFFEE = 'c'
    KITCHEN = 'k'
    AMENITY_LIST = ((WIFI, 'Wi-Fi'), (VENDING_MACHINE, 'Vending Machine'),
                     (COFFEE, 'Coffee'), (KITCHEN, 'Kitchen'))
    
    space_id = models.ForeignKey(Space)
    amenity = models.CharField(choices=AMENITY_LIST, max_length=3)
    
    def __str__(self):
        return str(self.space_id) + " " + self.amenity
        
    class Meta:
        unique_together = (("space_id","amenity"),)
    
    
class Arrangement(models.Model):
    space_id = models.ForeignKey(Space) # Should this be ManyToMany?????
    user_id = models.ForeignKey(User) # Should this be ManyToMany?????
    start_date = models.DateField(auto_now_add=True, editable=True)
    end_date = models.DateField()
    cost = models.FloatField()
    accepted = models.BooleanField(default=False)
    
    
class SpaceNetwork(models.Model):
    space_id = models.OneToOneField(Space)
    
    def __str__(self):
        return str(self.space_id.space_name) + " network"

    class Meta:
        unique_together = (("space_id","id"),)
    
    
# Relation that shows which users are in the space network
class IsNetworkMember(models.Model):
    network_id = models.ForeignKey(SpaceNetwork) # Should this be ManyToMany??
    user_id = models.ForeignKey(User) # Should this be ManyToMany??
    
    def __str__(self):
        return str(self.network_id) + " " + str(self.user_id)
    
    class Meta:
        unique_together = (("network_id","user_id"),)
        

class Comment(models.Model):
    comment = models.TextField()
    network_id = models.ForeignKey(SpaceNetwork)


class IsFriends(models.Model):
    # idk why adding the related name fixes the problem but i think
    # it's to make sure that there won't be clashes from getting rows from
    # the same table 
    user_id = models.ForeignKey(User, related_name="user_id")
    friend_id = models.ForeignKey(User, related_name="friend_id")
    
    class Meta:
        unique_together = (("friend_id","user_id"),)
    
    def __str__(self):
        return str(self.user_id) + " + " + str(self.user_id) 


class Picture(models.Model):
    space_id = models.ForeignKey(Space)
    photo_url = models.CharField(max_length = 40)
    # picture = models.ImageField(upload_to='profile_images', blank=True)
    # ^ better way to do it

    
    
class SpaceReview(models.Model):
    space_id = models.ForeignKey(Space)
    user_id = models.ForeignKey(User)
    date = models.DateField(auto_now_add=True)
    text = models.TextField()
    rating = models.FloatField()
    
    class Meta:
        unique_together = (("space_id","user_id","date"),)
    
    
class Synergy(models.Model):
    user_id = models.ForeignKey(User)
    network_id = models.OneToOneField(SpaceNetwork)
    title = models.CharField(max_length = 40)
    description = models.TextField()


class SynergyMember(models.Model):
    synergy_id = models.ForeignKey(Synergy)
    member_id = models.ForeignKey(User)
    
    class Meta:
        unique_together = (("synergy_id","member_id"),)


class UserReview(models.Model):
    reviewer_id = models.ForeignKey(User, related_name = 'reviewer')
    user_id = models.ForeignKey(User, related_name = 'reviewee')
    date = models.DateField(auto_now_add=True)
    text = models.TextField()
    rating = models.FloatField()

    class Meta:
        unique_together = (("reviewer_id","user_id","date"),)