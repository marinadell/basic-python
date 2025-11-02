import time
#time library for loading simulation

def rerun():
    print("again? type y for yes or n for no")
#prompt to run program again
    again = input()
    #input to run program or exit
    if again == "y":
	    #condition in which to re/run program
	    converter()
      #re/run program
    else: 
	    #condition in which to exit program
	    print("program ended")
	     #program end
def converter():
	#make it  we can re-use the program 
    print("Fahrenheit to Celsius converter")
    #what the program does
    time.sleep(1)
    print("please wait...")
    #loading effect
    time.sleep(1.7)
    print("Enter temperature in Fahrenheit")
    #prompt for input to convert
    Fahrenheit = input()
    #input to convert
    Fahrenheit_float = float(Fahrenheit)
    #make it readable to the interpreter
    print("calculating...")
    #another loading effect
    time.sleep(3)
    Celsius = ((Fahrenheit_float - 32) * 5/9)
    #converting input value to oitput
    print (Fahrenheit, "Fahrenheit is", Celsius, "Celsius")
    #output conversion
    time.sleep(1.5)
    #yet another loading effect
    rerun()
converter()
#start program

	
rerun()