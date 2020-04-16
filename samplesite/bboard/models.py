from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save



#class Human(models.Model):
 #   user = models.OneToOneField(User, on_delete= models.CASCADE)

  #  def __str__(self):
   #     return self.user.username

#def create_profile(sender, **kwargs):
 #   if kwargs['created']:
  #      user_profile = Human.objects.create(user=kwargs['instance'])

#post_save.connect(create_profile, sender=User)




class JsonData(models.Model):
    AttributeName = models.CharField(max_length=50)
    AttributeID = models.CharField(max_length=50)
    AttributeContent = models.TextField(max_length=50, db_index=True)


   # def get_absolute_url(self):
  #      return reverse('Searching_detail_url',
      #                 kwargs={'AttributeName': self.AttributeName, 'AttributeID': self.AttributeID})

    def __str__(self):
        return '{}'.format(self.AttributeName)








