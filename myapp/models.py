from django.db import models

# Create your models here.
#https://rohitlakhotia.com/blog/django-custom-user-model/
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
    ('N', 'Not Specified')
]

BLOOD_GROUP_CHOICES = [
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
    ('UNKNOWN', 'Unknown'),
]

RIDE_CHOICES = [
    ("Route 1","Abdullahpur -> House Building -> Azampur -> Airport -> Kawla -> Khilkhet -> Biswa Road -> Shewrah -> BRAC University"),
    ("Route 2", "Kallyanpur -> Tolarbag -> Sony-Cinema -> Mirpur-College -> Swimming-Fed -> Popular-diag. -> Pallabi -> Bonolata-shop -> Mirpur-ceramic -> Pallabi-thana -> Kalshi -> ECB -> BRAC University"),
    ("Route 3","Jigatola -> Shankar -> Mohammadpur -> Manik Mia Ave. -> BRAC University"),
    ("Route 4","Azimpur-etim-khana -> Azimpur Chowrasta -> New Market -> Happy Arcade -> Dhanmondi -> Kalabagan Krira -> Sobhanbag -> Manik Mia Ave -> Khejur Bagan -> BRAC University"),
    ("Route 5","Jatrabari -> Doyaganj Mour -> Ittefaq Mour -> Mugda -> Bouddha Mandir -> Bashabo -> Khidmah hospital -> Malibag Railgate -> Abul Hotel -> Rampura TV Center -> BRAC University"),
    ("Route 6","Baldha Garden -> Motijheel -> Arambag -> Fakirapul -> Purana Palton -> Kakrail -> Shantinagar -> Malibag -> Mouchak -> Mogbazar TNT office -> Mogbazar Mour -> BRAC University"),
]



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)   
    name =  models.CharField(null=True,blank=True, max_length=200, default="None")
    profile_pic = models.ImageField(default='default.jpg', upload_to='profiles_pics')
    hobby = models.CharField(null=True,blank=True, max_length=200, default='N')
    skills = models.CharField(null=True,blank=True, max_length=200, default='N')
    department = models.CharField(null=True,blank=True, max_length=200, default='N')
    blood_group = models.CharField(null=True,blank=True,max_length=200, choices=BLOOD_GROUP_CHOICES, default='UNKNOWN')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='N')
    role = models.CharField(null=True,blank=True, max_length=200, default='Student')    
    student_id = models.CharField(null=True,blank=True, max_length=200, default='N')
    is_active = models.BooleanField(default=False)
    profession = models.CharField(null=True,blank=True, max_length=200, default='N')
    

    room_no = models.CharField(null=True,blank=True, max_length=200, default='N')
    research_interest = models.CharField(null=True,blank=True, max_length=200, default='N')
    current_city = models.CharField(null=True,blank=True, max_length=200, default='N')

    gsuiteEmail = models.CharField(null=True,blank=True, max_length=200, default='N')
    projects = models.CharField(null=True,blank=True,max_length=200, default='N')
    school = models.CharField(null=True,blank=True, max_length=200, default='N')
    college = models.CharField(null=True,blank=True, max_length=200, default='N')
    university = models.CharField(null=True,blank=True, max_length=200, default='BRAC University')
    publication = models.CharField(null=True,blank=True, max_length=200, default='N')
    clubs = models.CharField(null=True,blank=True, max_length=200, default='N')
    courses = models.CharField(null=True,blank=True, max_length=200, default='N')
    facinitial = models.CharField(null=True,blank=True, max_length=200, default='N')
    msc = models.CharField(null=True,blank=True, max_length=200, default='N')
    phd = models.CharField(null=True,blank=True, max_length=200, default='N')
    bsc = models.CharField(null=True,blank=True, max_length=200, default='N')
    bio = models.CharField(null=True,blank=True, max_length=200, default='N')
    certifications = models.CharField(null=True,blank=True, max_length=400, default='N')
    phone = models.CharField(null=True,blank=True, max_length=200, default='N')

    travel_route = models.CharField(null=True,blank=True, max_length=400, default='N', choices=RIDE_CHOICES)

    def research_interest_as_list(self):
        return self.research_interest.split(',')
    def skills_listed(self):
        return self.skills.split(',')
    def publication_listed(self):
        return self.publication.split(',')
    def project_listed(self):
        return self.projects.split(',')
    def course_listed(self):
        return self.courses.split(',')
    def club_listed(self):
        return self.clubs.split(',')
    def certifications_listed(self):
        return self.certifications.split(',')
    def current_city_listed(self):
        items = self.current_city.split(',')
        var = ",\n ".join(items)
        print(var)
        return var

    def __str__(self):
        return self.name
    

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    instance.user.delete()

@receiver(post_save, sender=User)
def activate_profile(sender, instance, created, **kwargs):
    if not created and instance.is_active:
        instance.profile.is_active = True
        instance.profile.save()



class Notification(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sent_notifications')
    recipient = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='received_notifications')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sender.name} requested a ride with {self.recipient.name}" 