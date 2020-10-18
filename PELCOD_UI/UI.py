
# coding: utf-8

# In[119]:


from tkinter import *
import serial

BUTTON_SIZE_X = 10
BUTTON_SIZE_Y = 10

root = Tk()
root.geometry("400x300")

string = ''

"""ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600)
"""
#ser.write(serial.to_bytes(cw))

#HEX Commands
#################################################################
Loaded_list   = [0xFF,0xFF,0x00,0xFF,0xBB,0xCC,0x85]
Unloaded_list = [0xFF,0xFF,0x00,0xFF,0xCC,0xBB,0x85]

Sample_list   = [0xFF,0x00,0x00,0x00,0x00,0x00,0x00]
Sample_list2  = [0xFF,0x00,0x00,0x00,0x00,0x00,0xFF]

stop_list     = [0xFF,0x00,0x00,0x00,0x00,0x00,0x00]
tilt_down     = [0xFF,0x00,0x00,0x10,0x00,0x00,0x00] #FF 00 00 10 00 00 10
tilt_up       = [0xFF,0x00,0x00,0x10,0x00,0x00,0x00] #FF 00 00 08 00 00 08
pan_left      = [0xFF,0x00,0x00,0x04,0x00,0x00,0x00] #FF 00 00 04 04 00 08
pan_right     = [0xFF,0x00,0x00,0x02,0x00,0x00,0x00] #FF 00 00 02 04 00 06


#Variables
#################################################################
var_loaded = IntVar()
var_unloaded = IntVar()

#Functions
#################################################################
def readloaded_chkbox(var):
    x = var.get()
    print(x)
    if x == 1:
        print("loaded_chkbox CLicked!")
#        ser.write(serial.to_bytes(Loaded_list))
        
def readunloaded_chkbox(var):
    x = var.get()
    print(x)
    if x == 1:
        print("unloaded_chkbox CLicked!")     
#        ser.write(serial.to_bytes(Unloaded_list))
        
def readscale_pan():
    x = scalepan.get()
    print(x)
    
def Left_button():
    print("Left pressed!")
    x = scalepan.get()
    pan_left[4] = x
    Checksum(pan_left)
    print(pan_left)

def Right_button():
    print("Right pressed!")
    x = scalepan.get()
    pan_right[4] = x
    Checksum(pan_right)    
    print(pan_right)
    
def Up_button():
    print("Up button pressed!")
    x = scaletilt.get()
    tilt_up[5] = x
    Checksum(tilt_up)
    print(tilt_up)
#    ser.write(serial.to_bytes(tilt_up))

def Down_button():
    print("Down button pressed!")
    x = scaletilt.get()
    tilt_down[5] = x
    Checksum(tilt_down)
    print(tilt_down)
#    ser.write(serial.to_bytes(tilt_down))
    
def Stop_button():
    print("Stop!")
    print(stop_list)
#    ser.write(serial.to_bytes(stop_list))

def Checksum(list_var):
    checksum_var = list_var[1]+list_var[2]+list_var[3]+list_var[4]+list_var[5]
    checksum_var = checksum_var % 100
    list_var[6] = checksum_var

def readserial_entry():
    string =serial_entry.get()
    print(type(string))
    
#Button layout 
#################################################################

leftbutton = Button(root,text = "LEFT",padx=BUTTON_SIZE_X,pady=BUTTON_SIZE_Y,height=1,width=3,command=lambda:Left_button())
#leftbutton.grid(row=10,column=4)
leftbutton.grid(row=10,column=0)

rightbutton = Button(root,text = "RIGHT",padx=BUTTON_SIZE_X,pady=BUTTON_SIZE_Y,height=1,width=3,command=lambda:Right_button())
#rightbutton.grid(row=10,column=6)
rightbutton.grid(row=10,column=2)

upbutton = Button(root,text = "UP",padx=BUTTON_SIZE_X,pady=BUTTON_SIZE_Y,height=1,width=3,command=lambda:Up_button())
#upbutton.grid(row=9,column=5)
upbutton.grid(row=9,column=1)

downbutton = Button(root,text = "DOWN",padx=BUTTON_SIZE_X,pady=BUTTON_SIZE_Y,height=1,width=3,command=lambda:Down_button())
#downbutton.grid(row=11,column=5)
downbutton.grid(row=11,column=1)

stopbutton = Button(root,text = "STOP",padx=BUTTON_SIZE_X,pady=BUTTON_SIZE_Y,height=1,width=3,command=lambda:Stop_button())
stopbutton.grid(row=10,column=1)
#stopbutton.grid(row=10,column=5)

opendevice = Button(root,text="open",padx=BUTTON_SIZE_X,pady=BUTTON_SIZE_Y,height=1,width=3,command=lambda:readserial_entry())
#opendevice.grid(row=1,column=0)
opendevice.grid(row=1,column=0)

#Checkbox layout
###############################################################

Loadedcheckbox = Checkbutton(root, text="Loaded",command=lambda:readloaded_chkbox(var_loaded),variable = var_loaded)
Loadedcheckbox.grid(row=0,column=3)

Unloadedcheckbox = Checkbutton(root, text="Unloaded",command=lambda:readunloaded_chkbox(var_unloaded),variable = var_unloaded)
Unloadedcheckbox.grid(row=0,column=4)


#Slider layout
###############################################################

scalepan = Scale(root,from_=0,to=63,orient=HORIZONTAL)
scalepan.grid(row=9,column=4)#0

scaletilt = Scale(root,from_=0,to=63,orient=HORIZONTAL)
scaletilt.grid(row=11,column=4)#2

#Label layout
###############################################################
panlabel = Label(root,text="Pan Scale")
panlabel.grid(row=10,column=4)

Tiltlabel = Label(root,text="Tilt Scale")
Tiltlabel.grid(row=12,column=4)

seriallabel = Label(root,text="Port:")
seriallabel.grid(row=0,column=0)
                    
#Entry Layout
###############################################################
serial_entry = Entry(root,width=10)
serial_entry.grid(row=0,column=1,columnspan=2)

root.mainloop()

