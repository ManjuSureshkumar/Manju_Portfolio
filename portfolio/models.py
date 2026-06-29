from django.db import models


# ==========================
# Profile
# ==========================

class Profile(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profile/')
    resume = models.FileField(upload_to='resume/', blank=True, null=True)

    about = models.TextField()

    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=200)

    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    portfolio = models.URLField(blank=True)

    def __str__(self):
        return self.name


# ==========================
# Skills
# ==========================

class Skill(models.Model):
    skill_name = models.CharField(max_length=100)
    percentage = models.IntegerField(default=80)

    def __str__(self):
        return self.skill_name


# ==========================
# Education
# ==========================

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=250)
    year = models.CharField(max_length=30)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.degree


# ==========================
# Experience
# ==========================

class Experience(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.company


# ==========================
# Services
# ==========================

class Service(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


# ==========================
# Projects
# ==========================

class Project(models.Model):
    title = models.CharField(max_length=200)

    image = models.ImageField(upload_to='projects/')

    description = models.TextField()

    technologies = models.CharField(
        max_length=300,
        help_text="Example: HTML, CSS, JavaScript, Django"
    )

    github = models.URLField(blank=True)

    live_demo = models.URLField(blank=True)

    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# ==========================
# Certificates
# ==========================

class Certificate(models.Model):
    title = models.CharField(max_length=200)

    organization = models.CharField(max_length=200)

    year = models.CharField(max_length=20)

    certificate_image = models.ImageField(
        upload_to='certificates/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title


# ==========================
# Contact Messages
# ==========================

class Contact(models.Model):
    name = models.CharField(max_length=100)

    email = models.EmailField()

    subject = models.CharField(max_length=200)

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# ==========================
# Internship
# ==========================

class Internship(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.TextField()
    certificate_image = models.ImageField(
        upload_to='Intership_certificates/',
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.role} - {self.company}"