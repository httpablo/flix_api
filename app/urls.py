from django.contrib import admin
from django.urls import include, path
from actors.views import ActorCreateListView, ActorRetriveUpdateDestroyView
from movies.views import MovieCreateListView
from movies.views import MovieRetriveUpdateDestroyView
from reviews.views import ReviewCreateListView
from reviews.views import ReviewRetrieveUpdateDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/v1/', include('genres.urls')),

    path('actors/', ActorCreateListView.as_view(), name='actors-create-list'),
    path('actors/<int:pk>/', ActorRetriveUpdateDestroyView.as_view(), name='actors-detail-view'),

    path('movies/', MovieCreateListView.as_view(), name='movies-create-list'),
    path('movies/<int:pk>/', MovieRetriveUpdateDestroyView.as_view(), name='movies-detail-view'),

    path('reviews/', ReviewCreateListView.as_view(), name='reviews-create-list'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(), name='reviews-detail-view'),
]
