# Step 1: Import the necessary library
from plyer import notification
import time

# Step 2: Define the notification function
def send_notification():
    notification.notify(
        title="Break Reminder!",
        message="It's time to take a break and stretch!",
        timeout=10  # Notification will disappear after 10 seconds
    )

# Step 3: Run the script in an infinite loop
while True:
    send_notification()  # Step 4: Send the notification
    time.sleep(3600)    # Step 5: Wait for 1 hour (3600 seconds)
