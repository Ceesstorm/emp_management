from django.contrib import admin

from emp.models import Department, Employee, Roster, Truck

# Register your models here.
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Truck)
admin.site.register(Roster)

