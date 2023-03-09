from django.db import models

# Create your models here.
class WhyChooseUs(models.Model):
    whyImg = models.ImageField(upload_to= 'why_choose_us_img')
    whyName = models.CharField(max_length= 250)
    whyDes = models.TextField()

    def __str__(self):
        return self.whyName

class MeetTheTeamMembers(models.Model):
    memberImg = models.ImageField(upload_to= 'meet_the_team_members_img')
    memberName = models.CharField(max_length= 250)
    memberDes = models.TextField()

    def __str__(self):
        return self.memberName