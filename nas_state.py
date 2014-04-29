import RPi.GPIO as GPIO
import time
import urllib2
import os
import threading

# Configuration GPIO
#
# J'utilise le mode BCM plutot que BOARD que je trouve moins pratique dans mon ca.
GPIO.setmode(GPIO.BCM)

# PIN GPIO ou sont place les LED
GREEN = 18
YELLOW = 23

# PIN GPIO des bouton reboot et Stop
SWITCH_REBOOT = 17
SWITCH_STOP = 22
#

run = True  # Initialisation du mode "run"

# Class DEL
# Cette classe sert a definir le PIN et le statut de la LED (eteinte ou allumee)
class DEL:
    def __init__(self, led_pin):
        self.pin = led_pin
        self.state = False
        GPIO.setup(led_pin, GPIO.OUT)
    
    def set_state(self, led_state):
        self.state = led_state
        GPIO.output(self.pin, led_state)
            
    def get_state(self):
        return self.state

# Test de la connexion internet
def test_connection():
    global test_connect
    
    try:
        response = urllib2.urlopen('http://74.125.228.100',timeout=1)
    except urllib2.URLError as err:
        yellow.set_state(False)
        print "Erreur"

    # On repart le Thread dans 60s
    test_connect = threading.Timer(60, test_connection)
    test_connect.start()
        
	    
# Fonction de reboot
def reboot(channel):
    # On ferme correctement le system en liberant les ports GPIO
    GPIO.cleanup()
    # Puis on reboot correctement
    os.system('shutdown -r now')
        
# Setup du bouton Reboot
GPIO.setup(SWITCH_REBOOT, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.add_event_detect(SWITCH_REBOOT, GPIO.FALLING, callback=reboot)
			
# On initialise les LED
green = DEL(GREEN)
green.set_state(True)
yellow = DEL(YELLOW)
yellow.set_state(True)

test_connect = threading.Timer(1, test_connection)
test_connect.start()

# Application principale
# Pour le moment, elle ne fait rien...
while run:
    pass

GPIO.cleanup()
print "end"
