#!/usr/bin/python

from pyfirmata import Arduino, util
import OSC, atexit

def exit_handler():
	pin13.write(0) # Turn OFF the built-in LED
    print("Exiting ...")

def handler(addr, tags, data, client_address):
    txt = "OSCMessage '%s' from %s: " % (addr, client_address)
    txt += str(data)
    print(txt)
    pin9.write(180*data[0])
    
if __name__ == "__main__":
    print("Initializing board ...")
    try:
        board = Arduino('/dev/ttyATH0')
    except Exception as inst:
        print(type(inst))
        print(inst.args)
        print(inst)
        
    pin9 = board.get_pin('d:9:s')
    pin13 = board.get_pin('d:13:o')
	
	atexit.register(exit_handler)
	
	print("Initializing server ...")
    s = OSC.OSCServer(('192.168.1.118', 57120))  # port 57120
    s.addMsgHandler('/test', handler)     # call handler() for OSC messages received with the /startup address
    s.serve_forever()
	pin13.write(1) # Turn ON the built-in LED
	print("Serving ...")