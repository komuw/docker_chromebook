run:
	@pip install -r requirements.txt
	@python manage.py syncdb --noinput --settings=config.settings.development
	@python manage.py migrate --settings=config.settings.development
	@python manage.py collectstatic --noinput --settings=config.settings.development
	@python manage.py runserver 0.0.0.0:7000 --settings=config.settings.development

