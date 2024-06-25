import time
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller

keyboard = Controller()

def send_whatsapp_message(msg: str, phone_numbers: list):
    try:
        for phone_no in phone_numbers:
            pywhatkit.sendwhatmsg_instantly(
                phone_no=phone_no,
                message=msg,
                tab_close=True,
                close_time=3  # Additional parameter to close the tab after 3 seconds
            )
            time.sleep(10)  # Wait for the message to be prepared
            pyautogui.click()  # Click to activate the message window
            time.sleep(2)  # Short delay to ensure the click is registered
            keyboard.press(Key.enter)  # Press Enter to send the message
            keyboard.release(Key.enter)
            print(f"Message sent to {phone_no}")
    except Exception as e:
        print(f"Failed to send message to {phone_no}: {e}")

if __name__ == "__main__":
    friend_numbers = ["whatsapp_number1", "whatsapp_number2", "whatsapp_number3"]
    message = "Hello, this is a test message!"
    send_whatsapp_message(msg=message, phone_numbers=friend_numbers)
