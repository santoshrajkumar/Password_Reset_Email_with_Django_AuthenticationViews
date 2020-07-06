# Generating Password Reset Email (Secure) with Django Authentication views.

## This is the exact same project of my [Repository](https://github.com/santoshrajkumar/userprofile_CRUD_functionality_with_Django_signals), with password reset functionality embedded to the log in page. The new codes added to the project for the password reset functionality are explained below.


### New codes added in the urls.py file in the signal_demo folder are:


```python
from django.contrib.auth import views as auth_views

urlpatterns = [
  # This represents previously present lines of code, add the codes given below after that
  path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),

  path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),

  path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),

  path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
```
