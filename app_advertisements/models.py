from django.db import models
class Advertisement(models.Model):
    title = models.CharField("заголовок", max_length= 128)
    description = models.TextField("описание")
    price = models.DecimalField("цена", max_digits=10,decimal_places=2)
    auction = models.BooleanField("торг", help_text=" поставьте галочку, если торг уместен ")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title



# Create your models her