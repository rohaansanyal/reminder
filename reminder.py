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
import os
import pandas as pd
import csv
import atexit
from pathlib import Path

#-------------------------------------------------------------------------------------------------------------------------------------------------

window = tk.Tk()
window.title("Habitude")
window.option_add('*Font', '1')
device_os = str(platform.system())

screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
window.geometry(str(screen_width) + "x" + str(screen_height))
window_width=window.winfo_width()
window_height=window.winfo_height()
placement_unit_x = window.winfo_screenwidth()/20
placement_unit_y = window.winfo_screenheight()/20

TimeMonth=time.strftime("%B")#current time of the day in a certin form to check the task
TimeDay=time.strftime("%d")
TimeHour=time.strftime("%H")
TimeMinute=time.strftime("%M")
CurrentTime = time.strftime("%y:%m:%d:%H:%M")
datetimeCurrent = datetime.strptime(CurrentTime, "%y:%m:%d:%H:%M")

#-------------------------------------------------------------------------------------------------------------------------------------------------

description = "Test"

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

tasks = []

tasks_shown = []

veryimportanttasks = []
importanttasks = []
notimportanttasks = []

noFiveMinCheck = False

#-------------------------------------------------------------------------------------------------------------------------------------------------

banner = tk.Label(window, text=" "*1000, fg="white", bg="grey60")#top orange line withe the time
banner.place(x=(0),y=(0))


title = tk.StringVar(window, "Title")
entry_title = tk.Entry(window, text=title)
entry_title.place(x=placement_unit_x*1.5, y=placement_unit_y)


selected_month = tk.StringVar(window)
selected_month.set(months[0])
dropdown_list_month = tk.OptionMenu(window, selected_month, *months)
dropdown_list_month.place(x=(placement_unit_x*1), y=(placement_unit_y*3))
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
minuteslabel = tk.Label(window, text="Minutes", fg="white", bg="grey60")
minuteslabel.place(x=(placement_unit_x*7.5), y=(placement_unit_y*5))


important = ["Very Important", "Important", "Not Important"]
selected_importance = tk.StringVar(window)
selected_importance.set(important[0]) 
dropdown_list_importance = tk.OptionMenu(window, selected_importance, *important)
dropdown_list_importance.place(x=(placement_unit_x*2.5), y=(placement_unit_y*7))


night_day = ["Light", "Dark"]
selected_theme = tk.StringVar(window)
selected_theme.set(night_day[0])
dropdown_night_day = tk.OptionMenu(window, selected_theme, *night_day)
dropdown_night_day.place(x=placement_unit_x*1, y=placement_unit_y*18)





clockTime = tk.Label(window, text=" ", bg="sienna1")
clockTime.place(x=(window_width/2), y=0)




reminder_holder = tk.StringVar(window, "")
veryimportanttasks_holder = tk.StringVar(window, "")
importanttasks_holder = tk.StringVar(window, "")
notimportanttasks_holder = tk.StringVar(window, "")

topveryimportant_holder = tk.StringVar(window, "")
topimportant_holder = tk.StringVar(window,"")
topnotimportant_holder = tk.StringVar(window,"")




completed = tk.StringVar(window, "Event to Remove")

to_remove = []

entry_completed = tk.Entry(window, text=completed)
entry_completed.place(x=(placement_unit_x*7.5), y=(placement_unit_y*8))


addtime = tk.StringVar(window, "10")
not_completed_addtime = tk.Entry(window, text=addtime)
not_completed_addtime.place(x=(placement_unit_x*1.5), y=(placement_unit_y*16.5))

snoozeLabel = tk.Label(window, text="Snooze Time", bg = "sienna1")
snoozeLabel.place(x=(placement_unit_x*0.5), y =(placement_unit_y*16.5))

def set_current_date():
	selected_day.set(time.strftime("%d"))
	selected_month.set(time.strftime("%B"))
	selected_hour.set(time.strftime("%H"))
	selected_minutes.set(time.strftime("%M"))


def set_for_five():
	x = datetime.strptime(time.strftime("%y:%m:%d:%H:%M"), "%y:%m:%d:%H:%M") + timedelta(minutes= 5)

	selected_day.set(x.strftime("%d"))
	selected_month.set(x.strftime("%B"))
	selected_hour.set(x.strftime("%H"))
	selected_minutes.set(x.strftime("%M"))

	noFiveMinCheck = True

	#make it so that when task made it doesn't ask if task is done because it is done in 5
	

def notify(time, title): 

	if time == '0 minutes':

		answer = messagebox.askquestion("Timer", str(title) + " is due. Is it complete?", icon='warning')

	else:

		answer = messagebox.askquestion("Timer", str(title) + " is due in " + str(time) + ". Is it complete?", icon='warning')

	return answer


current_date = tk.Button(window, text="Set Current Time", command=set_current_date, fg="white", bg="sienna1")
current_date.place(x=(placement_unit_x*7.5), y=(placement_unit_y*1.5))

inFive = tk.Button(window, text="Set For 5 Minutes", command=set_for_five, fg="black", bg="sienna1", highlightbackground="azure2")
inFive.place(x=(placement_unit_x*6.3), y=(placement_unit_y*2.59))


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


tasks_made_veryimortant=tk.Label(window, textvariable=topveryimportant_holder, fg="white", bg="grey60", wraplength=900)
#tasks_made_veryimortant=tk.Label(window, textvariable=veryimportanttasks_holder,fg="white", bg="grey60", wraplength=900)
tasks_made_veryimortant.place(x=(placement_unit_x*10.2), y=(placement_unit_y*2.5))

tasks_made_imortant=tk.Label(window, textvariable=topimportant_holder,fg="white", bg="grey60", wraplength=900)
#tasks_made_imortant=tk.Label(window, textvariable=importanttasks_holder,fg="white", bg="grey60", wraplength=900)
tasks_made_imortant.place(x=(placement_unit_x*10.2), y=(placement_unit_y*7.5))

tasks_made_notimortant=tk.Label(window, textvariable=topnotimportant_holder,fg="white", bg="grey60", wraplength=900)
#tasks_made_notimortant=tk.Label(window, textvariable=notimportanttasks_holder,fg="white", bg="grey60", wraplength=900)
tasks_made_notimortant.place(x=(placement_unit_x*10.2), y=(placement_unit_y*12.5))

tasks_title_veryimportant=tk.Label(window, text = "Very Important Tasks",fg="white", bg="grey60", wraplength=900)
tasks_title_veryimportant.place(x=(placement_unit_x*10.2), y=(placement_unit_y*2))

tasks_title_important=tk.Label(window, text = "Important Tasks",fg="white", bg="grey60", wraplength=900)
tasks_title_important.place(x=(placement_unit_x*10.2), y=(placement_unit_y*7))

tasks_title_notimportant=tk.Label(window, text = "Not Important Tasks",fg="white", bg="grey60", wraplength=900)
tasks_title_notimportant.place(x=(placement_unit_x*10.2), y=(placement_unit_y*12))





l1 = Label(window, text = "First:")
l2 = Label(window, text = "Second:")

l1.grid(row = 0, column = 0, sticky = W, pady = 2)
l2.grid(row = 1, column = 0, sticky = W, pady = 2)
 
# entry widgets, used to take entry from user
e1 = Entry(window)
e2 = Entry(window)
 
# this will arrange entry widgets
e1.grid(row = 0, column = 1, pady = 2)
e2.grid(row = 1, column = 1, pady = 2)











month_ends = {"January":31, "February":28, "March":31, "April":30, "May":31, "June":30, "July":31, "August":31, "September":30, "October":31, "November":30, "December":31}

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
	CurrentTime = time.strftime("%y:%m:%d:%H:%M")
	datetimeCurrent = datetime.strptime(CurrentTime, "%y:%m:%d:%H:%M")


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



	#~~~~~~~~~~~~~~~~~~~~~~ updating positions ~~~~~~~~~~~~~~~~~~~~~~~

	#habitude.place(x=(window_width/2),y=(0))
	dropdown_night_day.place(x=placement_unit_x*0.5, y=placement_unit_y*18)

	dropdown_list_month.place(x=(placement_unit_x*0.45), y=(placement_unit_y*4.5))
	monthlabel.place(x=placement_unit_x*0.5, y=placement_unit_y*3.8)

	dropdown_list_day.place(x=(placement_unit_x*4.45), y=(placement_unit_y*4.5))
	daylabel.place(x=(placement_unit_x*4.5), y=(placement_unit_y*3.8))

	dropdown_list_importance.place(x=(placement_unit_x*0.45), y=(placement_unit_y*8.5))

	dropdown_list_hour.place(x=(placement_unit_x*0.45), y=(placement_unit_y*6.5))
	hours.place(x=(placement_unit_x*0.5), y=(placement_unit_y*5.8))

	dropdown_list_minutes.place(x=(placement_unit_x*4.5), y=(placement_unit_y*6.5))
	minuteslabel.place(x=(placement_unit_x*4.55), y=(placement_unit_y*5.8))

	entry_title.place(x=placement_unit_x*0.5, y=placement_unit_y*2.5) #y based off of this, used to be 1.5

	entry_completed.place(x=(placement_unit_x*4.5), y=(placement_unit_y*8.5))

	clockTime.place(x=(window_width/2), y=0)

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

	tasks_made_veryimortant.place(x=(placement_unit_x*10.2), y=(placement_unit_y*2.5))
	tasks_made_imortant.place(x=(placement_unit_x*10.2), y=(placement_unit_y*7.5))
	tasks_made_notimortant.place(x=(placement_unit_x*10.2), y=(placement_unit_y*12.5))

	tasks_title_veryimportant.place(x=(placement_unit_x*10.2), y=(placement_unit_y*2))
	tasks_title_important.place(x=(placement_unit_x*10.2), y=(placement_unit_y*7))
	tasks_title_notimportant.place(x=(placement_unit_x*10.2), y=(placement_unit_y*12))

	inFive.place(x=(placement_unit_x*6.8), y=(placement_unit_y*2.59))

	clearveryimportant.place(x=(placement_unit_x*12.2), y=(placement_unit_y*2))
	clearimportant.place(x=(placement_unit_x*11.8), y=(placement_unit_y*7))
	clearnotimportant.place(x=(placement_unit_x*12.2), y=(placement_unit_y*12))

	snoozeLabel.place(x=(placement_unit_x*0.5), y =(placement_unit_y*16.6))
	not_completed_addtime.place(x=(placement_unit_x*2.5), y=(placement_unit_y*16.5))

	#~~~~~~~~~~~~~~~~~~~~~~ window dimensions refresher ~~~~~~~~~~~~~~~~~~~~~~~



	if selected_theme.get() == "Light":

		#if device_os == "Darwin": #macOS operating system name

			window.configure(bg="azure2")
			clockTime.config(bg="sienna1")
			banner.config(bg="sienna1")
			dropdown_night_day.config(bg="azure2")
			dropdown_night_day.config(fg="black")
			dropdown_list_month.config(bg="azure2")
			dropdown_list_month.config(fg="black")
			dropdown_list_minutes.config(bg="azure2")
			dropdown_list_minutes.config(fg="black")
			dropdown_list_hour.config(bg="azure2")
			dropdown_list_hour.config(fg="black")
			dropdown_list_importance.config(bg="azure2")
			dropdown_list_importance.config(fg="black")
			dropdown_list_day.config(bg="azure2")
			dropdown_list_day.config(fg="black")
			#am_or_pm.config(bg="azure2")
			entry_title.config(highlightbackground = "azure2")
			entry_title.config(bg = "azure3")
			entry_title.config(bd = 1.5)
			entry_title.config(relief="ridge")
			entry_title.config(fg="black")
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
			entry_completed.config(fg="black")
			not_completed_addtime.config(highlightbackground = "azure2")
			not_completed_addtime.config(bg = "azure3")
			not_completed_addtime.config(bd = 1.5)
			not_completed_addtime.config(relief="ridge")
			not_completed_addtime.config(fg="black")
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
			tasks_made_veryimortant.config(bg="grey60")
			tasks_made_imortant.config(bg="grey60")
			tasks_made_notimortant.config(bg="grey60")
			clearveryimportant.config(highlightbackground="snow3")
			clearveryimportant.config(fg="black")
			clearimportant.config(highlightbackground="snow3")
			clearimportant.config(fg="black")
			clearnotimportant.config(highlightbackground="snow3")
			clearnotimportant.config(fg="black")


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


	x = ""

	for i in tasks:

		x = x+i.strng+"\n" 
	
	reminder_holder.set(x)



	#~~~~~~~~~~~~~~~~~~~~~~~ ordering lists ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	templst = selection_sort(veryimportanttasks,len(veryimportanttasks))
	importanttemplst = selection_sort(importanttasks, len(importanttasks))
	notimportanttemplst = selection_sort(notimportanttasks, len(notimportanttasks))

	#~~~~~~~~~~~~~~~~~~~~~~ countdown timer ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	for event in tasks:

		currmonthend=month_ends[TimeMonth]
		if TimeDay != currmonthend and event.month == TimeMonth and TimeDay == event.day:
			hoursuntilevent = int(event.hour) - int(TimeHour) 

			if int(event.minute)>=int(TimeMinute):
				minuntilevent = int(event.minute) - int(TimeMinute)
			else:
				minuntilevent = (60 - int(TimeMinute))+int(event.minute)

				hoursuntilevent=hoursuntilevent-1


		
	

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

		if len(veryimportanttasks) >= 3:
			x = veryimportanttasks[0].strng+"\n"+veryimportanttasks[1].strng+"\n"+veryimportanttasks[2].strng
		elif len(veryimportanttasks) > 0:
			x=""
			for event in veryimportanttasks:
				x = x + (event.strng+"\n")
		else:
			x=""

		topveryimportant_holder.set(x)



		
		
		
		

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
	
		if len(importanttasks) >= 3:
			x = importanttasks[0].strng+"\n"+importanttasks[1].strng+"\n"+importanttasks[2].strng
		elif len(importanttasks) > 0:
			x=""
			for event in importanttasks:
				x = x + (event.strng+"\n")
		else:
			x=""

		topimportant_holder.set(x)
		
		
		
		

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

		if len(notimportanttasks) >= 3:
			x = notimportanttasks[0].strng+"\n"+notimportanttasks[1].strng+"\n"+notimportanttasks[2].strng
		elif len(notimportanttasks) > 0:
			x=""
			for event in notimportanttasks:
				x = x + (event.strng+"\n")
		else:
			x=""

		topnotimportant_holder.set(x)

		
		
		
		

		if TimeDay == event.day and TimeMonth == event.month:

			tempcount=event
			tempvar = (str(hoursuntilevent).zfill(2) + ":" + str(minuntilevent).zfill(2))
			tempcount.countdown=tempvar
			event.strng = (str(event.importance)+" "+str(event.title)+" - "+ str(event.month)+" "+str(event.day)+" • "+str(event.hour)+":"+str(event.minute)+"\n"+str(event.desc)+"\n"+str(tempvar))




	#~~~~~~~~~~~~~~~~~~~~~~ check if event is due ~~~~~~~~~~~~~~~~~~~~~~~

	for j in veryimportanttasks:

		secondsaway = (j.datetime - datetimeCurrent).total_seconds()

		if secondsaway == 3600 and j.oneHourCheck == False:

			answer = notify('1 hour', j.title)

			if answer == "yes":

				RemoveEvent(j)

		j.oneHourCheck = True

		if secondsaway == 1800 and j.thirtyMinuteCheck == False:

			answer = notify('30 minutes', j.title)

			if answer == "yes":

				RemoveEvent(j)

			j.thirtyMinuteCheck = True


		if (j.datetime - datetimeCurrent).total_seconds() == 600 and j.tenMinuteCheck == False:

			answer = notify('10 minutes', j.title)

			if answer == "yes":
				
				RemoveEvent(j)

			j.tenMinuteCheck = True

		if (j.datetime - datetimeCurrent).total_seconds() == 300 and j.fiveMinuteCheck == False:

			answer = notify('5 minutes', j.title)

			if answer == "yes":
				
				RemoveEvent(j)

			j.fiveMinuteCheck = True

		if (j.datetime - datetimeCurrent).total_seconds() == 60 and j.oneMinuteCheck == False:

			answer = notify('1 minute', j.title)

			if answer == "yes":
				
				RemoveEvent(j)

			j.oneMinuteCheck = True
				

		if (j.datetime - datetimeCurrent).total_seconds() == 0:

			answer = notify('0 minutes', j.title)

			if answer == "yes":
				
				RemoveEvent(j)


			elif answer == "no":
				j.datetime = j.datetime + timedelta(minutes=int(addtime.get()))

				j.month = (j.datetime).strftime("%B")

				j.day = (j.datetime).strftime("%d")

				j.hour = (j.datetime).strftime("%H")

				j.minute = (j.datetime).strftime("%M")

				
				


	for j in importanttasks:

		secondsaway = (j.datetime - datetimeCurrent).total_seconds()

		if secondsaway == 1800 and j.thirtyMinuteCheck == False:

			answer = notify('30 minutes', j.title)

			if answer == "yes":

				RemoveEvent(j)

			j.thirtyMinuteCheck = True

		if (j.datetime - datetimeCurrent).total_seconds() == 600 and j.tenMinuteCheck == False:

			answer = notify('10 minutes', j.title)

			if answer == "yes":
				
				RemoveEvent(j)

			j.tenMinuteCheck = True	

		if (j.datetime - datetimeCurrent).total_seconds() == 60 and j.oneMinuteCheck == False:

			answer = notify('1 minute', j.title)

			if answer == "yes":
				
				RemoveEvent(j)

			j.oneMinuteCheck = True

		if secondsaway == 0:

			answer = notify('0 minutes', j.title)

			if answer == "yes":
				
				RemoveEvent(j)


			elif answer == "no":
				j.datetime = j.datetime + timedelta(minutes=int(addtime.get()))

				j.month = (j.datetime).strftime("%B")

				j.day = (j.datetime).strftime("%d")

				j.hour = (j.datetime).strftime("%H")

				j.minute = (j.datetime).strftime("%M")


	for j in notimportanttasks:

		secondsaway = (j.datetime - datetimeCurrent).total_seconds()

		if (j.datetime - datetimeCurrent).total_seconds() == 600 and j.tenMinuteCheck == False:

			answer = notify('10 minute', j.title)

			if answer == "yes":
				
				RemoveEvent(j)

			j.tenMinuteCheck = True

		if secondsaway == 0:

			answer = notify('0 minutes', j.title)

			if answer == "yes":
				
				RemoveEvent(j)


			elif answer == "no":
				print("no answer ran")
				j.datetime = j.datetime + timedelta(minutes=itn(addtime.get()))

				j.month = (j.datetime).strftime("%B")

				j.day = (j.datetime).strftime("%d")

				j.hour = (j.datetime).strftime("%H")

				j.minute = (j.datetime).strftime("%M")



	if len(to_be_deleted)>0:
					
		tasks_shown = [i for j, i in enumerate(tasks_shown) if j not in to_be_deleted]

	clockTime.after(100,tick)

def selection_sort(unsorted, n):
	
	sortedlst=unsorted

	def swap(arr, a, b):
	    """ swap elements a and b in an array """

	    temp = arr[a]
	    arr[a] = arr[b]
	    arr[b] = temp
	    return(arr)

	CurrentTime = time.strftime("%m:%d:%H:%M")
	datetimeCurrent = datetime.strptime(CurrentTime, "%m:%d:%H:%M")

	lstsorted = False

	for i in range(0, n):


		check_swap = False

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
				check_swap = True

		# swap ith and jth values
		sortedlst = swap(unsorted, i, min_index)

	return(sortedlst)


def AddEvent(event):
	tasks.append(event)
	x = ""

	for i in tasks: #NOT IN USE

		x = x+i.strng+"\n"

	reminder_holder.set(x)

	'''

	if (event.datetime - datetimeCurrent).total_seconds() == 60:
		event.oneMinuteCheck = True

	elif (event.datetime - datetimeCurrent).total_seconds() == 300:
		event.fiveMinuteCheck = True

	elif (event.datetime - datetimeCurrent).total_seconds() == 600:
		event.tenMinuteCheck=True

	elif (event.datetime - datetimeCurrent).total_seconds() == 1800:
		event.thirtyMinuteCheck = True

	elif (event.datetime - datetimeCurrent).total_seconds() == 3600:
		event.oneHourCheck = True


	'''
	
	if event.importance == "Very Important":

		veryimportanttasks.append(event)

		if len(veryimportanttasks) >= 3:
			x = veryimportanttasks[0].strng+"\n"+veryimportanttasks[1].strng+"\n"+veryimportanttasks[2].strng
		elif len(veryimportanttasks) > 0:
			x=""
			for event in veryimportanttasks:
				x = x + (event.strng+"\n")
		else:
			x=""

		topveryimportant_holder.set(x)

	elif event.importance == "Important":

		
		importanttasks.append(event)


		if len(importanttasks) >= 3:
			x = importanttasks[0].strng+"\n"+importanttasks[1].strng+"\n"+importanttasks[2].strng
		elif len(importanttasks) > 0:
			x=""
			for event in importanttasks:
				x = x + (event.strng+"\n")
		else:
			x=""

		topimportant_holder.set(x)

	elif event.importance == "Not Important":

		
		notimportanttasks.append(event)

		if len(notimportanttasks) >= 3:
			x = notimportanttasks[0].strng+"\n"+notimportanttasks[1].strng+"\n"+notimportanttasks[2].strng
		elif len(notimportanttasks) > 0:
			x=""
			for event in notimportanttasks:
				x = x + (event.strng+"\n")
		else:
			x=""

		topnotimportant_holder.set(x)

	x=""

categories = ['name', 'desc', 'month', 'day', 'hour', 'minute']

path = Path(os.getcwd() + "/veryimportant.csv")

if os.path.isfile(path) == True:

	pass

else:

	with open('veryimportant.csv', 'w') as csvfile:

		vi_csvwriter = csv.writer(csvfile)
		vi_csvwriter.writerow(categories)

path = Path(os.getcwd() + "/important.csv")

if os.path.isfile(path) == True:

	pass

else:

	with open('important.csv', 'w') as csvfile:

		i_csvwriter = csv.writer(csvfile)
		i_csvwriter.writerow(categories)

path = Path(os.getcwd() + "/notimportant.csv")

if os.path.isfile(path) == True:

	pass

else:

	with open('notimportant.csv', 'w') as csvfile:

		ni_csvwriter = csv.writer(csvfile)
		ni_csvwriter.writerow(categories)	

veryimportantdf = pd.read_csv('veryimportant.csv')
importantdf = pd.read_csv('important.csv')
notimportantdf = pd.read_csv('notimportant.csv')

veryimportantdf = veryimportantdf.fillna(" ")
importantdf = importantdf.fillna(" ")
notimportantdf = notimportantdf.fillna(" ")

print("initial reading of veryimportantdf")
print(veryimportantdf)

if veryimportantdf.empty == False:

	for col, row in veryimportantdf.iterrows():

		AddEvent(Assignment(row['name'], row['desc'], 'Very Important', str(row['month']), str(row['day']), str(row['hour']), str(row['minute']), ''))

if importantdf.empty == False:

	for col, row in importantdf.iterrows():

		AddEvent(Assignment(row['name'], row['desc'], 'Important', str(row['month']), str(row['day']), str(row['hour']), str(row['minute']), ''))

if notimportantdf.empty == False:

	for col, row in notimportantdf.iterrows():

		AddEvent(Assignment(row['name'], row['desc'], 'Not Important', str(row['month']), str(row['day']), str(row['hour']), str(row['minute']), ''))

veryimportantdf = veryimportantdf[0:0]
importantdf = importantdf[0:0]
notimportantdf = notimportantdf[0:0]

#with open('veryimportant.csv', 'w') as csvfile:

	
	#csvwriter = csv.writer(csvfile)
	#csvfile.truncate()
	#for i in len('veryimportant.csv'): -----------------------------------------------to clear file-------------------------------------------------not work
	#	csvwriter.drop(i)


def ExitFunction(arg):



	for event in veryimportanttasks:

		veryimportantdf.loc[len(veryimportantdf.index)] = [event.title, event.desc, event.month, event.day, event.hour, event.minute]

	for event in importanttasks:

		importantdf.loc[len(importantdf.index)] = [event.title, event.desc, event.month, event.day, event.hour, event.minute]

	for event in notimportanttasks:

		notimportantdf.loc[len(notimportantdf.index)] = [event.title, event.desc, event.month, event.day, event.hour, event.minute]

	#veryimportantdf.drop_duplicates()
	#importantdf.drop_duplicates()
	#notimportantdf.drop_duplicates()

	print("\nfinal reading of veryimportantdf")
	print(veryimportantdf)

	with open('veryimportant.csv', 'w') as csvfile:

		csvwriter = csv.writer(csvfile)
		veryimportantdf.to_csv('veryimportant.csv', mode='w', index=False, header=True) 

	with open('important.csv', 'w') as csvfile:

		csvwriter = csv.writer(csvfile)
		importantdf.to_csv('important.csv', mode='w', index=False, header=True)

	with open('notimportant.csv', 'w') as csvfile:

		csvwriter = csv.writer(csvfile)
		notimportantdf.to_csv('notimportant.csv', mode='w', index=False, header=True)

	print(arg)

atexit.register(ExitFunction, 'Program closed.')


def RemoveEvent(event):
	tasks.remove(event)
	x = ""

	for i in tasks:

		x = x+i.strng+"\n"

	reminder_holder.set(x)

	if event.importance == "Very Important":
	
		veryimportanttasks.remove(event)

		if len(veryimportanttasks) >= 3:
			x = veryimportanttasks[0].strng+"\n"+veryimportanttasks[1].strng+"\n"+veryimportanttasks[2].strng
		elif len(veryimportanttasks) > 0:
			x=""
			for event in veryimportanttasks:
				x = x + (event.strng+"\n")
		else:
			x=""

		topveryimportant_holder.set(x)

	elif event.importance == "Important":

		importanttasks.remove(event)

		if len(importanttasks) >= 3:
			x = importanttasks[0].strng+"\n"+importanttasks[1].strng+"\n"+importanttasks[2].strng
		elif len(importanttasks) > 0:
			x=""
			for event in importanttasks:
				x = x + (event.strng+"\n")
		else:
			x=""

		topimportant_holder.set(x)

		#importantdf.drop(importantdf.loc[importantdf['name'] == event.title].index)

	elif event.importance == "Not Important":

		notimportanttasks.remove(event)

		if len(notimportanttasks) >= 3:
			x = notimportanttasks[0].strng+"\n"+notimportanttasks[1].strng+"\n"+notimportanttasks[2].strng
		elif len(notimportanttasks) > 0:
			x=""
			for event in notimportanttasks:
				x = x + (event.strng+"\n")
		else:
			x=""

		topnotimportant_holder.set(x)

		#notimportantdf.drop(notimportantdf.loc[notimportantdf['name'] == event.title].index)

	x=""

#print("tasks")
#for i in tasks:
#	print(i.title)
#print("very important df")
#print(veryimportantdf)

def remove_event_button():

	eventToRemove = ""
	for event in veryimportanttasks:

		#veryimportantdf.drop(veryimportantdf.loc[veryimportantdf['name'] == event.title].index)

		event_title = event.title

		if str(completed.get()) == event_title:

			eventToRemove = event
	for event in importanttasks:

		event_title = event.title

		if str(completed.get()) == event_title:

			eventToRemove = event
	for event in notimportanttasks:

		event_title = event.title

		if str(completed.get()) == event_title:

			eventToRemove = event

	RemoveEvent(eventToRemove)

remove = tk.Button(window, text="Remove", command=remove_event_button, fg="white", bg="sienna1")
remove.place(x=(placement_unit_x*7.5), y=(placement_unit_y*7))

def tasksclear(lst):

	if lst == "very important":

		print("clearing")

		veryimportanttasks.clear()

		topveryimportant_holder.set("")

	elif lst == "important":

		importanttasks.clear()

		topimportant_holder.set("")

	elif lst == "not important":

		notimportanttasks.clear()

		topnotimportant_holder.set("")

def veryimportantclear():

	tasksclear("very important")

def importantclear():

	tasksclear("important")

def notimportantclear():

	tasksclear("not important")


clearnotimportant = tk.Button(window, text="Clear", command=notimportantclear, fg="white", bg="sienna1")
clearnotimportant.place(x=(placement_unit_x*11.5), y=(placement_unit_y*12))

clearveryimportant = tk.Button(window, text="Clear", command=veryimportantclear, fg="white", bg="sienna1")
clearveryimportant.place(x=(placement_unit_x*11.5), y=(placement_unit_y*2))

clearimportant = tk.Button(window, text="Clear", command=importantclear, fg="white", bg="sienna1")
clearimportant.place(x=(placement_unit_x*11.5), y=(placement_unit_y*7))




def reminder_confirm():

	unique_title = True

	correct_time = False

	title_length = False
	

	for event in veryimportanttasks:

		event_title = event.title

		if title.get() == event_title:

			unique_title = False
			messagebox.showerror(title="Invalid Title", message="Your title needs to be unique and not the same as a different one.")

	for event in importanttasks:

		event_title = event.title

		if title.get() == event_title:

			unique_title = False
			messagebox.showerror(title="Invalid Title", message="Your title needs to be unique and not the same as a different one.")

	for event in notimportanttasks:

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


	if len(str(title.get()))<=40:
		title_length = True 
	else:
		messagebox.showerror(title="Passed Character Limit", message="Your title should be 40 characters or less.")




	if unique_title == True and correct_time==True and title_length==True:

		tempvar = Assignment(title.get(), descstr, selected_importance.get(), selected_month.get(), selected_day.get(), selected_hour.get(), selected_minutes.get(), "") 

		

		if (tempvar.datetime - datetimeCurrent).total_seconds() == 60:
			tempvar.oneMinuteCheck = True

		elif (tempvar.datetime - datetimeCurrent).total_seconds() == 300:
			tempvar.fiveMinuteCheck = True
			print("changed 5 check to true")

		elif (tempvar.datetime - datetimeCurrent).total_seconds() == 600:
			tempvar.tenMinuteCheck=True

		elif (tempvar.datetime - datetimeCurrent).total_seconds() == 1800:
			tempvar.thirtyMinuteCheck = True

		elif (tempvar.datetime - datetimeCurrent).total_seconds() == 3600:
			tempvar.oneHourCheck = True
		

		AddEvent(tempvar)

		tempvar = ""

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

def seeMoreFunctionVI():
	descwindow = tk.Tk()
	descwindow.title("Very Important Tasks")
	descwindow.geometry(str(int(screen_width/3.5)) + "x" + str(int(screen_height/3.5)))
	placement_unit_x = (window.winfo_screenwidth()/3.5)/20
	placement_unit_y = (window.winfo_screenheight()/3.5)/20


def seeMoreFunctionI():
	descwindow = tk.Tk()
	descwindow.title("Important Tasks")
	descwindow.geometry(str(int(screen_width/3.5)) + "x" + str(int(screen_height/3.5)))
	placement_unit_x = (window.winfo_screenwidth()/3.5)/20
	placement_unit_y = (window.winfo_screenheight()/3.5)/20


def seeMoreFunctionNI():
	descwindow = tk.Tk()
	descwindow.title("Not Important Tasks")
	descwindow.geometry(str(int(screen_width/3.5)) + "x" + str(int(screen_height/3.5)))
	placement_unit_x = (window.winfo_screenwidth()/3.5)/20
	placement_unit_y = (window.winfo_screenheight()/3.5)/20




seeMoreVeryImportant = tk.Button(window, text="See More", command=seeMoreFunctionVI, fg="white", bg="sienna1")
seeMoreVeryImportant.place(x=(placement_unit_x*13), y=(placement_unit_y*2))

seeMoreImportant = tk.Button(window, text="See More", command=seeMoreFunctionI, fg="white", bg="sienna1")
seeMoreImportant.place(x=(placement_unit_x*13), y=(placement_unit_y*7))

seeMoreNotImportant = tk.Button(window, text="See More", command=seeMoreFunctionNI, fg="white", bg="sienna1")
seeMoreNotImportant.place(x=(placement_unit_x*13), y=(placement_unit_y*12))




#	description = tk.Text(descwindow, wrap = WORD, padx = 10, pady = 10, width = screen_width/3 - 10, height = screen_height/4 - 10)
	#description.pack()







confirm = tk.Button(window, text="Enter", command=reminder_confirm, fg="white", bg="sienna1")
confirm.place(x=(placement_unit_x*2.5), y=(placement_unit_y*7))

descbutton = tk.Button(window, text="Description", command=description_window, fg="white")
descbutton.place(x=placement_unit_x*5, y=placement_unit_y)

tick()
clockChange()
window.mainloop()