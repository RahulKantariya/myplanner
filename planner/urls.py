from django.urls import path

from . import views

urlpatterns = [
    path('', views.Homepage, name='Homepage'),
    path('dashboard/',views.index,name='dashboard'),
    path('profile/',views.profile,name='profile'),
    path('preview/',views.preview,name='preview'),
    path('basicdetail/',views.basicdetail,name='basicdetail'),
    path('new/',views.new,name='new'),
    path('someview/<int:id>',views.some_view,name="someview"),
    path('tracker/',views.listplan,name="tracker"),
    path('existingplan/',views.existingplan,name="existingplan"),
    path('updateform/<int:id>',views.updateform,name="updateform"),
    path('update/<int:id>',views.update,name="update"),
    path('trackerdetail/',views.trackerdetail,name="trackerdetail")


]