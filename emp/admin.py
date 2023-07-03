from django.contrib import admin
from .models import Emp,Testimonial

class EmpAdmin(admin.ModelAdmin):
    list_display=('name','working','emp_id','phone')
    list_editable=('working','phone')
    search_fields=('name','emp_id')
    list_filter=('working',)


admin.site.register(Emp,EmpAdmin)
admin.site.register(Testimonial)

# Register your models here.
