from setuptools import setup, find_packages

setup(
    name='app',
    version='0.0.1',
    url='https://github.com/praekelt/jozihub-web',
    description='Website',
    author='Praekelt Developers',
    author_email='dev@praekeltfoundation.org',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    dependency_links=[
        'http://github.com/unomena/django-photologue/tarball/2.8.praekelt#egg=django-photologue-2.8.praekelt',
        'http://github.com/unomena/django-ckeditor-new/tarball/3.6.2.2#egg=django-ckeditor-3.6.2.2',
        'http://github.com/unomena/tunobase/tarball/1.0.3#egg=tunobase-1.0.3'
    ],
    install_requires=[
        'South',
        'django==1.11.29',
        'django-debug-toolbar==0.11.0',
        'django-countries',
        'django-polymorphic',
        'django-ckeditor==3.6.2.2',
        'django-photologue==2.8.praekelt',
        'django-registration==1.0',
        'django-preferences',
        'django-countries==1.5',
        'python-memcached',
        'django_compressor',
        'gunicorn',
        'celery==3.0.23',
        'django-celery==3.0.23',
        'django-honeypot',
        'Pillow',
        'psycopg2',
        'flufl.password==1.2.1',
        'tunobase==1.0.3',
        'raven',
        'django-extensions'
    ],
    include_package_data=True,
)
