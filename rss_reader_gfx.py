#A basic RSS display using Pimoroni's GFX Hat.
print("If you get an error involving isAlive, run the lifeline.py program in an elevated terminal or manually replace every instance of isAlive with is_alive in cap1xxx.py")

import time, textwrap, webbrowser, feedparser, warnings, sys, os
from PIL import Image, ImageFont, ImageDraw
from gfxhat import lcd, backlight, fonts, touch
warnings.filterwarnings("ignore", category=DeprecationWarning)
#I would really love to just fix the code, but I don't know how.
        
for i in range(6):
    touch.set_led(i, 1)
    time.sleep(0.05)
for i in range(6):
    touch.set_led(i, 0)
    time.sleep(0.05)

#The screen was randomly blanking or bugging out. The easiest solution was a program restart.
def fix_blank(ch, event):
    if event == 'press':
        print("argv was",sys.argv)
        print("sys.executable was", sys.executable)
        print("restart now")
        os.execv(sys.executable, ['python'] + sys.argv)
touch.on(0, fix_blank)

def browser(ch, event):
    if event == 'press':
        webbrowser.get('firefox').open_new_tab(link)
        print("Opening browser to", link)
        touch.set_led(4, 1)
        time.sleep(0.25)
        touch.set_led(4, 0)
touch.on(4, browser)
#Opens the webpage to match the title.

def backlight_on(ch, event):
    if event == 'press':
        #If you want to customize the colors, the format is (pixel, r, g, b)
        backlight.set_pixel(0, 255, 0, 125)
        backlight.set_pixel(5, 255, 0, 0)
        backlight.set_pixel(3, 255, 100, 100)
        backlight.show()
        print("Backlight on")
        touch.set_led(5, 1)
        time.sleep(0.25)
        touch.set_led(5, 0)
touch.on(5, backlight_on)
#Plus Button. Enables backlight.

def backlight_off(ch, event):
    if event == 'press':
        backlight.set_pixel(0, 0, 0, 0)
        backlight.set_pixel(5, 0, 0, 0)
        backlight.set_pixel(3, 0, 0, 0)
        backlight.show()
        print("Backlight off")
        touch.set_led(3, 1)
        time.sleep(0.25)
        touch.set_led(3, 0)
touch.on(3, backlight_off)
#Minus button. Disables backlight.

#These variables are a good starting point for customization.
#Any TTF in the same folder as this project (likely downloads) will work.
font = ImageFont.truetype("Orbitron-Regular.ttf", 10)
wrapper = textwrap.TextWrapper(width=16)
url = "https://magpi.raspberrypi.com/feed"


width, height = lcd.dimensions()
image = Image.new('P', (width, height))    
draw = ImageDraw.Draw(image)

while True:
    feed = feedparser.parse(url)
    for entry in feed.entries:
        text = entry.title
        link = entry.link
        text_str = wrapper.fill(text)
        
        draw.rectangle([(0,0), (width, height)], 0)
        w, h = font.getsize(text_str)
        x = 2
        y = 2

        draw.text((x, y), text_str, 1, font)

        for x in range(width):
            for y in range(height):
                pixel = image.getpixel((x, y))
                lcd.set_pixel(x, y, pixel)
        #This loads the image.
                
        lcd.show()
        #Refresh the display.
        
        time.sleep(10)
        #Adjust to taste

