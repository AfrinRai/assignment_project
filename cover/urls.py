from django.urls import path
from .views.cbv_views import CoversListView
from .views.fbv_views import cover_page


urlpatterns = [
    path('cover/', cover_page),
    path('c_cover', CoversListView.as_view()),
]
