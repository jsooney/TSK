##############################
#Done by Jaimes
#Date: 14 Aug 2021
#Time: 1500H
#version: 0.0.0
# to extract entry info (in future can use the info for further automation)

##############################

import webbrowser, pyperclip, requests, bs4, re, logging, json, os, subprocess, signal
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
TK_SILENCE_DEPRECATION=1

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def __init__():

    return
    
def getFromClipboard():
    return pyperclip.paste()

def temp():

    return

def runcommand (cmd):
    logging.debug('Start of runcommand') 
    proc = subprocess.Popen(cmd,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            shell=True,
                            universal_newlines=True)
    std_out, std_err = proc.communicate()
    logging.debug('End of runcommand') 
    return proc.returncode, std_out, std_err

def paste_execute():
    tensorflow_filename = getFromClipboard()
    entryField.set(tensorflow_filename)
    execute()
    return


def execute():
    logging.debug('Start of execute') 
    
    print("zgrep -r " + entryField.get() + " " + str_tenosorflow_whl.get())
    try:
        code, out, err = runcommand("zgrep -r " + entryField.get() + " tensorflow-2.6.0-cp36-cp36m-manylinux2010_x86_64.whl")
        code, out, err = runcommand("zgrep -r " + entryField.get() + " " + str_tenosorflow_whl.get())
        #output = subprocess.check_output('grep string tsvfile', shell=True, preexec_fn=lambda: signal.signal(signal.SIGPIPE, signal.SIG_DFL))
        #exit err code 1 = not found
    except:
        temp=1
    
    if (code == 1):
        print("Not found in tensorflow")
        tensorflowflag = "Not found in tensorflow"
    else:
        print("Found in tensorflow")
        tensorflowflag = "Found in tensorflow"


    print("zgrep -r " + entryField.get() + " " + str_tenosorflow_cpu_whl.get())
    try:
        code, out, err = runcommand("zgrep -r " + entryField.get() + " " + str_tenosorflow_cpu_whl.get())
        #output = subprocess.check_output('grep string tsvfile', shell=True, preexec_fn=lambda: signal.signal(signal.SIGPIPE, signal.SIG_DFL))
        #exit err code 1 = not found
    except:
        temp=1
    
    if (code == 1):
        print("Not found in tensorflow_cpu")
        tensorflowCPUFlag= "Not found in tensorflow_cpu"
    else:
        print("Found in tensorflow_cpu")
        tensorflowCPUFlag= "Found in tensorflow_cpu"
    #print(subprocess.check_output(['zgrep -r compression_utils.h tensorflow-2.6.0-cp36-cp36m-manylinux2010_x86_64.whl']))

    print("zgrep -r " + entryField.get() + " " + str_tenosorflow_gpu_whl.get())
    try:
        code, out, err = runcommand("zgrep -r " + entryField.get() + " " + str_tenosorflow_gpu_whl.get())
        #output = subprocess.check_output('grep string tsvfile', shell=True, preexec_fn=lambda: signal.signal(signal.SIGPIPE, signal.SIG_DFL))
        #exit err code 1 = not found
    except:
        temp=1
    
    if (code == 1):
        print("Not found in tensorflow_gpu")
        tensorflowGPUFlag = "Not found in tensorflow_gpu"
    else:
        print("Found in tensorflow_gpu")
        tensorflowGPUFlag = "Found in tensorflow_gpu"


    messagebox.showinfo("Information", entryField.get() + " is " + tensorflowflag + ", " + tensorflowCPUFlag + " and is " + tensorflowGPUFlag)



    return
#===========================================================================================================================
#--------------------------------------------- start of tkinter ------------------------------------------------------------
#===========================================================================================================================
#initialized tkinter
root = Tk() 
#title
root.title("Tsk - Tensorflow Search Key")

mainframe = ttk.Frame(root, padding="3 3 12 12") 
mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) 
# not sure, but this is the spill over if there is space on another grid in column
mainframe.columnconfigure(0, weight=1) 
mainframe.rowconfigure(0, weight=1)

#============================================================== row 1

rowCount = 1

ttk.Label(mainframe, text=(str(rowCount) + ". Enter Vuln File (without .cc/.h):")).grid(column=1, row=rowCount, sticky=(W, E))

#text field: 
entryField = StringVar()      
entry_entry = ttk.Entry(mainframe, width=18, textvariable=entryField) 
entry_entry.grid(column=2, row=rowCount, sticky=(W, E))

entry_entry_button_label=StringVar()
ttk.Button(mainframe, textvariable=entry_entry_button_label,command=execute).grid(row=rowCount, column=3, sticky=(W,E))
entry_entry_button_label.set("Execute")

#==============================================================
rowCount += 1

ttk.Label(mainframe, text=(str(rowCount) + ". Download the latest tensorflow, tensorflow_cpu and tensorflow_gpu whl files in the same folder and enter the names below:")).grid(column=1, row=rowCount, sticky=(W, E), columnspan=3)

#==============================================================
rowCount += 1

ttk.Label(mainframe, text=(str(rowCount) + ". Latest Tensorflow whl file:")).grid(column=1, row=rowCount, sticky=(W, E))

#text field: 
str_tenosorflow_whl = StringVar()      
entry_tenosorflow_whl = ttk.Entry(mainframe, width=18, textvariable=str_tenosorflow_whl) 
entry_tenosorflow_whl.grid(column=2, row=rowCount, sticky=(W, E))

#==============================================================
rowCount += 1

ttk.Label(mainframe, text=(str(rowCount) + ". Latest Tensorflow_cpu whl file:")).grid(column=1, row=rowCount, sticky=(W, E))

#text field: 
str_tenosorflow_cpu_whl = StringVar()      
entry_tenosorflow_cpu_whl = ttk.Entry(mainframe, width=18, textvariable=str_tenosorflow_cpu_whl) 
entry_tenosorflow_cpu_whl.grid(column=2, row=rowCount, sticky=(W, E))
#==============================================================
rowCount += 1

ttk.Label(mainframe, text=(str(rowCount) + ". Latest Tensorflow_gpu whl file:")).grid(column=1, row=rowCount, sticky=(W, E))

#text field: 
str_tenosorflow_gpu_whl = StringVar()      
entry_tenosorflow_gpu_whl = ttk.Entry(mainframe, width=18, textvariable=str_tenosorflow_gpu_whl) 
entry_tenosorflow_gpu_whl.grid(column=2, row=rowCount, sticky=(W, E))

#========================== Render Tkinter ===================================================================================
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
root.mainloop()