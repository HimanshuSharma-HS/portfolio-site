from django.contrib import admin

# Register your models here.
from .models import Hero,Skill, SkillCategory,About,Education,Projects,Achievements,Contact,ContactMe,Technology,Footer,Logo

admin.site.register(Hero)
admin.site.register(About)
admin.site.register(Education)
admin.site.register(Projects)
admin.site.register(Achievements)
admin.site.register(Contact)
admin.site.register(ContactMe)
admin.site.register(Skill)
admin.site.register(SkillCategory)
admin.site.register(Technology)
admin.site.register(Footer)
admin.site.register(Logo)









class ContactMeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')