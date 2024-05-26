from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Worker(models.Model):
    name = models.CharField(verbose_name="Mentor Name", max_length=25)
    surname = models.CharField(verbose_name="Mentor Surname", max_length=25)
    technology = models.CharField(verbose_name="Mentor Teach Technology", max_length=50)
    image = models.ImageField(verbose_name="Workers Image", upload_to="image_workers")
    image1 = models.ImageField(verbose_name="Workers Hover Image" , upload_to="hover_image_workers")
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.surname} - {self.technology} ({self.reg_date:%Y-%m-%d})"

    class Meta:
        verbose_name = "Worker"
        verbose_name_plural = "Workers"


class VideoChoice(models.Model):
    name = models.CharField(verbose_name="Name Choice", max_length=80)
    video = models.FileField(verbose_name="Video Choice", upload_to="video_choice_we")
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Video Choice"
        verbose_name_plural = "Video Choices"


class RegisterStudent(models.Model):
    field_of_study = models.CharField(
        verbose_name="Field Of Study",
        max_length=588
    )
    name = models.CharField(verbose_name="Student Name", max_length=20)
    phone_number = models.IntegerField(verbose_name="Student Phone Number")
    age = models.IntegerField(
        validators=[
            MinValueValidator(limit_value=9),
            MaxValueValidator(limit_value=30)
        ]
    )
    status = models.BooleanField(verbose_name="Student Status", default=False)
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.field_of_study})"

    class Meta:
        verbose_name = "Register Student"
        verbose_name_plural = "Register Students"


class FAQ(models.Model):
    title = models.CharField(verbose_name="FAQ Title", max_length=250)
    answer = models.TextField(verbose_name="FAQ Answer")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"


class Sponsor(models.Model):
    image = models.ImageField(verbose_name="Sponsor Image", upload_to="sponsor_image")

    def __str__(self):
        return f"Sponsor {self.id}"

    class Meta:
        verbose_name = "Sponsor"
        verbose_name_plural = "Sponsors"
        
class Consulting(models.Model):
    name = models.CharField(verbose_name="Name Student: " , max_length=50)
    phone = models.IntegerField(verbose_name="Phone Number: ")
    age = models.IntegerField(verbose_name="Age: ")
    reg_date = models.DateField(auto_now_add = True)
    
    def __str__(self) -> str:
        return f"{self.name}{self.phone}{self.reg_date}"
    
    class Meta:
        verbose_name = "Consulting"
        verbose_name_plural = "Consulting's"
        
        
class OurVideo(models.Model):
    video = models.TextField(verbose_name="OurVideo")