Installation
------------

Install latest from github:
```
pip install -e git+https://github.com/retailify/calixos-poll.git#egg=calixos-poll
```

Usage
-----

1. Add 'poll' application in the ``INSTALLED_APPS`` settings:

	```
	INSTALLED_APPS = (
    	# ...
    	'poll',
	)

	```

2. Add the poll's url to your urls.py.

	```
	urlpatterns = patterns('',
		# ...
    	url(r'^poll/', include('poll.urls')),
	)
	```

3. Run python manage.py migrate poll.

5. Add the poll to your page via django CMS

-----
Based on https://github.com/applecat/django-simple-poll
