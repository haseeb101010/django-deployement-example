from django.db import models

# SuperUserInformation
# User: Jose
# Email: training@pieriandata.com
# Password: testpassword

# CREATE SOME TEST DATA WITH SOME SHELL COMMANDS:

# python manage.py shell

# from first_app.models import Topic
# print(Topic.objects.all())
# t = Topic(top_name="Social Network")
# t.save()
# print(Topic.objects.all())
# quit()

class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique=True, default='DEFAULT VALUE')

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    #topic = models.ForeignKey(Topic)
    topic = models.ForeignKey(Topic, models.CASCADE, related_name='topics')
    name = models.CharField(max_length=264,unique=True, default='DEFAULT VALUE')
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    #name = models.ForeignKey(Webpage)
    name = models.ForeignKey(Webpage, models.CASCADE, related_name='topics')
    date = models.DateField()

    def __str__(self):
        return str(self.date)

class Onemore(models.Model):
    name = models.ForeignKey(AccessRecord, models.CASCADE, related_name='topics')
    ratings = models.DateField()

    def __str__(self):
        return (self.ratings)
