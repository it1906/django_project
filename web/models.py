from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

def attachment_path(instance, filename):
    return "foods/"+str(instance.recipe.id)+"/attachments/"+filename
def picture_path(instance, filename):
    return "foods/"+str(instance.id)+"/pictures/"+filename

class Foodstuff(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Foodstuff name")
    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    foodstuff = models.ManyToManyField(Foodstuff, help_text='Select your foodstuff')
    kcal = models.CharField(max_length=10, verbose_name="Kcal")
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    picture = models.ImageField(upload_to=picture_path, blank= True, null = True, verbose_name="Picture")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}, kcal: {str(self.kcal)}"

    def get_absolute_url(self):
        return reverse('recipe-detail',args=[str(self.id)])

class Attachment(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    last_update = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to=attachment_path, null=True,verbose_name="File")
    TYPE_OF_ATTACHMENT = (
        ('audio', 'Audio'),
        ('image', 'Image'),
        ('text', 'Text'),
        ('video', 'Video'),
        ('other', 'Other'),
    )
    type = models.CharField(max_length=5, choices=TYPE_OF_ATTACHMENT, blank=True, default='image', verbose_name="Attachment type")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    class Meta:
        ordering= ["-last_update","type"]

    def __str__(self):
        return f"{self.name},({self.type})"