# bazinga_ML_winter19

PNR.py-> Python code to check and return railway pnr status 
weather.py-> Python code to show 3 consecutive day weather forecast using curl request from wttr

#drivepush

Automation of file upload and view in Google drive using google apis(further creation of alias that displays results on the teminal itself)

main.py-> Code snippet containing all functions to list,upload data

auth.py-> Code snippet to use client secter to authorise the script

listfile.py-> Code snippet to print the list of latest 50 files on drive

upload.py-> Code snippet to upload a image file to google drive

Working-
Requirements-> clientid and client secret json file need to be generated from Google Developer API
To congigure run auth.py then, the list and update function can be performed by the listfile.py and upload.py

Further configuration in linux terminal is done by 

alias gpush_up="python <path_to_upload.py>"
alias gpush_list="python <path_to_listfile.py> | cut -d '(' -f 1"

Thus the final linux command required -
gpush_list     #Lists latest updated 50 files on your google drive
gpush_up       #Uploads jpg file to google drive(the path to file needs to be given on prompt)

#PNR.py
Python script to show PNR status of user
alias chalo="python path_to_PNR.py"     #PNR number needs to be given on prompt

#weather.py
Simple python script that uses curl wttr(website giving weather data)
alias mausam="python path_to_weather.py"
