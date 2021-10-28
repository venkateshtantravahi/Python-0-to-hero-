# app related urls
from django.urls import path

from . import views

urlpatterns = [
    path(
        "", views.index, name="all-meetups"
    ),  # the first argument will be the path after our domain like(our_domain.com/meetups)
    path(
        "<slug:meetup_slug>/success",
        views.confirm_registration,
        name="confirm-registration",
    ),
    path(
        "<slug:meetup_slug>", views.meetup_details, name="meetup-detail"
    ),  # out_domain.com/meetups/<meetup_slug>
]
