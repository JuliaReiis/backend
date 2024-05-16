#     def __str__(self):
#         return self.nome

from django.db import models
from django.utils import timezone

class User(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    last_password_redefinition_at = models.DateTimeField(null=True, blank=True)
    email_verified = models.BooleanField(default=False)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    last_update_at = models.DateTimeField(default=timezone.now)
    # companies = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, blank=True, related_name='companies')
    # company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, blank=True, related_name='companies')

    docs = models.ManyToManyField('Doc', related_name='documents_assign')


    company = models.OneToOneField('Company',on_delete=models.CASCADE, related_name='userOwner')
    companies = models.ManyToManyField('Company', related_name='users')



    def save(self):
        self.last_update_at = timezone.now()
        super().save()

class Company(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    last_update_at = models.DateTimeField(default=timezone.now)
                # field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),

    locate = models.CharField(max_length=50, default="-03:00")
    lang = models.CharField(max_length=2, default="pt")
    
    # created_by = models.OneToOneField('User', on_delete=models.CASCADE)
    created_by = models.ForeignKey('User', on_delete=models.CASCADE, related_name='+')
    # users = models.ManyToManyField('User', related_name='companies')
    docs = models.ManyToManyField('Doc', related_name='companies')

    def save(self):
        if not self.locate:
            self.locate = "-03:00"
        if not self.lang:
            self.lang = "pt"
        self.last_update_at = timezone.now()
        super().save()

class Doc(models.Model):
    name = models.CharField(max_length=255)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    last_update_at = models.DateTimeField(default=timezone.now)
    date_limit_to_sign = models.DateTimeField(null=True, blank=True)
    signed = models.BooleanField(default=False)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='+')
    created_by = models.ForeignKey('User', on_delete=models.CASCADE, related_name='+')

    def save(self):
        self.last_update_at = timezone.now()
        super().save()