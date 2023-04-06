from . import views
from django.urls import path

app_name = 'dashboard'
urlpatterns = [
    path('', view=views.index, name="index"),
    path('<int:id>/', view=views.open_profile, name="profile"),
    path('about/', view=views.about_us, name="about")
    # path('data/', view=views.run_data, name="demo"),
]
