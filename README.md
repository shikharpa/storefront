BOOKSTORE Api 

First I set up virtual environment on my desktop folder "Storefront" using dependency tool pipenv.

Installed Django framework. 

Created a project named Bookstore. 

Created an app named Bookapi and added to apps in settings.py.

Installed rest framework and added that to settings.py.

Craeted 2 models named Bookshelf and Reviews using default database sqlite3.

Created serializer for json data parsing.

Craeted BookViewset and reviewset for apis handling.

Override delete method to implement soft delete option. 

Used decorators to connevt both viewset to obtain data based on first viewset.

Registered urls with routers.

Installed django-filters and added to apps in settings.py to provide filter in get apis.

Craeted superadmin to handle admin authetication.

Used django utils decorators for viewset caching.

Provide exception handling with try except for wrong request id.


