from django.db import models
'from django.contrib.auth.models import User'
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from django.conf import settings

from .customvalidators import validate_national_id





class Fields(models.Model):
    'This is the Major That Students Choose in The begining of The Enrolling'
    #Field Details
    name = models.CharField(max_length=20, unique=True)
    Field_id = models.CharField(max_length=4, unique=True)
    #Field Relations

    def __str__(self):
        return self.name

    class Meta:
         verbose_name = "Field"
         verbose_name_plural = "Fields"



class UserManager(BaseUserManager):
    
    def create_user(self, email, password=None, **extra_fields):
        'create and save New user'
        if not email:
            raise ValueError('User Must Have An Email Address')
        user = self.model(email= self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using= self._db)

        return user

    def create_superuser(self, email, password):
        'Creating SuperUser In Terminal'
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using= self._db)

        return user



class User(AbstractBaseUser, PermissionsMixin):
    'custom User Model to Support Email Instead of UserName'

    email = models.EmailField(max_length=255, unique= True)
    name = models.CharField(max_length=30)
    is_active = models.BooleanField(default= True)
    is_staff = models.BooleanField(default= False)
    'Extending Basic User to make extra field for students and teachers'
    #these are Basic User Detail Fields
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    National_id = models.CharField(max_length=10, validators=[validate_national_id])

    'Student Info'
    stu_id = models.CharField(max_length=10, blank=True, null=True)

    'these are Relations for Student'
    #this is relation to classes and is optional because the user can be teaacher
    ###stu_enrolled_classes = models.ManyToManyField(ClassHolding, related_name='students', blank=True, on_delete=models.CASCADE)
    #this is relation to main Fields that Student is studing and is optional because the user can be teacher
    choosed_topics = models.ForeignKey(Fields, related_name='students', on_delete=models.CASCADE, null=True, blank=True)

    'Teacher Fields'
    prof_id = models.CharField(max_length=10, blank=True, null=True)

    'Teacher Relations Fields'

    'General Fields'
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_teacher = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def get_short_name(self):
        # The user is identified by their email address
        return self.email





class PhysicalClass(models.Model):
    'This is The Physical Classes Info'
    #Location Details
    class_Location_id = models.CharField(max_length=5, unique=True)
    is_smart_class = models.BooleanField(default=False)
    capacity = models.CharField(max_length=3)
    #Location Relations

    def __str__(self):
        return self.class_Location_id

    class Meta:
         verbose_name = "Location"
         verbose_name_plural = "Locations"




class Topics(models.Model):
    'Topics(Lessons) in the Fields'
    name = models.CharField(max_length=20, unique=True)
    Topic_id = models.CharField(max_length=4, unique=True)
    'Topics Relations'
    #each Topic(lesson) Blongs to one Field
    topic = models.ForeignKey(Fields, on_delete=models.CASCADE, related_name='topics')

    def __str__(self):
        return self.name

    class Meta:
         verbose_name = "Topic"
         verbose_name_plural = "Topics"


class ClassHolding(models.Model):
    'Integrate The Location And Topic And Teacher And Students use it to take Classes'
    is_class_active = models.BooleanField(default=True)
    is_class_online = models.BooleanField(default=False)
    classh_id = models.CharField(max_length=6)

    'Class relations'
    #each class can only have one teacher
    stu_enrolled_classes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='enrolled_classes', blank=True)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='classes')
    Location = models.ForeignKey(PhysicalClass, on_delete=models.CASCADE, related_name='classes')
    field = models.ForeignKey(Fields, on_delete=models.CASCADE, related_name='classes')

    class Meta:
         verbose_name = "Class"
         verbose_name_plural = "Classes"

    
    
