import threading
interval = 0.5

def myPeriodicFunction():
    print("print")
def startTimer():
    threading.Timer(interval, startTimer).start()
    myPeriodicFunction()
startTimer()