from django.db import models

# Create your models here.

# This app is basically to be used to learn and try
# stuff from the django book.
# These models will be run in the console


class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ("title",)


class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, null=True)

    def __unicode__(self):
        return self.headline

    class Meta:
        ordering = ("headline",)
