from datetime import datetime

class Assignment():

	def __init__(self, title, desc, importance, month, day, hour, minute, countdown, datetime):

		self.importance = importance
		self.month = month
		self.day = day
		self.hour = hour
		self.minute = minute
		self.title = title
		self.desc = desc
		self.countdown = countdown
		self.strng = (str(importance)+" "+str(title)+" - "+ str(month)+" "+str(day)+" • "+str(hour)+":"+str(minute)+"\n"+str(desc)+"\n"+str(countdown))
		
		eventTime=str(event.month + ":" + event.day + ":" + event.hour + ":" + event.minute)
		self.datetime = datetime.strptime(eventTime, "%B:%d:%H:%M")