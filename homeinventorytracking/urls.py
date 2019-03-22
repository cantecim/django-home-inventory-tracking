from django.urls import path

from . import views

app_name = 'hit'
urlpatterns = [
    path('', views.home_page, name='index'),
    path('buildings/', views.building.BuildingListView.as_view(), name='buildings'),
    path('buildings/new', views.building.BuildingCreateView.as_view(), name='create_building'),
    path('buildings/<int:pk>/', views.building.BuildingUpdateView.as_view(), name='building'),
    path('buildings/<int:pk>/apartments/', views.apartment.ApartmentListView.as_view(), name='apartments'),
    path('buildings/<int:pk>/apartments/new', views.apartment.ApartmentCreateView.as_view(), name='create_apartment'),
    path('buildings/<int:building>/apartments/<int:pk>/', views.apartment.ApartmentUpdateView.as_view(),
         name='apartment'),
    path('buildings/<int:building>/apartments/<int:pk>/rooms/', views.room.RoomListView.as_view(), name='rooms'),
    path('buildings/<int:building>/apartments/<int:pk>/rooms/new', views.room.RoomCreateView.as_view(),
         name='create_room'),
    path('buildings/<int:building>/apartments/<int:apartment>/rooms/<int:pk>/', views.room.RoomUpdateView.as_view(),
         name='room'),
    path('buildings/<int:building>/apartments/<int:apartment>/rooms/<int:pk>/objects/',
         views.object.ObjectListView.as_view(),
         name='objects'),
    path('buildings/<int:building>/apartments/<int:apartment>/rooms/<int:pk>/objects/new',
         views.object.ObjectCreateView.as_view(),
         name='create_object'),
    path('buildings/<int:building>/apartments/<int:apartment>/rooms/<int:room>/objects/<int:pk>/',
         views.object.ObjectUpdateView.as_view(),
         name='object'),
    path('structure/delete/<int:pk>/', views.structure_delete, name='delete_structure'),
    path('object/delete/<int:pk>/', views.object_delete, name='delete_object'),
]
