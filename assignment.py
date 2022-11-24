from datetime import datetime
import time

def selection_sort(unsorted, n):
	
	def swap(arr, a, b):
	    """ swap elements a and b in an array """
	    temp = arr[a]
	    arr[a] = arr[b]
	    arr[b] = temp

	CurrentTime = time.strftime("%m:%d:%H:%M")
	datetimeCurrent = datetime.strptime(CurrentTime, "%m:%d:%H:%M")

	for i in range(0, n):
		
		# initialise with first value
		current_min = (unsorted[i].datetime - datetimeCurrent).total_seconds()
		
		# min_index initialiser
		min_index = i
		
		# iterate over remaining unsorted items
		for j in range(i, n):
			
			# check if jth value is less than current min
			if (unsorted[j].datetime - datetimeCurrent).total_seconds() < current_min:
			  
				# update minimum value and index
				current_min = (unsorted[j].datetime - datetimeCurrent).total_seconds()
				min_index = j
				
		# swap ith and jth values
		swap(unsorted, i, min_index)

	return(arr)

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

		if len(hour) == 1:

			newhour = hour
			newhour = "0" + eventhour

		else:

			newhour = hour

		eventTime=str(currentyear+" "+month + " " + day + ":" + newhour + ":" + minute)

		CurrentTime = time.strftime("%m:%d:%H:%M")
		
		self.datetime = datetime.strptime(eventTime, "%y %B %d:%H:%M")

		#delta = self.datetime - CurrentTime
		
		#self.second = delta.total_seconds()