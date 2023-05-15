from django.contrib import admin

from .models import Education, Experience, Profile, Software, Technical, Work

# Register your models here.

admin.site.register(Profile)
admin.site.register(Work)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Software)
admin.site.register(Technical)
