time = float(input("Total seconds: ")) #user input prompt in sec and converts to float

hours = int(time // 3600) # calc total hours by dividing time by 3600
minutes = int((time/ 60) % 60) # converts total time to minutes by dividing by 60 and takes the remainder (to get the minuted part of the time)
seconds = int(time % 60) # takes remainder when dividing total time by 60 to get seconds

print(f"Total time: {hours}:{minutes}:{seconds}") # formats hours minutes seconds
