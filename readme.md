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

### Now add the SMTP configuration in the settings.py file for the email address you'll be using to send password reset email:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'your email host'
EMAIL_PORT = email port
EMAIL_USE_TLS = True / False depending on your email
EMAIL_HOST_USER = 'your remail id'
EMAIL_HOST_PASSWORD = 'your email password'
```
- For Gmail, the configuration will be :
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'yourid@gmail.com'
EMAIL_HOST_PASSWORD = 'your gmail password'
```
* Also keep in mind that you need to go to https://myaccount.google.com/lesssecureapps?pli=1 and turn allow less secure apps ON. Otherwise Gmail will block your django apps request to access your Gmail to send the password reset email.
