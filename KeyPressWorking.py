#2020-12-26 Turn off lights from Sofa Baton Remote
#Listen to key press. Turn off lights on key press.
#-----11 - Tom's desk
#-----10 - Living Room Light
#-----13 & 14 - Smart Plugs (X-Mas Lights)
from pynput.keyboard import Key, Listener
import requests
import json


def on_press(key):
    print('pressed')
    print(key)
    if str(key) == '<269025125>':
        print("Toggle Lights On")
        toggleAllLights()
def on_release(key):
    print('released')
    
def toggleAllLights():


    #lightNum - use living room light as key for on off
    lightNum = str(10)
    print('executing toggleOneLight function for light number ' + lightNum)

    # Construct URL specific to bulb
    urlBase = 'http://192.168.1.133/api/O5uWLcD2mrNhfmQdUy9Hn78MmTGo4OHgXtWjCqes/lights'
    urlGet = urlBase + '/' + lightNum
    urlPut10 = urlBase + '/' + str(10) + '/state'
    urlPut13 = urlBase + '/' + str(13) + '/state'
    urlPut14 = urlBase + '/' + str(14) + '/state'

    # Get state of bulb and flip value in JSON
    bulbState = requests.get(urlGet) #get state from Hue Bridge
    bulbState = json.loads(bulbState.text) #convert str to python dictionary
    if bulbState['state']['on']: #flip set payload
        payload = {'on':False}
    else:
        payload = {'on':True}
        
    # Update blub with new state
    r = requests.put(urlPut10, json=payload)
    r = requests.put(urlPut13, json=payload)
    r = requests.put(urlPut14, json=payload)

    # Response for troubleshooting
    print(' ')
    print(r.url)
    print(r.text)
    print(r.status_code)

print('hello')

with Listener(
    on_press=on_press,
    on_release=on_release) as listener:
    listener.join()