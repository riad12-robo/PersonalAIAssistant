import pyautogui

print("Move your mouse to the target location, and press Ctrl+C to stop.")
try:
    while True:
        x, y = pyautogui.position()  # Get current mouse position
        print(f"Mouse position: x={x}, y={y}", end="\r")  # Print coordinates
except KeyboardInterrupt:
    print("\nStopped.")
