<h1>Database file setup</h1>

create a 'local_settings.py' file in you project directory and save the database configurations in there. 

(Note: Replace dbname, username and password according to the user you created.)

<code>
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
</code>

Alternatively, you can replace the following code snippet in settings.py and paste the above configuration directly.

<code>
try:
    from .local_settings import *
except ImportError:
    pass
</code>

<h1>Endpoints for testing</h1>

host: http://127.0.0.1:8000/

Application UI
<ul>
<li>Login with existing user (for ref: accounts/login)</li>
<li>View home (for ref: restaurant/home)</li>
<li>View menu (for ref: restaurant/menu)</li>
<li>View Bookings (for ref: bookings)</li>
<li>Add Booking (for ref: booking/tables/)</li>
<li>Logout (for ref: accounts/logout)</li>
</ul>


Insomnia (or other API testing tools)

<ul>
<li>auth/users/  - create new user/register</li>
<li>auth/token/login/  - obtain a token</li>
<li>auth/users - view users</li>
<li>restaurant/menu - add menu item (POST)</li>
<li>restaurant/menu/menuitemid - view single menu item - json response (GET)</li>
<li>restaurant/bookings - view all bookings - json response (GET)</li>
</ul>
