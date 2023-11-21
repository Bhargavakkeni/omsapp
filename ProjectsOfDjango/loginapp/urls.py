from django.urls import path
from . import views
urlpatterns=[
    path('',views.root,name='root'), #url when user enter the app
    path('loginpage/',views.index,name='loginpage'), #url for login
    path('loginpage/verifyUser',views.verifyUser,name='verifyUser'), #url for verification of login details
    path('registration',views.registration,name='registration'), #url for new user registration
    path('uploading',views.uploading,name='uploading'),     #url for uplading user login details data to the model
    path('omsadmin',views.omsadmin,name='omsadmin1'),
    path('omsadmin/<str:adminName>',views.omsadmin,name='omsadmin'), #url for displaying a CRUD application when login is successful
    path('show/<str:adminName>',views.show,name='show'), #url to display records of the user's(omsadmin) orders
    path('add/<str:adminName>',views.add,name='add'),    #url to add new records in to omsadmin database
    path('update/<str:adminName>',views.update,name='update'),  #url to update the specified fields in omsadmin database
    path('delete/<str:adminName>',views.delete,name='delete'),  #url to delete the specified record in omsadmin database
    path('logout',views.logout,name='logout'),  #url to logout from the omsadmin 
    path('resetpass',views.resetpass,name='resetpass'), # url to go to forgot password html to reset the password
    path('changepass',views.changepass,name='changepass'), #url to change the password
    
]