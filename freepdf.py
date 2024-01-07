from PIL import ImageGrab
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
import time
import pyautogui
from screeninfo import get_monitors
import pygetwindow as gw


# Get monitor information
monitors = get_monitors()

# Select the desired monitor (e.g., the first monitor)
monitor = monitors[0]
x1, y1, x2, y2 = monitor.x, monitor.y, monitor.width, monitor.height


def get_mouse_x_y():
    time.sleep(3)
    x, y = pyautogui.position()

    # Print the coordinates
    print(f"Mouse X: {x}, Mouse Y: {y}")
    
#Mouse X: 2869, Mouse Y: 276
#Mouse X: 4125, Mouse Y: 1125
# 59 pages (double)
# clickcoords: Mouse X: 4141, Mouse Y: 706
# backwards clickcoords: Mouse X: 2892, Mouse Y: 698
    
    
def get_monitor_mouse_pos():
    time.sleep(3)
    # Get the active window
    active_window = gw.getActiveWindow()

    # Get the mouse cursor position on the screen
    mouse_x, mouse_y = pyautogui.position()

    # Get the monitor where the mouse cursor is located
    monitor = gw.getWindowsWithTitle(active_window.title)

    if monitor:
        monitor = monitor[0]  # If the active window was found
    else:
        monitor = gw.getWindowsAt(mouse_x, mouse_y)[0]  # If the active window wasn't found, get the window under the mouse cursor

    # Get the monitor-related coordinates of the mouse cursor
    mouse_x_monitor = mouse_x - monitor.left
    mouse_y_monitor = mouse_y - monitor.top

    print(f"Mouse X: {mouse_x_monitor}, Mouse Y: {mouse_y_monitor} on {monitor.title}")
#top left: Mouse X: 313, Mouse Y: 148
#down right: Mouse X: 1591, Mouse Y: 1018
# click 1: Mouse X: 1620, Mouse Y: 576
# click 2: Mouse X: 342, Mouse Y: 578




def capture_screenshots_and_create_pdf():
    x1, y1, x2, y2 = 632, 143, 1904, 1187  # Define your own coordinates

    # Define the file names and PDF file name
    image_files = ["a0.png"]
    for i in range(1, 60):
        image_files.append(f"a{i}.png")

    pdf_file = "output.pdf"

    # Take screenshots, save them, and click at specified coordinates
    for i, file_name in enumerate(image_files):
        time.sleep(0.5)
        screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        screenshot.save(file_name)

        # Simulate the mouse click at the specified coordinates
        print(f"Progress: {i}/{60}")
        # You can insert code here to perform a mouse click using a library like PyAutoGUI if needed.
        pyautogui.click((1937,754))
        # Wait for 1 second (adjust as needed)

    # Create a PDF from the screenshots
    c = canvas.Canvas(pdf_file, pagesize=letter)

    for image_file in image_files:
        c.drawImage(image_file, 0, 0, width=letter[0], height=letter[1])
        c.showPage()

    c.save()

    # Delete the screenshots
    for file_name in image_files:
        os.remove(file_name)

    print(f"PDF created: {pdf_file}")
    
    for i in range(0,60):
        pyautogui.click((625,710))
        time.sleep(0.02)
        

capture_screenshots_and_create_pdf()
# get_monitor_mouse_pos()
# get_mouse_x_y()
