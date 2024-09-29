from machine import Pin, I2C
import ssd1306
import time

# Initialize I2C on Raspberry Pi Pico (SDA=GP0, SCL=GP1)
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)

# Define OLED display width and height
oled_width = 128
oled_height = 64

# Create an SSD1306 OLED object
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Function to display text on the OLED
def display_text():
    oled.fill(0)  # Clear the display
    oled.text("Hello, World!", 0, 0)  # Add text at x=0, y=0
    oled.text("SSD1306 OLED", 0, 16)  # Add text at x=0, y=16
    oled.text("MicroPython", 0, 32)   # Add text at x=0, y=32
    oled.show()  # Refresh the screen to display the text

# Main loop
while True:
    display_text()
    time.sleep(2)  # Delay for 2 seconds