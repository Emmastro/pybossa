# -*- coding: utf8 -*-
# This file is part of PyBossa.
#
# Copyright (C) 2013 SF Isle of Man Limited
#
# PyBossa is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyBossa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PyBossa.  If not, see <http://www.gnu.org/licenses/>.
import logging
import os

from dotenv import load_dotenv

load_dotenv()

DEBUG = (os.getenv('DEBUG', 'False') == 'True')

# host for local development
HOST = os.environ.get('HOST', '0.0.0.0')

# use SERVER_NAME instead of HOST for production environment with real URLs
# SERVER_NAME = 'somecoolurl.com'

# PORT used for local development, in production environment let nginx handle this
PORT = os.environ.get('PORT', 5000)

SECRET = os.environ.get('SECRET', 'foobar')
SECRET_KEY = os.environ.get('SECRET_KEY', 'my-session-secret')

POSTGRES_USER = os.environ.get('POSTGRES_USER', 'pybossa')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'pybossa')
DB_HOST = os.environ.get('DB_HOST', '0.0.0.0')
POSTGRES_DB = os.environ.get('POSTGRES_DB', 'pybossa')


SQLALCHEMY_DATABASE_URI = os.environ.get(
    'SQLALCHEMY_DATABASE_URI', f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}/{POSTGRES_DB}')

# Slave configuration for DB
# SQLALCHEMY_BINDS = {
#    'slave': 'postgresql://user:password@server/db'
# }

ITSDANGEROUSKEY = os.environ.get('ITSDANGEROUSKEY', 'its-dangerous-key')

# project configuration
BRAND = os.environ.get('BRAND', 'PyBossa')
TITLE = os.environ.get('TITLE', 'PyBossa')
LOGO = os.environ.get('LOGO', 'default_logo.svg')
COPYRIGHT = os.environ.get('COPYRIGHT', 'Set Your Institution')
DESCRIPTION = os.environ.get(
    'DESCRIPTION', 'Set the description in your config')
TERMSOFUSE = os.environ.get('TERMSOFUSE', 'http://okfn.org/terms-of-use/')
DATAUSE = os.environ.get('DATAUSE', 'http://opendatacommons.org/licenses/by/')
CONTACT_EMAIL = os.environ.get('CONTACT_EMAIL', 'info@pybossa.com')
CONTACT_TWITTER = os.environ.get('CONTACT_TWITTER', 'PyBossa')

# Default number of projects per page
APPS_PER_PAGE = os.environ.get('APPS_PER_PAGE', 20)

# External Auth providers

TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY', '')
TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET', '')
FACEBOOK_APP_ID = os.environ.get('FACEBOOK_APP_ID', '')
FACEBOOK_APP_SECRET = os.environ.get('FACEBOOK_APP_SECRET', '')
GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID', '')
GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET', '')


# Supported Languages

DEFAULT_LOCALE = 'en'
LOCALES = [('en', 'English'), ('es', u'Español'),
           ('it', 'Italiano'), ('fr', u'Français'),
           ('ja', u'日本語'), ('pt_BR', 'Brazilian Portuguese')]


# list of administrator emails to which error emails get sent. On .env, you can set this as a comma separated list
ADMINS = [os.environ.get('ADMINS', '').split(',')]

# CKAN URL for API calls


CKAN_NAME = os.environ.get('CKAN_NAME', "Demo CKAN server")
CKAN_URL = os.environ.get('CKAN_URL', "http://demo.ckan.org")


# logging config
# Sentry configuration
SENTRY_DSN = os.environ.get('SENTRY_DSN', '')

# set path to enable
LOG_FILE = os.environ.get('LOG_FILE', '/tmp/log')

# Optional log level

LOG_LEVEL = logging.DEBUG

# Mail setup
MAIL_SERVER = 'localhost'
MAIL_USERNAME = None
MAIL_PASSWORD = None
MAIL_PORT = 25
MAIL_FAIL_SILENTLY = False
MAIL_DEFAULT_SENDER = 'PyBossa Support <info@pybossa.com>'

# Announcement messages
# Use any combination of the next type of messages: root, user, and app owners
# ANNOUNCEMENT = {'admin': 'Root Message', 'user': 'User Message', 'owner': 'Owner Message'}

# Enforce Privacy Mode, by default is disabled
# This config variable will disable all related user pages except for admins
# Stats, top users, leaderboard, etc
ENFORCE_PRIVACY = False


# Cache setup. By default it is enabled
# Redis Sentinel
# List of Sentinel servers (IP, port)
# On .env, set as a comma separated list of IP:port


REDIS_SENTINEL = [('redis-sentinel', 26379)]
REDIS_MASTER = os.environ.get('REDIS_MASTER', 'redis-master')
REDIS_DB = os.environ.get('REDIS_DB', 0)
REDIS_KEYPREFIX = os.environ.get('REDIS_KEYPREFIX', 'pybossa_cache')
REDIS_SOCKET_TIMEOUT = os.environ.get('REDIS_SOCKET_TIMEOUT', None)
REDIS_RETRY_ON_TIMEOUT = os.environ.get('REDIS_RETRY_ON_TIMEOUT', True)

# Allowed upload extensions
ALLOWED_EXTENSIONS = ['js', 'css', 'png', 'jpg', 'jpeg', 'gif', 'zip']

# If you want to use the local uploader configure which folder
UPLOAD_METHOD = os.environ.get('UPLOAD_METHOD', 'local')
UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', 'uploads')

# If you want to use Rackspace for uploads, configure it here
# RACKSPACE_USERNAME = 'username'
# RACKSPACE_API_KEY = 'apikey'
# RACKSPACE_REGION = 'ORD'

# Default number of users shown in the leaderboard
# LEADERBOARD = 20
# Default shown presenters
# PRESENTERS = ["basic", "image", "sound", "video", "map", "pdf"]
# Default Google Docs spreadsheet template tasks URLs
TEMPLATE_TASKS = {
    'image': "https://docs.google.com/spreadsheet/ccc?key=0AsNlt0WgPAHwdHFEN29mZUF0czJWMUhIejF6dWZXdkE&usp=sharing",
    'sound': "https://docs.google.com/spreadsheet/ccc?key=0AsNlt0WgPAHwdEczcWduOXRUb1JUc1VGMmJtc2xXaXc&usp=sharing",
    'video': "https://docs.google.com/spreadsheet/ccc?key=0AsNlt0WgPAHwdGZ2UGhxSTJjQl9YNVhfUVhGRUdoRWc&usp=sharing",
    'map': "https://docs.google.com/spreadsheet/ccc?key=0AsNlt0WgPAHwdGZnbjdwcnhKRVNlN1dGXy0tTnNWWXc&usp=sharing",
    'pdf': "https://docs.google.com/spreadsheet/ccc?key=0AsNlt0WgPAHwdEVVamc0R0hrcjlGdXRaUXlqRXlJMEE&usp=sharing"}

# Expiration time for password protected project cookies
PASSWD_COOKIE_TIMEOUT = os.environ.get('PASSWD_COOKIE_TIMEOUT', 60 * 30)

# Expiration time for account confirmation / password recovery links
ACCOUNT_LINK_EXPIRATION = os.environ.get('ACCOUNT_LINK_EXPIRATION', 5 * 60 * 60)

# Ratelimit configuration
# LIMIT = 300
# PER = 15 * 60

# Disable new account confirmation (via email)
ACCOUNT_CONFIRMATION_DISABLED = os.environ.get('ACCOUNT_CONFIRMATION_DISABLED', True)

# Mailchimp API key
# MAILCHIMP_API_KEY = "your-key"
# MAILCHIMP_LIST_ID = "your-list-ID"

# Flickr API key and secret
# FLICKR_API_KEY = 'your-key'
# FLICKR_SHARED_SECRET = 'your-secret'

# Dropbox app key
# DROPBOX_APP_KEY = 'your-key'

# Send emails weekly update every
# WEEKLY_UPDATE_STATS = 'Sunday'

# Youtube API server key
# YOUTUBE_API_SERVER_KEY = 'your-key'

# Enable Server Sent Events
# WARNING: this will require to run PyBossa in async mode. Check the docs.
# WARNING: if you don't enable async when serving PyBossa, the server will lock
# WARNING: and it will not work. For this reason, it's disabled by default.
# SSE = False

# Add here any other ATOM feed that you want to get notified.
NEWS_URL = ['https://github.com/Scifabric/enki/releases.atom',
            'https://github.com/Scifabric/pybossa-client/releases.atom',
            'https://github.com/Scifabric/pbs/releases.atom']

# Pro user features. False will make the feature available to all regular users,
# while True will make it available only to pro users
PRO_FEATURES = {
    'auditlog':              True,
    'webhooks':              True,
    'updated_exports':       True,
    'notify_blog_updates':   True,
    'project_weekly_report': True,
    'autoimporter':          True,
    'better_stats':          True
}

# Libsass style. You can use nested, expanded, compact and compressed
LIBSASS_STYLE = 'compressed'

# CORS resources configuration.
# WARNING: Only modify this if you know what you are doing. The below config
# are the defaults, allowing PYBOSSA to have full CORS api.
# For more options, check the Flask-Cors documentation: https://flask-cors.readthedocs.io/en/latest/
# CORS_RESOURCES = {r"/api/*": {"origins": "*",
#                               "allow_headers": ['Content-Type',
#                                                 'Authorization'],
#                               "methods": "*"
#                               }}

# Email notifications for background jobs.
# FAILED_JOBS_MAILS = 7
# FAILED_JOBS_RETRIES = 3

# Language to use stems, full text search, etc. from postgresql.
# FULLTEXTSEARCH_LANGUAGE = 'english'


# Use strict slashes at endpoints, by default True
# This will return a 404 if and endpoint does not have the api/endpoint/
# while if you configured as False, it will return the resource with and without the trailing /
# STRICT_SLASHES = True

# Use SSO on Disqus.com
# DISQUS_SECRET_KEY = 'secret-key'
# DISQUS_PUBLIC_KEY = 'public-key'

# Use Web Push Notifications
# ONESIGNAL_APP_ID = 'Your-app-id'
# ONESIGNAL_API_KEY = 'your-app-key'


# Enable two factor authentication
# ENABLE_TWO_FACTOR_AUTH = True

# Strong password policy for user accounts
# ENABLE_STRONG_PASSWORD = True

# Create new leaderboards based on info field keys from user
# LEADERBOARDS = ['foo', 'bar']

# Unpublish inactive projects
# UNPUBLISH_PROJECTS = True

# Use this config variable to create valid URLs for your SPA
# SPA_SERVER_NAME = 'https://yourserver.com'

# LDAP
# LDAP_HOST = '127.0.0.1'
# LDAP_BASE_DN = 'ou=users,dc=scifabric,dc=com'
# LDAP_USERNAME = 'cn=yourusername,dc=scifabric,dc=com'
# LDAP_PASSWORD = 'yourpassword'
# LDAP_OBJECTS_DN = 'dn'
# LDAP_OPENLDAP = True
# Adapt it to your specific needs in your LDAP org
# LDAP_USER_OBJECT_FILTER = '(&(objectclass=inetOrgPerson)(cn=%s))'
# LDAP_USER_FILTER_FIELD = 'cn'
# LDAP_PYBOSSA_FIELDS = {'fullname': 'givenName',
#                        'name': 'uid',
#                        'email_addr': 'cn'}

# Flask profiler
# FLASK_PROFILER = {
#     "enabled": True,
#     "storage": {
#         "engine": "sqlite"
#     },
#     "basicAuth":{
#         "enabled": True,
#         "username": "admin",
#         "password": "admin"
#     },
#     "ignore": [
# 	    "^/static/.*"
# 	]
# }
# Specify which key from the info field of task, task_run or result is going to be used as the root key
# for exporting in CSV format
# TASK_CSV_EXPORT_INFO_KEY = 'key'
# TASK_RUN_CSV_EXPORT_INFO_KEY = 'key2'
# RESULT_CSV_EXPORT_INFO_KEY = 'key3'

# A 32 char string for AES encryption of public IPs.
# NOTE: this is really important, don't use the following one
# as anyone with the source code of pybossa will be able to reverse
# the anonymization of the IPs.
CRYPTOPAN_KEY = '32-char-str-for-AES-key-and-pad.'

# TTL for ZIP files of personal data
TTL_ZIP_SEC_FILES = 3

# Instruct PYBOSSA to generate HTTP or HTTPS
PREFERRED_URL_SCHEME = 'https'

# Instruct PYBOSSA to generate absolute paths or not for avatars
AVATAR_ABSOLUTE = True

# Inactive users months to send email notification
USER_INACTIVE_NOTIFICATION = 5
# Inactive users months to delete users
USER_INACTIVE_DELETE = 6

# Inactive users email SQL query
INACTIVE_USERS_SQL_QUERY = """SELECT user_id FROM task_run WHERE user_id IS NOT NULL AND to_date(task_run.finish_time, 'YYYY-MM-DD\THH24:MI:SS.US') >= NOW() - '12 month'::INTERVAL AND to_date(task_run.finish_time, 'YYYY-MM-DD\THH24:MI:SS.US') < NOW() - '3 month'::INTERVAL GROUP BY user_id ORDER BY user_id;"""

THEME = 'default'