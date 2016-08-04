##Django ajax jQuery

This is a modified fork of [this](https://github.com/realpython/django-form-fun/tree/master/part1)

Server-side and client-side have been altered to persist all original form data in the database,
while client-side form contents are normalized and validated for US phone numbers. In addition,
I created a dictionary that maps US (and some other North American) area codes to states.

###TODO
* Create additional Django views for quick summaries (ie, counts of area codes per state)
* Create histogram of state frequency
* Loop through multiple states per entry, rather than just showing first

###Assumptions
To work locally, no further database details are needed, as sqlite3 settings are default.  
