#https://developers.google.com/classroom/reference/rest/v1/courses.courseWork/list

from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/classroom.coursework.me']

creds = None
	# The file token.json stores the user's access and refresh tokens, and is
	# created automatically when the authorization flow completes for the first
	# time.
if os.path.exists('token.json'):
	creds = Credentials.from_authorized_user_file('token.json', SCOPES)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
	if creds and creds.expired and creds.refresh_token:
		creds.refresh(Request())
	else:
		flow = InstalledAppFlow.from_client_secrets_file(
			'credentials.json', SCOPES)
		creds = flow.run_local_server(port=0)
	# Save the credentials for the next run
	with open('token.json', 'w') as token:
		token.write(creds.to_json())

service = build('classroom', 'v1', credentials=creds)

# Call the Classroom API
results = service.courses().list(pageSize=10).execute()
courses = results.get('courses', [])

#.courses.courseWork.get(courseId="Musicianship I", id="527034234809")

coursework = service.courses().courseWork().list(courseId=527034234809).execute()
upcoming_coursework = coursework.get('courseWork', [])

for work in upcoming_coursework:
	print("Coursework ID:", work['id'])
	print("Title:", work['title'])
	print("Due Date:", work['dueDate'])
	print("Max Points:", work['maxPoints'])
	print("-----")