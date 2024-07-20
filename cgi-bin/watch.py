import time
from datetime import datetime
import threading

def alarm_clock(alarm_time):
    while True:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            print("Alarm! Time to wake up!")
            break
        time.sleep(1)

def timer(duration):
    time.sleep(duration)
    print("Timer finished!")

if __name__ == "__main__":
    # Example usage:
    
    # Set an alarm
    alarm_time = input("Enter alarm time (HH:MM): ")
    threading.Thread(target=alarm_clock, args=(alarm_time,)).start()

    # Start a timer
    timer_duration = int(input("Enter timer duration in seconds: "))
    threading.Thread(target=timer, args=(timer_duration,)).start()
