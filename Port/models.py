from django.db import models

# Create your models here.


class Logo(models.Model):
    src = models.ImageField(upload_to="Port/logo", default="default.jpg", null=True, blank=True)
    
    def __str__(self):
        return str(self.src)

class Hero(models.Model):
    title=models.CharField(max_length=30)
    sub_title=models.CharField(max_length=30)
    desc=models.CharField(max_length=300,null=True, blank=True)
    image = models.ImageField(upload_to="Port/hero", default="default.jpg", null=True, blank=True)  
    
    def __str__(self):
        return self.title
    

class About(models.Model):
     
     desc=models.CharField(max_length=300,null=True, blank=True)
     Projects=models.IntegerField(blank=True)
     experience=models.IntegerField(blank=True)
     technologies=models.IntegerField(blank=True)
     image = models.ImageField(upload_to="Port/about", default="default.jpg", null=True, blank=True)
     file = models.FileField(upload_to='resumes/',default='resumes/default_resume.pdf')


    
     def __str__(self):
        return self.desc



class SkillCategory(models.Model):
    name = models.CharField(max_length=100)  # e.g., Backend Developer, Frontend Developer
    icon_class = models.CharField(max_length=100, blank=True)  # e.g., "ri-server-line"
    color_class = models.CharField(max_length=50, default='bg-primary')  # e.g., bg-primary or bg-secondary

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)  # e.g., Django, React.js
    percentage = models.PositiveIntegerField(default=0)  # e.g., 90

    def __str__(self):
        return f"{self.name} ({self.percentage}%)"





class Education(models.Model):
    degree=models.CharField(max_length=30,blank=True,null=True)
    college=models.CharField(max_length=30)
    year=models.IntegerField(blank=True)
    cgpa=models.DecimalField(max_digits=4, decimal_places=2,blank=True,null=True)
    desc=models.CharField(max_length=300,null=True, blank=True)


    def __str__(self):
        return self.degree
    

class Technology(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name   

class Projects(models.Model):
    image=models.ImageField(upload_to="Port/images" ,default="")
    title=models.CharField(max_length=30)
    desc=models.CharField(max_length=300)
    technology=models.ManyToManyField(Technology)
    live_demo_url=models.URLField(blank=True,null=True)
    github_url=models.URLField(blank=True,null=True)

    def __str__(self):
        return self.title

class Achievements(models.Model):
    title=models.CharField(max_length=30)
    desc=models.CharField(max_length=300)


    def __str__(self):
        return self.title


class Contact(models.Model):
    location=models.CharField(max_length=30,null=True, blank=True)
    email=models.EmailField()
    phone=models.CharField(max_length=20,null=True, blank=True)
    linkdin_url=models.URLField(blank=True,null=True)
    github_url=models.URLField(blank=True,null=True)
    mail_url=models.URLField(blank=True,null=True)
    
    

    def __str__(self):
        return f"Contact Info-{self.email}"


class ContactMe(models.Model):
    name = models.CharField(max_length=200,null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    subject=models.CharField(max_length=200,null=True, blank=True)
    message=models.CharField(max_length=200,null=True, blank=True)
   

    def __str__(self):
        return self.name
    


class SkillCategory(models.Model):
    CATEGORY_CHOICES = [
        ('backend', 'Backend Developer'),
        ('frontend', 'Frontend Developer'),
    ]

    name = models.CharField(max_length=100, choices=CATEGORY_CHOICES, unique=True)

    def __str__(self):
        return self.get_name_display()


class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    proficiency = models.PositiveIntegerField(help_text="Enter percentage (0-100)")

    def __str__(self):
        return f"{self.name} ({self.proficiency}%)"    
    

class Footer(models.Model):
    title=models.CharField(max_length=200,null=True,blank=True)
    rights_title=models.CharField(max_length=200,null=True,blank=True)
    

    def __str__(self):
        return self.title