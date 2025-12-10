# acme_project/urls.py
# Импортируем настройки проекта.
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

from django.conf import settings
# Импортируем функцию, позволяющую серверу разработки отдавать файлы.
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, reverse_lazy

from users.forms import CustomUserCreationForm



urlpatterns = [
    path(
        'auth/registration/', 
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=CustomUserCreationForm,
            success_url=reverse_lazy('pages:homepage'),
        ),
        name='registration',
    ),
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('birthday/', include('birthday.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    # В конце добавляем к списку вызов функции static.
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)