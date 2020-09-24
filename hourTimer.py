import datetime, time
import simpleaudio as sa

sound = sa.WaveObject.from_wave_file("bell.wav")
active = True
print ("Chiming Once per Hour")

def runTimer():
	currentTime = datetime.datetime.now()
	print ("Start Time: " + currentTime.strftime("%H:%M"))
	print ("Hours worked: 0")
	timerRunning = True
	mins = 0
	hoursWorked = 0

	while timerRunning:
		while mins < 60:
			# print ("Mins til break: " + str(60 - mins))
			time.sleep(1800)
			mins += 30
		sound.play()
		hoursWorked += 1
		currentTime = datetime.datetime.now()
		print ("Current Time: " + currentTime.strftime("%H:%M"))
		print ("Hours worked: " + str(hoursWorked))
		mins = 0
		continue

while active:
	runTimer()


	


