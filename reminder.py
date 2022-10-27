import tkinter as tk
from datetime import datetime, timedelta
import time
import tkinter.font as font
import tkinter.messagebox as messagebox
from tkinter import *
from assignment import Assignment
import platform
import datetime
from datetime import datetime

#test
#test 2

window = tk.Tk()
window.title("Habitude")
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
window.option_add('*Font', '1')
window.geometry(str(screen_width) + "x" + str(screen_height))
device_os = str(platform.system())

description = "Test"

window_width=window.winfo_width()
window_height=window.winfo_height()
placement_unit_x = window.winfo_screenwidth()/20
placement_unit_y = window.winfo_screenheight()/20

#print(max_hieght)
#print(max_width)
#print(placement_unit_x)
#print(placement_unit_y)

banner = tk.Label(window, text=" "*1000, fg="white", bg="grey60")
banner.place(x=(0),y=(0))

#habitude = tk.Label(window, text="Habitude", fg="white", bg="grey60")
#habitude.place(x=(window_width/2),y=(0))

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

tasks = []

tasks_shown = []

veryimportanttasks = []
importanttasks = []
notimportanttasks = []

selected_month = tk.StringVar(window)
selected_month.set(months[0])

dropdown_list_month = tk.OptionMenu(window, selected_month, *months)
dropdown_list_month.place(x=(placement_unit_x*1), y=(placement_unit_y*3))

night_day = ["Light", "Dark"]

selected_theme = tk.StringVar(window)
selected_theme.set(night_day[0])

dropdown_night_day = tk.OptionMenu(window, selected_theme, *night_day)
dropdown_night_day.place(x=placement_unit_x*1, y=placement_unit_y*18)

monthlabel = tk.Label(window, text="Month", fg="white", bg="grey60")
monthlabel.place(x=placement_unit_x*2.5, y=placement_unit_y*2.5)

days = range(1, 32)
days = [str(i).zfill(2) for i in days]

selected_day = tk.StringVar(window)
selected_day.set(days[0])

dropdown_list_day = tk.OptionMenu(window, selected_day, *days)
dropdown_list_day.place(x=(placement_unit_x*7.5), y=(placement_unit_y*3))

daylabel = tk.Label(window, text="Day", fg="white", bg="grey60")
daylabel.place(x=(placement_unit_x*7.5), y=(placement_unit_y*2.5))

important = ["Very Important", "Important", "Not Important"]

selected_importance = tk.StringVar(window)
selected_importance.set(important[0]) 

dropdown_list_importance = tk.OptionMenu(window, selected_importance, *important)
dropdown_list_importance.place(x=(placement_unit_x*2.5), y=(placement_unit_y*7))

'''
am_and_pm = ["AM", "PM"]

selected_am_or_pm = tk.StringVar(window)
selected_am_or_pm.set(am_and_pm[0])

am_or_pm = tk.OptionMenu(window, selected_am_or_pm, *am_and_pm)
am_or_pm.place(x=(placement_unit_x*2.5), y=(placement_unit_y*8))
'''
hours = range(1, 25)

selected_hour = tk.StringVar(window)
selected_hour.set(hours[0])

dropdown_list_hour = tk.OptionMenu(window, selected_hour, *hours)
dropdown_list_hour.place(x=(placement_unit_x*2.5), y=(placement_unit_y*5.5))

hours = tk.Label(window, text="Hours", fg="white", bg="grey60")
hours.place(x=(placement_unit_x*2.5), y=(placement_unit_y*5))

minutes = range(0, 60)
minutes = [str(i).zfill(2) for i in minutes]

selected_minutes = tk.StringVar(window)
selected_minutes.set(minutes[0])

dropdown_list_minutes = tk.OptionMenu(window, selected_minutes, *minutes)
dropdown_list_minutes.place(x=(placement_unit_x*7.5), y=(placement_unit_y*5.5))

minutes = tk.Label(window, text="Minutes", fg="white", bg="grey60")
minutes.place(x=(placement_unit_x*7.5), y=(placement_unit_y*5))

reminder_holder = tk.StringVar(window, "")
veryimportanttasks_holder = tk.StringVar(window, "")
importanttasks_holder = tk.StringVar(window, "")
notimportanttasks_holder = tk.StringVar(window, "")

title = tk.StringVar(window, "Title")

entry_title = tk.Entry(window, text=title)
entry_title.place(x=placement_unit_x*1.5, y=placement_unit_y)

completed = tk.StringVar(window, "Event to Remove")

to_remove = []

entry_completed = tk.Entry(window, text=completed)
entry_completed.place(x=(placement_unit_x*7.5), y=(placement_unit_y*8))

#confirm = tk.Button(window, text="Enter", command=reminder_confirm, fg="white", bg="sienna1")

#descript = tk.StringVar(window, "Description")

#description = tk.Text(window, x=placement_unit_x*5, y=placement_unit_y, width=20, height=4, wrap = WORD, padx = 10, pady = 10)
#description.pack(fill=None, expand=False)
#description.place(x=placement_unit_x*5, y=placement_unit_y, width=350, height=70, wrap = WORD, padx = 10, pady = 10)


#current_time=tk.Label(window, textvariable=datetime.now(),fg="black", bg="grey60")
#current_time.place(x=200, y=1000)

clockTime = tk.Label(window, text=" ", bg="sienna1")
clockTime.place(x=(window_width/2), y=0)

addtime = tk.StringVar(window, "10")
not_completed_addtime = tk.Entry(window, text=addtime)
not_completed_addtime.place(x=(placement_unit_x*2.5), y=(placement_unit_y*17))

def set_current_date():
	selected_day.set(time.strftime("%d"))
	selected_month.set(time.strftime("%B"))
	selected_hour.set(time.strftime("%H"))
	selected_minutes.set(time.strftime("%M"))


current_date = tk.Button(window, text="Set Current Time", command=set_current_date, fg="white", bg="sienna1")
current_date.place(x=(placement_unit_x*7.5), y=(placement_unit_y*1.5))

settingslabel_banner = tk.Label(window, text=" "*404, bg="sienna1", font=("IBM Plex Sans Light", 25))
settingslabel_banner.place(x=0, y=0)

settingslabel = tk.Label(window, text="Settings", bg="sienna1", font=("IBM Plex Sans Light", 25))
settingslabel.place(x=0, y=0)

createeventbanner = tk.Label(window, text=" "*404, bg="sienna1", font=("IBM Plex Sans Light", 25))
createeventbanner.place(x=0, y=0)

createeventlabel = tk.Label(window, text="Event Creation", bg="sienna1", font=("IBM Plex Sans Light", 25))
createeventlabel.place(x=0, y=0)

tasksbg = tk.Label(window, text=" "*50, bg="snow3", font=("IBM Plex Sans Light", 1000))
tasksbg.place(x=0, y=0)

tasksbanner = tk.Label(window, text=" "*404, bg="tomato3", font=("IBM Plex Sans Light", 25))
tasksbanner.place(x=0, y=0)

taskslabel = tk.Label(window, text="Tasks", bg="tomato3", font=("IBM Plex Sans Light", 25))
taskslabel.place(x=0, y=0)

descadded = False
desctext = ""
descstr = ""

#leap year

month_ends = {"January":31, "February":28, "March":31, "April":30, "May":31, "June":30, "July":31, "August":31, "September":30, "October":31, "November":30, "December":31}
'''
if selected_am_or_pm.get() == "PM":

	curr_time = time.strftime("%B %d • %h:%M")
	selected_hour = selected_hour + 12
'''

def clockChange():
	currentTimeMilitary=time.strftime("%B %d • %H:%M")
	clockTime.config(text=currentTimeMilitary)
	clockTime.after(1000,clockChange)

def notificationReminder():

	for event in tasks_shown: #remind notification

		event_time = str()



def tick():

	global tasks_shown
	global tasks
	global selected_month_number
	TimeMonth=time.strftime("%B")#current time of the day in a certin form to check the task
	TimeDay=time.strftime("%d")
	TimeHour=time.strftime("%H")
	TimeMinute=time.strftime("%M")

	CurrentTime = time.strftime("%m:%d:%H:%M")

	to_be_deleted = []

	window_width=window.winfo_width()
	window_height=window.winfo_height()
	placement_unit_x = window.winfo_width()/20
	placement_unit_y = window.winfo_height()/20


	selected_month_number=0

	a=0
	for a in months:
		if selected_month.get()==a:
			selected_month_number=months.index(a)+1


	#"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"

	#~~~~~~~~~~~~~~~~~~~~~~ updating positions ~~~~~~~~~~~~~~~~~~~~~~~

	#habitude.place(x=(window_width/2),y=(0))
	dropdown_night_day.place(x=placement_unit_x*0.5, y=placement_unit_y*18)

	dropdown_list_month.place(x=(placement_unit_x*0.45), y=(placement_unit_y*4.5))
	monthlabel.place(x=placement_unit_x*0.5, y=placement_unit_y*3.8)

	dropdown_list_day.place(x=(placement_unit_x*4.45), y=(placement_unit_y*4.5))
	daylabel.place(x=(placement_unit_x*4.5), y=(placement_unit_y*3.8))

	dropdown_list_importance.place(x=(placement_unit_x*0.45), y=(placement_unit_y*8.5))

	#am_or_pm.place(x=(placement_unit_x*0.5), y=(placement_unit_y*9.5))

	dropdown_list_hour.place(x=(placement_unit_x*0.45), y=(placement_unit_y*6.5))
	hours.place(x=(placement_unit_x*0.5), y=(placement_unit_y*5.8))

	dropdown_list_minutes.place(x=(placement_unit_x*4.5), y=(placement_unit_y*6.5))
	minutes.place(x=(placement_unit_x*4.55), y=(placement_unit_y*5.8))

	entry_title.place(x=placement_unit_x*0.5, y=placement_unit_y*2.5) #y based off of this, used to be 1.5

	entry_completed.place(x=(placement_unit_x*4.5), y=(placement_unit_y*8.5))

	clockTime.place(x=(window_width/2), y=0)

	not_completed_addtime.place(x=(placement_unit_x*2.5), y=(placement_unit_y*17))

	current_date.place(x=(placement_unit_x*7.5), y=(placement_unit_y*3))

	remove.place(x=(placement_unit_x*4.45), y=(placement_unit_y*9.5))

	#tasks_made.place(x=(placement_unit_x*10), y=(placement_unit_y*2.5))

	confirm.place(x=(placement_unit_x*0.5), y=(placement_unit_y*10.5))

	descbutton.place(x=placement_unit_x*3.5, y=placement_unit_y*2.59)

	current_date.place(x=placement_unit_x*4.9, y=placement_unit_y*2.59)

	settingslabel_banner.place(x=0, y=placement_unit_y*15)
	settingslabel.place(x=0, y=placement_unit_y*15)

	createeventbanner.place(x=0, y=placement_unit_y*0.9)
	createeventlabel.place(x=0, y=placement_unit_y*0.9)

	tasksbanner.place(x=(window_width/2), y=placement_unit_y*0.9)
	taskslabel.place(x=(window_width/2), y=placement_unit_y*0.9)
	tasksbg.place(x=window_width/2, y=placement_unit_y*0.9)

	#~~~~~~~~~~~~~~~~~~~~~~ window dimensions refresher ~~~~~~~~~~~~~~~~~~~~~~~



	if selected_theme.get() == "Light":

		#if device_os == "Darwin": #macOS operating system name

			window.configure(bg="azure2")
			clockTime.config(bg="sienna1")
			banner.config(bg="sienna1")
			dropdown_list_month.config(bg="azure2")
			dropdown_night_day.config(bg="azure2")
			dropdown_list_month.config(bg="azure2")
			dropdown_list_minutes.config(bg="azure2")
			dropdown_list_hour.config(bg="azure2")
			dropdown_list_importance.config(bg="azure2")
			dropdown_list_day.config(bg="azure2")
			#am_or_pm.config(bg="azure2")
			entry_title.config(highlightbackground = "azure2")
			entry_title.config(bg = "azure3")
			entry_title.config(bd = 1.5)
			entry_title.config(relief="ridge")
			descbutton.config(highlightbackground="azure2")
			descbutton.config(fg="black")
			current_date.config(fg="black")
			current_date.config(highlightbackground="azure2")
			remove.config(highlightbackground="azure2")
			remove.config(fg="black")
			confirm.config(highlightbackground="azure2")
			confirm.config(fg="black")
			entry_completed.config(highlightbackground = "azure2")
			entry_completed.config(bg = "azure3")
			entry_completed.config(bd = 1.5)
			entry_completed.config(relief="ridge")
			not_completed_addtime.config(highlightbackground = "azure2")
			not_completed_addtime.config(bg = "azure3")
			not_completed_addtime.config(bd = 1.5)
			not_completed_addtime.config(relief="ridge")
			settingslabel.config(bg="sienna1")
			settingslabel.config(fg="black")
			createeventlabel.config(bg="sienna1")
			createeventlabel.config(fg="black")
			taskslabel.config(bg="tomato3")
			taskslabel.config(fg="black")
			tasksbanner.config(bg="tomato3")
			tasksbg.config(bg="snow3")
			createeventbanner.config(bg="sienna1")
			settingslabel_banner.config(bg="sienna1")

	if selected_theme.get() == "Dark":

		#if device_os == "Darwin": #macOS operating system name

			"""
			window.configure(bg="light slate gray")
			banner.config(bg="deepskyblue3")
			clockTime.config(bg="deepskyblue3")
			dropdown_list_month.config(bg="light slate gray")
			dropdown_night_day.config(bg="light slate gray")
			dropdown_list_month.config(bg="light slate gray")
			dropdown_list_minutes.config(bg="light slate gray")
			dropdown_list_hour.config(bg="light slate gray")
			dropdown_list_importance.config(bg="light slate gray")
			dropdown_list_day.config(bg="light slate gray")
			am_or_pm.config(bg="light slate gray")
			entry_title.config(highlightbackground = "gray")
			entry_title.config(bg = "gray")
			entry_title.config(bd = 1.5)
			descbutton.config(highlightbackground="light slate gray")
			descbutton.config(fg="black")
			current_date.config(highlightbackground="light slate gray")
			current_date.config(fg="black")
			confirm.config(highlightbackground="light slate gray")
			confirm.config(fg="black")
			entry_completed.config(highlightbackground = "light slate gray")
			entry_completed.config(bg = "gray")
			entry_completed.config(bd = 1.5)
			remove.config(highlightbackground="light slate gray")
			remove.config(fg="black")
			not_completed_addtime.config(highlightbackground = "light slate gray")
			not_completed_addtime.config(bg = "gray")
			not_completed_addtime.config(bd = 1.5)
			not_completed_addtime.config(relief="ridge")
			settingslabel.config(bg="deepskyblue3")
			settingslabel.config(fg="white")
			createeventlabel.config(bg="deepskyblue3")
			createeventlabel.config(fg="white")
			taskslabel.config(bg="mediumpurple2")
			taskslabel.config(fg="white")
			tasksbanner.config(bg="mediumpurple2")
			createeventbanner.config(bg="deepskyblue3")
			settingslabel_banner.config(bg="deepskyblue3")
			tasksbg.config(bg="dark slate gray")

			"""

			window.configure(bg="dark slate gray")
			banner.config(bg="deepskyblue3")
			clockTime.config(bg="deepskyblue3")
			dropdown_list_month.config(bg="dark slate gray")
			dropdown_night_day.config(bg="dark slate gray")
			dropdown_list_month.config(bg="dark slate gray")
			dropdown_list_minutes.config(bg="dark slate gray")
			dropdown_list_hour.config(bg="dark slate gray")
			dropdown_list_importance.config(bg="dark slate gray")
			dropdown_list_day.config(bg="dark slate gray")
			#am_or_pm.config(bg="dark slate gray")
			entry_title.config(highlightbackground = "gray")
			entry_title.config(bg = "gray")
			entry_title.config(bd = 1.5)
			entry_title.config(relief="ridge")
			descbutton.config(highlightbackground="dark slate gray")
			descbutton.config(fg="black")
			current_date.config(highlightbackground="dark slate gray")
			current_date.config(fg="black")
			confirm.config(highlightbackground="dark slate gray")
			confirm.config(fg="black")
			entry_completed.config(highlightbackground = "dark slate gray")
			entry_completed.config(bg = "gray")
			entry_completed.config(bd = 1.5)
			remove.config(highlightbackground="dark slate gray")
			remove.config(fg="black")
			not_completed_addtime.config(highlightbackground = "dark slate gray")
			not_completed_addtime.config(bg = "gray")
			not_completed_addtime.config(bd = 1.5)
			not_completed_addtime.config(relief="ridge")
			settingslabel.config(bg="deepskyblue3")
			settingslabel.config(fg="white")
			createeventlabel.config(bg="deepskyblue3")
			createeventlabel.config(fg="white")
			taskslabel.config(bg="mediumpurple2")
			taskslabel.config(fg="white")
			tasksbanner.config(bg="mediumpurple2")
			createeventbanner.config(bg="deepskyblue3")
			settingslabel_banner.config(bg="deepskyblue3")
			tasksbg.config(bg="light slate gray")


	#print(selected_theme.get())
	"""
	print("width")
	print(window_width)
	print("height")
	print(window_height)
	print("placement unit x")
	print(placement_unit_x)
	print("placement unit y")
	print(placement_unit_y)
	print()
	"""

	#print(str(veryimportanttasks_holder.get()))
	#print(str(importanttasks_holder.get()))
	#print(str(notimportanttasks_holder.get()))

	#print(veryimportanttasks)


	for event in veryimportanttasks:

		print(event.datetime)

	x = ""

	for i in tasks:

		x = x+i.strng+"\n" 
	
	reminder_holder.set(x)







	#~~~~~~~~~~~~~~~~~~~~~~~ ordering lists ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	templst = []
	for event in veryimportanttasks:
		CurrentTime = time.strftime("%m:%d:%H:%M")
		#eventTime=str(event.month + ":" + event.day + ":" + event.hour + ":" + event.minute)
		
		datetimeCurrent = datetime.strptime(CurrentTime, "%m:%d:%H:%M")

		datetimeEvent = event.datetime

		delta = datetimeEvent - datetimeCurrent
		deltaSeconds = delta.total_seconds()

		#print(delta)
		#print("seconds ", delta.total_seconds())

		if templst == []:

			templst.append(event)

		else: #sort list

			for n in range(len(templst)-1):

				if templst[n].datetime.total_seconds() < deltaSeconds and templst[n+1].datetime.total_seconds() > deltaSeconds:

					templst.insert(n+1, event)

				else:

					templst.append(event)


		


	#~~~~~~~~~~~~~~~~~~~~~~ countdown timer ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	#24:00:00 -> 23:59:59

	for event in tasks:
		currmonthend=month_ends[TimeMonth]
		if TimeDay != currmonthend and event.month == TimeMonth and TimeDay == event.day:
			hoursuntilevent = int(event.hour) - int(TimeHour) 

			if int(event.minute)>=int(TimeMinute):
				minuntilevent = int(event.minute) - int(TimeMinute)
			else:
				minuntilevent = (60 - int(TimeMinute))+int(event.minute)
				#print(minuntilevent)
				#print(TimeHour)
				hoursuntilevent=hoursuntilevent-1


		
		
		#print("hours until event: " + str(hoursuntilevent))
		#print("minutes until event: " + str(minuntilevent))

		if TimeDay == event.day and TimeMonth == event.month:

			tempcount=event
			tempvar = (str(hoursuntilevent).zfill(2) + ":" + str(minuntilevent).zfill(2))
			tempcount.countdown=tempvar
			event.strng = (str(event.importance)+" "+str(event.title)+" - "+ str(event.month)+" "+str(event.day)+" • "+str(event.hour)+":"+str(event.minute)+"\n"+str(event.desc)+"\n"+str(tempvar))

	for event in veryimportanttasks:
		currmonthend=month_ends[TimeMonth]
		if TimeDay != currmonthend and event.month == TimeMonth and TimeDay == event.day:
			hoursuntilevent = int(event.hour) - int(TimeHour) 

			if int(event.minute)>=int(TimeMinute):
				minuntilevent = int(event.minute) - int(TimeMinute)
			else:
				minuntilevent = (60 - int(TimeMinute))+int(event.minute)
				#print(minuntilevent)
				#print(TimeHour)
				hoursuntilevent=hoursuntilevent-1

		x=""
		for i in veryimportanttasks:

			x = x+i.strng+"\n" 

		veryimportanttasks_holder.set(x)



		
		
		#print("hours until event: " + str(hoursuntilevent))
		#print("minutes until event: " + str(minuntilevent))

		if TimeDay == event.day and TimeMonth == event.month:

			tempcount=event
			tempvar = (str(hoursuntilevent).zfill(2) + ":" + str(minuntilevent).zfill(2))
			tempcount.countdown=tempvar
			event.strng = (str(event.importance)+" "+str(event.title)+" - "+ str(event.month)+" "+str(event.day)+" • "+str(event.hour)+":"+str(event.minute)+"\n"+str(event.desc)+"\n"+str(tempvar))

	for event in importanttasks:
		currmonthend=month_ends[TimeMonth]
		if TimeDay != currmonthend and event.month == TimeMonth and TimeDay == event.day:
			hoursuntilevent = int(event.hour) - int(TimeHour) 

			if int(event.minute)>=int(TimeMinute):
				minuntilevent = int(event.minute) - int(TimeMinute)
			else:
				minuntilevent = (60 - int(TimeMinute))+int(event.minute)
				#print(minuntilevent)
				#print(TimeHour)
				hoursuntilevent=hoursuntilevent-1
	
		x=""
	
		for i in importanttasks:

			x = x+i.strng+"\n" 

		importanttasks_holder.set(x)

		
		
		#print("hours until event: " + str(hoursuntilevent))
		#print("minutes until event: " + str(minuntilevent))

		if TimeDay == event.day and TimeMonth == event.month:

			tempcount=event
			tempvar = (str(hoursuntilevent).zfill(2) + ":" + str(minuntilevent).zfill(2))
			tempcount.countdown=tempvar
			event.strng = (str(event.importance)+" "+str(event.title)+" - "+ str(event.month)+" "+str(event.day)+" • "+str(event.hour)+":"+str(event.minute)+"\n"+str(event.desc)+"\n"+str(tempvar))


	for event in notimportanttasks:
		currmonthend=month_ends[TimeMonth]
		if TimeDay != currmonthend and event.month == TimeMonth and TimeDay == event.day:
			hoursuntilevent = int(event.hour) - int(TimeHour) 

			if int(event.minute)>=int(TimeMinute):
				minuntilevent = int(event.minute) - int(TimeMinute)
			else:
				minuntilevent = (60 - int(TimeMinute))+int(event.minute)
				#print(minuntilevent)
				#print(TimeHour)
				hoursuntilevent=hoursuntilevent-1

		x=""
		for i in notimportanttasks:

			x = x+i.strng+"\n" 

		notimportanttasks_holder.set(x)


		
		
		#print("hours until event: " + str(hoursuntilevent))
		#print("minutes until event: " + str(minuntilevent))

		if TimeDay == event.day and TimeMonth == event.month:

			tempcount=event
			tempvar = (str(hoursuntilevent).zfill(2) + ":" + str(minuntilevent).zfill(2))
			tempcount.countdown=tempvar
			event.strng = (str(event.importance)+" "+str(event.title)+" - "+ str(event.month)+" "+str(event.day)+" • "+str(event.hour)+":"+str(event.minute)+"\n"+str(event.desc)+"\n"+str(tempvar))




	#~~~~~~~~~~~~~~~~~~~~~~ check if event is due ~~~~~~~~~~~~~~~~~~~~~~~

	for j in veryimportanttasks:

		if j.month==TimeMonth and j.day==TimeDay and j.hour==TimeHour and j.minute==TimeMinute:
			answer = messagebox.askquestion("Timer", j.title + " is due. Is it complete?", icon='warning')

			if answer == "yes":
				
				RemoveEvent(j)


			elif answer == "no":
				hoursuntilevent=hoursuntilevent+1
				tempj = j
				RemoveEvent(j)

				if int(TimeMinute) >= int(60-int(addtime.get())) and int(TimeMinute) <= 59:

					tempj.minute = str(int(tempj.minute) + int(addtime.get()) - 60)
					tempj.hour = str(int(tempj.hour))

				else:
					
					tempj.minute = str(int(tempj.minute) + int(addtime.get()))
				
				AddEvent(tempj)

	for j in importanttasks:

		if j.month==TimeMonth and j.day==TimeDay and j.hour==TimeHour and j.minute==TimeMinute:
			answer = messagebox.askquestion("Timer", j.title + " is due. Is it complete?", icon='warning')

			if answer == "yes":
				
				RemoveEvent(j)


			elif answer == "no":
				hoursuntilevent=hoursuntilevent+1
				tempj = j
				RemoveEvent(j)

				if int(TimeMinute) >= int(60-int(addtime.get())) and int(TimeMinute) <= 59:

					tempj.minute = str(int(tempj.minute) + int(addtime.get()) - 60)
					tempj.hour = str(int(tempj.hour))

				else:
					
					tempj.minute = str(int(tempj.minute) + int(addtime.get()))
				
				AddEvent(tempj)


	for j in notimportanttasks:

		if j.month==TimeMonth and j.day==TimeDay and j.hour==TimeHour and j.minute==TimeMinute:
			answer = messagebox.askquestion("Timer", j.title + " is due. Is it complete?", icon='warning')

			if answer == "yes":
				
				RemoveEvent(j)


			elif answer == "no":
				hoursuntilevent=hoursuntilevent+1
				tempj = j
				RemoveEvent(j)

				if int(TimeMinute) >= int(60-int(addtime.get())) and int(TimeMinute) <= 59:

					tempj.minute = str(int(tempj.minute) + int(addtime.get()) - 60)
					tempj.hour = str(int(tempj.hour))

				else:
					
					tempj.minute = str(int(tempj.minute) + int(addtime.get()))
				
				AddEvent(tempj)



	if len(to_be_deleted)>0:
					
		tasks_shown = [i for j, i in enumerate(tasks_shown) if j not in to_be_deleted]

	clockTime.after(100,tick)
	



def remove_by_name(item_to_remove):

	x=""

	
	#for i in tasks_shown:
#
#		if item_to_remove in i:

#			tasks_shown.remove(i)
	

#      -----------TASKS-------------
	for i in tasks:

		event_title = i.title

		if item_to_remove == event_title:

			tasks.remove(i)
			#print("task delete")

	x=""

	for i in tasks:

		x = x+i.strng+"\n" 

	reminder_holder.set(x)



#   ------------VeryImporant--------------
	for i in veryimportanttasks:

		event_title = i.title

		if item_to_remove == event_title:

			veryimportanttasks.remove(i)
			#print("verimportnat delete")

	x=""

	for i in veryimportanttasks:

		x = x+i.strng+"\n" 

	
	veryimportanttasks_holder.set(x)

#--------------Imporant---------------

	for i in importanttasks:

		event_title = i.title

		if item_to_remove == event_title:

			importanttasks.remove(i)
			#print("imporatn delete")

	x=""

	for i in importanttasks:

		x = x+i.strng+"\n" 

	importanttasks_holder.set(x)

#-----------------NotImporant------------

	for i in notimportanttasks:

		event_title = i.title

		if item_to_remove == event_title:

			notimportanttasks.remove(i)

	x=""

	for i in notimportanttasks:

		x = x+i.strng+"\n" 

	notimportanttasks_holder.set(x)


def AddEvent(event):
	tasks.append(event)
	x = ""

	for i in veryimportanttasks:

		x = x+i.strng+"\n"

	reminder_holder.set(x)

	#tasks_shown.append(str(event.importance)+" "+str(event.title)+" - "+ str(event.month)+" "+str(event.day)+" • "+str(event.hour)+":"+str(event.minute)+"\n"+str(event.desc)+"\n"+str(event.countdown))

	if event.importance == "Very Important":

		veryimportanttasks.append(event)

		x = ""

		for i in veryimportanttasks:

			x = x+i.strng+"\n"

		veryimportanttasks_holder.set(x)

	elif event.importance == "Important":

		importanttasks.append(event)

		x = ""

		for i in importanttasks:

			x = x+i.strng+"\n"

		importanttasks_holder.set(x)

	elif event.importance == "Not Important":

		notimportanttasks.append(event)

		x = ""

		for i in notimportanttasks:

			x = x+i.strng+"\n"

		notimportanttasks_holder.set(x)

	x=""



def RemoveEvent(event):
	
	tasks.remove(event)

	"""

	x=""

	for i in tasks:

		if event.title in i.strng:

			tasks.remove(i)

		x = x+i.strng+"\n"

	reminder_holder.set(x)
	
	"""

def remove_event_button():

	remove_by_name(str(completed.get()))

remove = tk.Button(window, text="Remove", command=remove_event_button, fg="white", bg="sienna1")
remove.place(x=(placement_unit_x*7.5), y=(placement_unit_y*7))

#print(window.winfo_width()/2)

#tasks_made=tk.Label(window, textvariable=reminder_holder,fg="white", bg="grey60") ------------------------------------------------------- task made
#tasks_made.place(x=(placement_unit_x*12), y=(placement_unit_y*1.5))
tasks_made_veryimortant=tk.Label(window, textvariable=veryimportanttasks_holder,fg="white", bg="grey60", wraplength=900)
tasks_made_veryimortant.place(x=(placement_unit_x*10.2), y=(placement_unit_y*2.5))

tasks_made_imortant=tk.Label(window, textvariable=importanttasks_holder,fg="white", bg="grey60", wraplength=900)
tasks_made_imortant.place(x=(placement_unit_x*10.2), y=(placement_unit_y*7.5))

tasks_made_notimortant=tk.Label(window, textvariable=notimportanttasks_holder,fg="white", bg="grey60", wraplength=900)
tasks_made_notimortant.place(x=(placement_unit_x*10.2), y=(placement_unit_y*12.5))



def reminder_confirm():

	unique_title = True

	correct_time = False

	

	for event in tasks:

		event_title = event.title

		if title.get() == event_title:

			unique_title = False
			messagebox.showerror(title="Invalid Title", message="Your title needs to be unique and not the same as a different one.")



	if selected_month_number>=int(time.strftime("%m")):
		#print("1")
		if selected_month_number==int(time.strftime("%m")):
			#print("2")
			if int(selected_day.get())>=int(time.strftime("%e")):
				#print("3")
				
				if int(selected_day.get())==int(time.strftime("%e")):
					#print("4")
					if int(selected_hour.get())>=int(time.strftime("%H")):  
						#print("5")
						
						if int(selected_hour.get())==int(time.strftime("%H")):
							#print("6")
							if int(selected_minutes.get())>int(time.strftime("%M")):
								#print("7")
								correct_time=True
						else:
							correct_time=True

				else:
					correct_time=True
		else:
			correct_time=True
								              
	if correct_time==False:
		messagebox.showerror(title="Invalid Alarm", message="Your alarm needs to be set at a date that has not passed yet.")


	if unique_title == True and correct_time==True:

		tempvar = Assignment(title.get(), descstr, selected_importance.get(), selected_month.get(), selected_day.get(), selected_hour.get(), selected_minutes.get(), "") 
		AddEvent(tempvar)

	x=""

	for i in tasks_shown:

		x = x+i+"\n"

	reminder_holder.set(x)

def description_window():

	descwindow = tk.Tk()
	descwindow.title("Enter Description")
	descwindow.geometry(str(int(screen_width/3.5)) + "x" + str(int(screen_height/3.5)))
	placement_unit_x = (window.winfo_screenwidth()/3.5)/20
	placement_unit_y = (window.winfo_screenheight()/3.5)/20

	desctext = Text(descwindow, height = 10, width = 47)
	desctext.place(x=placement_unit_x*3, y=placement_unit_y*2)

	def done():
		global descstr 
		descstr = str(desctext.get("1.0", 'end-1c'))
		if len(descstr) < 100:

			descwindow.destroy()

		else:

			messagebox.showerror(title="Passed Character Limit", message="Your description should be under 100 characters.")

	donebutton = Button(descwindow, text="Done", command=done)
	donebutton.place(x=placement_unit_x*17, y=placement_unit_y*17)

	if selected_theme.get() == "Light":

		descwindow.configure(bg="azure2")
		desctext.configure(bg="azure3")
		donebutton.configure(highlightbackground="azure2", fg="black")

	if selected_theme.get() == "Dark":

		descwindow.configure(bg="dark slate gray")
		desctext.configure(bg="gray")
		donebutton.configure(highlightbackground="dark slate gray", fg="black")



#	description = tk.Text(descwindow, wrap = WORD, padx = 10, pady = 10, width = screen_width/3 - 10, height = screen_height/4 - 10)
	#description.pack()


confirm = tk.Button(window, text="Enter", command=reminder_confirm, fg="white", bg="sienna1")
confirm.place(x=(placement_unit_x*2.5), y=(placement_unit_y*7))

descbutton = tk.Button(window, text="Description", command=description_window, fg="white")
descbutton.place(x=placement_unit_x*5, y=placement_unit_y)

tick()
clockChange()
window.mainloop()