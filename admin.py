from django.contrib import admin
from .models import Resume1

# Register your models here.
@admin.register(Resume1)
class ResumeModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','dob','gender','locality','city','pin','state','mobile','job_city','profile_image','my_file']