
==========

Violations

==========

Violations is a simple Django app to maintain violation records that a project wants to maintain.
For each violations, user can execute Actions and add new Comments

Each Violations are defined by it's Type, 'who' violated to 'whom' (can be a person or an event), & their types, a 'cc_list' which defines who all can take action against that violation,
'status' defining whether Violation is 'Active/Open', can be 'Ignored' or to be 'Archived' and 'violation_status'

Quick start
-----------

1. Add "violations" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'violations',
    )

2. Include the violations URLconf in your project urls.py like this::

    url(r'^violations/', include('violations.urls')),

3. Run `pip install -r requirements.txt` to install the pages necessary for this package

3. Run `python manage.py migrate` to create the violation models.

4. Start the development server and 
	* Add/Edit the types through URL http://127.0.0.1:8000/types/add/ - request_type : (POST)
	* Add/Edit/View the Violations through URL http://127.0.0.1:8000/violations/ - request_type : ( POST / POST / GET)
	* Add actions through URL http://127.0.0.1:8000/actions/add/ - request_type : (POST)
	* Add comments through URL http://127.0.0.1:8000/comments/add/ - request_type : (POST)