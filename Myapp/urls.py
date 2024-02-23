from django.urls import path
from Myapp import views

urlpatterns=[
   path('',views.home,name='my_home'),
   path('',views.about,name='my_about'),
   path('',views.we_do,name='we_do'),
   path('',views.portfolio,name='portfolio'),
   path('',views.contact,name='contact')
]