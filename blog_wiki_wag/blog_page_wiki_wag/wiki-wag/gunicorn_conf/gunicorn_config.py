import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
bind = '0.0.0.0:8000'
loglevel = 'info'
errorlog = '-'
accesslog = '-'
raw_env = ['DJANGO_SETTINGS_MODULE=quintiliano.settings.dev']
