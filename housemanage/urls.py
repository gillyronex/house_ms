from django.urls import path
from django.conf.urls.static import static
from .import views


urlpatterns = [
    path("createowner/",views.create_owner,name='owner'),
    path("getowners/",views.get_owners,name='owners'),
    path("updateowner/<int:id>/",views.update_owner,name='owner'),
    path("viewspecificowner/<int:id>/",views.get_specific_owner,name='owner'),
    path("deleteowner/<int:id>",views.delete_owner,name='owner')
]