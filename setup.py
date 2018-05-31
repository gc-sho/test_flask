"""

Flask Test

"""

from setuptools import setup, find_packages

setup(
    name='gc-test-flask',
    version='0.0.1',
    url='https://github.com/gc-sho/test_flask.git',
    description=""" Desription TBA """,
    packages=find_packages(),
    author=['Nenad Jakovljevic'],
    author_email=['nenad.jakovljevic@gamecredits.com'],
    install_requires=[
        'requests>=2.4.3',
        'Flask>=0.12',
        'Flask-SQLAlchemy>=2.1',
        'flasgger==0.8.1',
        'pymongo'
    ]
)