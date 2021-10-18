from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name} ({self.address})'


class Participant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Organizers(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Meetup(models.Model):
    title = models.CharField(max_length=200)
    organizers_email = models.ForeignKey(Organizers, on_delete=models.SET('dummy@gmail.com'))
    date = models.DateField()
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)  #what happens is when related record in location table get deleted our meetup will also get deleted and foreign key is used for one-to-many relationship
    participants = models.ManyToManyField(Participant, blank=True, null=True) # this blank will ensure that you may or may not needed to add this field compulsory

    def __str__(self):
        return f'{self.title} - {self.slug} - {self.description}'