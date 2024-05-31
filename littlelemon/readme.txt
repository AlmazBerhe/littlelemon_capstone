Database file setup:
create a 'local_settings.py' file in you project directory and save the database configurations in there. 
(Replace dbname, username and password according to the user you created.)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dbname',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
         
    }
}

Alternatively, you can replace the following code snippet in settings.py and paste the above configuration directly.

try:
    from .local_settings import *
except ImportError:
    pass




Endpoints for testing

host: http://127.0.0.1:8000/

Application UI:
Login with existing user (for ref: accounts/login)
View home (for ref: restaurant/home)
View menu (for ref: restaurant/menu)
View Bookings (for ref: bookings)
Add Booking (for ref: booking/tables/)
Logout (for ref: accounts/logout)


Insomnia:

auth/users/  - create new user/register
auth/token/login/  - obtain a token
auth/users - view users
restaurant/menu - add menu item (POST)
restaurant/menu/<id> - view single menu item - json response (GET)
restaurant/bookings - view all bookings - json response (GET)