Django Project Boilerplate
===

To start a project -

    django-admin.py startproject --template=https://github.com/iambibhas/django-boilerplate/archive/master.zip myproject

Then create the dev settings -

    cp projectname/dev.py{.sample,}

Change `projectname` directory to anything you want and update `DJANGO_SETTINGS_MODULE` in `manage.py`.
