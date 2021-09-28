import keyboard
from datetime import datetime
s_now=''
caps_now=''
quote_now=''
delay=130000


def s_press(key):
    global s_now
    keyboard.send('left shift', do_press=True, do_release=False)
    if not s_now:
        s_now=datetime.now()
def s_release(key):
    global s_now
    keyboard.send('left shift', do_press=False, do_release=True)
    time_passed=(datetime.now()-s_now).microseconds
    s_now=''
    if time_passed<delay:
        keyboard.send('s')

def double_qoute_press(key):
    global quote_now
    keyboard.send('right shift', do_press=True, do_release=False)
    if not quote_now:
        quote_now=datetime.now()
def double_qoute_release(key):
    global quote_now
    keyboard.send('right shift', do_press=False, do_release=True)
    time_passed=(datetime.now()-quote_now).microseconds
    quote_now=''
    if time_passed<delay:
        keyboard.send(';')

def caps_press(key):
    global caps_now
    keyboard.send('left ctrl', do_press=True, do_release=False)
    if not caps_now:
        caps_now=datetime.now()
def caps_release(key):
    global caps_now
    keyboard.send('left ctrl', do_press=False, do_release=True)
    time_passed=(datetime.now()-caps_now).microseconds
    caps_now=''
    if time_passed<delay:
        keyboard.send('escape')

# keyboard.add_hotkey('shift+s',lambda:keyboard.send('S'))
# keyboard.add_hotkey(';+s',lambda:keyboard.send('S'))
# keyboard.on_press_key("s", s_press,suppress=True)
# keyboard.on_release_key("s", s_release)
keyboard.on_press_key(";", double_qoute_press,suppress=True)
keyboard.on_release_key(";", double_qoute_release)
keyboard.on_press_key("caps lock", caps_press,suppress=True)
keyboard.on_release_key("caps lock", caps_release)
keyboard.remap_hotkey('left alt+z','0')
keyboard.remap_hotkey('left alt+x','1')
keyboard.remap_hotkey('left alt+c','2')
keyboard.remap_hotkey('left alt+s','4')
keyboard.remap_hotkey('left alt+v','3')
keyboard.remap_hotkey('left alt+d','5')
keyboard.remap_hotkey('left alt+f','6')
keyboard.remap_hotkey('left alt+w','7')
keyboard.remap_hotkey('left alt+e','8')
keyboard.remap_hotkey('left alt+r','9')
keyboard.remap_hotkey('left alt+a','\\')
keyboard.remap_hotkey('left alt+g','shift+\\')
keyboard.remap_hotkey('left alt+q','`')
keyboard.remap_hotkey('left alt+t','shift+`')

keyboard.remap_hotkey('left alt+b','=')
keyboard.remap_hotkey('left alt+n','+')
keyboard.remap_hotkey('left alt+m','shift+1')
# keyboard.remap_hotkey('left alt+,','@')
keyboard.remap_hotkey('left alt+/','shift+2') #/ is detected as ,
keyboard.remap_hotkey('left alt+.','shift+3')
keyboard.remap_hotkey('left alt+h','shift+_')
keyboard.remap_hotkey('left alt+j','shift+4')
keyboard.remap_hotkey('left alt+k','shift+5')
keyboard.remap_hotkey('left alt+l','shift+6')
keyboard.remap_hotkey('left alt+\'','-')
keyboard.remap_hotkey('left alt+u','shift+7')
keyboard.remap_hotkey('left alt+i','*')
keyboard.remap_hotkey('left alt+o','shift+9')
keyboard.remap_hotkey('left alt+p','shift+0')
keyboard.remap_hotkey('left alt+[','backspace')
keyboard.remap_hotkey('left alt+]','delete')
keyboard.remap_hotkey('left alt+space','enter')

keyboard.wait()
