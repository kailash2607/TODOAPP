from django.contrib import admin
from django.urls import path, include  # ✅ include is important

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # ✅ Include URLs from the 'todo' app
    path('', include('todo.urls')),  # This will handle login, register, dashboard, etc.
]
