from django.contrib import admin

from .models import InjuryRecord, User, UserProfile


admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(InjuryRecord)