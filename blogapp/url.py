from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('homepage/', views.homepage),
                  path('blogapp/', views.add_blog),
                  path('bookreview/', views.review),
                  path('toread/', views.tbr),
                  path('favourite/<int:cat_id>/', views.favourite),
                  path('read/<int:cur_id>/', views.current),
                  path('book/<int:cat_id>/', views.book_detail),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

