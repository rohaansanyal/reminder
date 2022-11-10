from datetime import datetime
import time

class Assignment():

	def __init__(self, title, desc, importance, month, day, hour, minute, countdown):

		self.importance = importance
		self.month = month
		self.day = day
		self.hour = hour
		self.minute = minute
		self.title = title
		self.desc = desc
		self.countdown = countdown
		self.strng = (str(importance)+" "+str(title)+" - "+ str(month)+" "+str(day)+" • "+str(hour)+":"+str(minute)+"\n"+str(desc)+"\n"+str(countdown))
		
		
		#today = datetime.date.today()
		#year = today.year

		currentyear = time.strftime("%y")

		eventTime=str(currentyear+"-"+month + ":" + day + ":" + hour + ":" + minute)

		CurrentTime = time.strftime("%m:%d:%H:%M")
		
		self.datetime = datetime.strptime(eventTime, "%y-%B:%d:%H:%M")

		delta = self.datetime - datetimeCurrent
		
		self.second = delta.total_seconds()