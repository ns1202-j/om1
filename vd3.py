import threading
import requests
import urllib.request
import os
import subprocess
from subprocess import Popen
import time
from omxplayer.player import OMXPlayer
from pathlib import Path

def screen():
	global screen_status
	url= 'http://143.198.132.112/smarthh/pantalla.php'
	status_code = 200
	try:
		status_code = requests.get(url,timeout = 10)
		print(status_code)

	except requests.exceptions.ConnectTimeout:
		status_code = 3
	except requests.exceptions.ConnectionError:
		status_code = 3
	if status_code == 200 or "[200]":
		query = {'lat':'45','lon':'180'}
		r = requests.post('http://143.198.132.112/smarthh/pantalla.php')
		screen_status = r.text
		print(r.text)
		#print('request realizado')
	else:print('no hubo request')
def play1():
        global player
        if(omx2.is_playing()):
                print (omx2)
                omx2.pause()
                omx2.hide_video()
                player = OMXPlayer(video)
                time.sleep(2.5)
                omx2.quit()
        else:
                player = OMXPlayer(video)
                time.sleep(2.5)
                omx2.quit()                
        
        return player

def play2():
        global omx2
        player.pause()
        player.hide_video()
        omx2 = OMXPlayer(video2)
        time.sleep(2.5)
        player.quit()
        return omx2

flag = 1
video = Path("/home/pi/Downloads/hnd/camalion.mp4")
video2 = Path("/home/pi/Downloads/AnimatedSF.mp4")
global a
os.environ['DISPLAY']= ":0"
global screen_status
screen_status = ''
a = 'no video'
while True:
    screen()
    if((screen_status == '2') and (a != 'omx1')):
            global player            
            if(a == 'omx2'):
                    play1()
            else:
                    player = OMXPlayer(video)
            a = 'omx1'  #subprocess.call('xset dpms force off',shell=True)
    elif((screen_status == '1') and (a != 'omx2')):
            global omx2
            if( a == 'omx1'):
                    play2()
            else:                    
                    omx2 = OMXPlayer(video2)
            a = 'omx2'
##        player.pause()
##        player.hide_video()
##        omx2 = OMXPlayer(video2)
##        time.sleep(2.5)
##        player.quit()
##        time.sleep(8)
##        omx2.pause()
##        a = 'omx2'
##        subprocess.call('xset dpms force on',shell=True)
    elif(screen_status == '3'):
        os.system('sudo killall omxplayer.bin')
        a = 'no video'
    else:
        pass
        
