# drink water notification project:-
import time
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please Drink Water!!",
            message = "It lubricates the joints · 2. It forms saliva and mucus · It delivers oxygen throughout the body · ",
            app_icon = "M:\projects\glass-of-water.ico", 
            
            timeout = 5

        )
        time.sleep(60*60)
        
