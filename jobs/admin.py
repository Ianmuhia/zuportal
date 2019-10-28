from django.contrib import admin

from .models import Category, Company, Job, Tech_included, Job_Application



class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_featured','employer', 'post_date', 'location')
    list_display_links = ('id', 'title', 'employer')
    list_filter =('employer', 'category')
    list_editable = ('is_featured',)
    search_fields = ('title', 'description','location','category','state','salary')
    list_per_page = 20



class Job_ApplicationAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'job', 'name', 'contact_date', 'phone', 'is_accepted')
    list_display_links =  ('user_id', 'job', 'name', 'contact_date', 'phone')
    list_filter =('name', 'job', 'contact_date')
    list_editable = ('is_accepted',)
    search_fields = ('job', 'name','email')
    list_per_page = 10

admin.site.register(Job, JobAdmin)
admin.site.register(Job_Application, Job_ApplicationAdmin)

admin.site.register(Company)
admin.site.register(Category)

admin.site.register(Tech_included)

