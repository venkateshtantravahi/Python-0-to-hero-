from django.contrib import admin

from .models import Meetup, Location, Participant, Organizers

# Register your models here.


class MeetupAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "description")
    list_filter = ("location", "date")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)
admin.site.register(Organizers)
