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

def selection_sort(unsorted, n):
	
	def swap(arr, a, b):
	    """ swap elements a and b in an array """
	    print("-----------------SwapRan-------------------")
	    temp = arr[a]
	    arr[a] = arr[b]
	    arr[b] = temp
	    return(arr)

	CurrentTime = time.strftime("%m:%d:%H:%M")
	datetimeCurrent = datetime.strptime(CurrentTime, "%m:%d:%H:%M")

	lstsorted = False

	for i in range(0, n):
		print("------------------------------selectionSortForLoopRan-----------------------------------")

		check_swap = False

		# initialise with first value
		current_min = (unsorted[i] - datetimeCurrent).total_seconds()
		
		# min_index initialiser
		min_index = i
		
		# iterate over remaining unsorted items
		for j in range(i, n):
			
			# check if jth value is less than current min
			if (unsorted[j] - datetimeCurrent).total_seconds() < current_min:
			  
				# update minimum value and index
				current_min = (unsorted[j] - datetimeCurrent).total_seconds()
				min_index = j
				check_swap = True

		# swap ith and jth values
		sortedlst = swap(unsorted, i, min_index)

	return(sortedlst)

unsortedlst = [datetime.strptime('November 30 22 6:30', '%B %d %y %H:%M'), datetime.strptime('December 30 22 8:30', '%B %d %y %H:%M'), datetime.strptime('October 31 22 9:30', '%B %d %y %H:%M')]

print(selection_sort(unsortedlst, 3))