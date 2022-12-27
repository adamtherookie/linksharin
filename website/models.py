from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  pass

class Page(models.Model):
  user = models.CharField(max_length=600)
  pic = models.ImageField(upload_to='images', default='images/default.png')
  bio = models.CharField(max_length=10000)
  background = models.ImageField(upload_to='images', null=True, blank=True, default=None)
  watermark = models.BooleanField(default=True)
  colorscheme = models.CharField(max_length=100, default='default')
  effect = models.CharField(max_length=100, default='raise')
  font = models.CharField(max_length=100, default='karla')

  def __str__(self):
    return f"{self.user}'s page"

class Category(models.Model):
  name = models.CharField(max_length=600)
  page = models.ForeignKey(Page, on_delete=models.CASCADE)

  def __str__(self):
    return f"Category {self.name} on page {self.page}"

class Link(models.Model):
  name = models.CharField(max_length=600)
  url = models.CharField(max_length=600)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  page = models.ForeignKey(Page, on_delete=models.CASCADE)

  def __str__(self):
    return f"Link with name {self.name} and url {self.url} on {self.category}"

class Style(models.Model):
  page = models.ForeignKey(Page, on_delete=models.CASCADE)
  css = models.CharField(max_length=1000000)

  def __str__(self):
    return f"Stylesheet {self.css} on {self.page}"

class Colorscheme(models.Model):
  # This is just to keep track of the colorschemes we have.
  # Only admins will be able to add them through the admin portal
  name = models.CharField(max_length=100)

  def __str__(self):
    return f"Colorscheme {self.name}"

class Effect(models.Model):
  # Same as colorschemes
  name = models.CharField(max_length=100)

  def __str__(self):
    return f"Effect {self.name}"

class Font(models.Model):
  # Same as colorscheme (again (:)
  name = models.CharField(max_length=100)

  def __str__(self):
    return f"Font {self.name}"

class View(models.Model):
  date = models.DateField()
  page = models.ForeignKey(Page, on_delete=models.CASCADE)

  def __str__(self):
    return f"View on {self.page} on {self.date}"

