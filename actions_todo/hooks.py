app_name = "actions_todo"
app_title = "Actions Todo"
app_publisher = "Nazmul Hossain"
app_description = "Actions ToDo Task list with Task Progress App"
app_email = "nazmulfx.dev@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "actions_todo",
# 		"logo": "/assets/actions_todo/logo.png",
# 		"title": "Actions Todo",
# 		"route": "/actions_todo",
# 		"has_permission": "actions_todo.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/actions_todo/css/actions_todo.css"
# app_include_js = "/assets/actions_todo/js/actions_todo.js"

# include js, css files in header of web template
# web_include_css = "/assets/actions_todo/css/actions_todo.css"
# web_include_js = "/assets/actions_todo/js/actions_todo.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "actions_todo/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "actions_todo/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "actions_todo.utils.jinja_methods",
# 	"filters": "actions_todo.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "actions_todo.install.before_install"
# after_install = "actions_todo.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "actions_todo.uninstall.before_uninstall"
# after_uninstall = "actions_todo.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "actions_todo.utils.before_app_install"
# after_app_install = "actions_todo.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "actions_todo.utils.before_app_uninstall"
# after_app_uninstall = "actions_todo.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "actions_todo.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"actions_todo.tasks.all"
# 	],
# 	"daily": [
# 		"actions_todo.tasks.daily"
# 	],
# 	"hourly": [
# 		"actions_todo.tasks.hourly"
# 	],
# 	"weekly": [
# 		"actions_todo.tasks.weekly"
# 	],
# 	"monthly": [
# 		"actions_todo.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "actions_todo.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "actions_todo.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "actions_todo.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["actions_todo.utils.before_request"]
# after_request = ["actions_todo.utils.after_request"]

# Job Events
# ----------
# before_job = ["actions_todo.utils.before_job"]
# after_job = ["actions_todo.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"actions_todo.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }


website_route_rules = [{'from_route': '/frontend/<path:app_path>', 'to_route': 'frontend'},]