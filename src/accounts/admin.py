from django.contrib import admin

# Register your models here.
from accounts.models import *

admin.site.register(User)
admin.site.register(Space)
admin.site.register(InterestedSpace)
admin.site.register(Amenity)
admin.site.register(Arrangement)
admin.site.register(SpaceNetwork)
admin.site.register(IsNetworkMember)
admin.site.register(Comment)
admin.site.register(IsFriends)
admin.site.register(Picture)
admin.site.register(SpaceReview)
admin.site.register(Synergy)
admin.site.register(SynergyMember)
admin.site.register(UserReview)