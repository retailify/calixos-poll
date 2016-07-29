Simple Django poll application.

WARNING
-------
This application has changed radically. No more south and this poll module needs django-cms!

To save your all polls use the standard backup and after the migration load data from the backup.

Reset your all polls.

	```
	python manage.py migrate poll zero
	python manage.py migrate
	```

Installation
------------

Install latest from github:
```
pip install -e git+https://github.com/retailify/django-simple-poll.git#egg=django-simple-poll
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
2. If you want to deploy this plugin to django-cms add following into your settings:
	```
	SIMPLE_POLL_DJANGOCMS = True
	```

3. Add the poll's url to your urls.py.

	```
	urlpatterns = patterns('',
		# ...
    	url(r'^poll/', include('poll.urls')),
	)
	```

4. Run python manage.py migrate poll.

5. Add this tags in your template file to show poll:

	```
	{% load poll_tags %}
	{% poll %}
	```
or you can add the poll with your django-cms as plugin.

-----
Based on https://bitbucket.org/RafRaf/django-poll-system
