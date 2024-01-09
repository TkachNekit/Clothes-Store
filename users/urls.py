from django.urls import path, include


from users.views import login, registration

app_name = "products"

urlpatterns = [
    path('login/', login, name="login"),
    path('registration/', registration, name="registration"),
]

