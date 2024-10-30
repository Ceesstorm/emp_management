from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('register', views.register, name="register"),
    path('my_login', views.my_login, name="my_login"),
    path('user-logout', views.user_logout, name="user-logout"),
    path('allemployees/', views.all_employees, name="allemployees"),
    path('alldepartments/', views.all_departments, name="alldepartments"),
    path('alltrucks/', views.all_trucks, name="alltrucks"),
    path('allrosters/', views.all_rosters, name="allrosters"),


    path('addemployee/', views.add_employee, name="addemployee"),
    path('adddepartment/', views.add_department, name="adddepartment"),
    path('addtruck/', views.add_truck, name="addtruck"),
    
    path('singleemployee/<int:empid>/', views.single_employee, name="singleemployee"),
    path('singledepartment/<int:empid>/', views.single_department, name="singledepartment"),
    path('singletruck/<int:id>/', views.single_truck, name='singletruck'),
    path('department/<int:empid>/', views.single_department, name='singledepartment'),
    path('updateemployee/<int:empid>/', views.update_employee, name="updateemployee"),
    path('updatedepartment/<int:empid>/', views.update_department, name='updatedepartment'),
    path('updatetruck/<int:id>/', views.update_truck, name='updatetruck'),
    path('deleteemployee/<int:empid>/', views.delete_employee, name="deleteemployee"),
    path('deletedepartment/<int:empid>/', views.delete_department, name="deletedepartment"),
    path('deletetruck/<int:empid>/', views.delete_truck, name="deletetruck"),
]
