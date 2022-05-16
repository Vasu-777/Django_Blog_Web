from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# from captcha.fields import CaptchaField

DEFAULT = 'profile_pics/default.jpg'

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    # captcha = CaptchaField()
    image=models.ImageField(upload_to='profile_pics',default=DEFAULT)
    skills=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    twitter=models.CharField(max_length=100,blank=True)
    facebook=models.CharField(max_length=100,blank=True)
    instagram=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    # def get_photo_url(self):
    #   if self.image and hasattr(self.image, 'url'):
    #         return self.image.url
    #   else:
    #     return "static/img/default.jpg"      


    def save(self,*args, **kwargs):
        super(Profile, self).save(*args, **kwargs) #parent's class save method

        img=Image.open(self.image.path)   
        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)#resize image
            img.save(self.image.path)