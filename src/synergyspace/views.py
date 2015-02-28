from django.views import generic
from accounts.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class HomePage(generic.TemplateView):
    template_name = "browse.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"

class ReviewBooking(generic.TemplateView):
    template_name = "review_booking.html"
    
class BrowsePage(generic.ListView):
    model = Space
    template_name = "browse.html"
    