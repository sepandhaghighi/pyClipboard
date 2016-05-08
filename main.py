import tkinter
import time
import datetime
import sys
f=tkinter.Tk()
temp=""
file=open("log.txt","a")
while(1):
    try:
        time.sleep(2)
        c=f.clipboard_get()
        if c!=temp:
            temp=c
            print("====="+str(datetime.datetime.today())+"=====",temp)
            file.write("====="+str(datetime.datetime.today())+"=====\n")
            file.write(temp+"\n")
    except tkinter.TclError:
        print("Large Input")
        file.close()
        f.destroy()
    except:
        print("End Of PyClipboard")
        file.close()
        f.destroy()
        sys.exit()
    

            
        
