#A basic RSS display using Pimoroni's GFX Hat.
print("If you get an error involving isAlive, run the lifeline.py program in an elevated terminal or manually replace every instance of isAlive with is_alive in cap1xxx.py")

import time, textwrap, webbrowser
from PIL import Image, ImageFont, ImageDraw
from gfxhat import lcd, backlight, fonts, touch
import feedparser
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
#I would really love to just fix the code, but I don't know how.

def browser(ch, event):
    if event == 'press':
        webbrowser.get('firefox').open_new_tab(link)
        print("Opening browser")
touch.on(4, browser)
#Opens the webpage to match the title.

def backlight_on(ch, event):
    if event == 'press':
        backlight.set_pixel(0, 0, 0, 255)
        backlight.set_pixel(5, 255, 0, 0)
        backlight.set_pixel(3, 100, 100, 100)
        backlight.show()
        print("Backlight on")
touch.on(5, backlight_on)
#Plus Button. Enables a pik+blue backlight.

def backlight_off(ch, event):
    if event == 'press':
        backlight.set_pixel(0, 0, 0, 0)
        backlight.set_pixel(5, 0, 0, 0)
        backlight.set_pixel(3, 0, 0, 0)
        backlight.show()
        print("Backlight off")
touch.on(3, backlight_off)
#Minus button. Disables backlight.

#Allows the custom assignment of RSS feeds. Delete if you only intend on showing one.
def feed_1(ch, event):
    if event == 'press':
        url = "https://magpi.raspberrypi.com/feed"
        print("MagPi")
touch.on(0, feed_1)

def feed_2(ch, event):
    if event == 'press':
        url = "https://magpi.raspberrypi.com/feed"
        print("MagPi")
touch.on(1, feed_2)
def feed_3(ch, event):
    if event == 'press':
        url = "https://magpi.raspberrypi.com/feed"
        print("MagPi")
touch.on(2, feed_3)
#End of link-switching code

#These variables are a good starting point for customization.
#Any TTF in the same folder as this project (likely downloads) will work.
font = ImageFont.truetype("Orbitron-Regular.ttf", 10)
wrapper = textwrap.TextWrapper(width=16)
url = "https://magpi.raspberrypi.com/feed"

feed = feedparser.parse(url)
width, height = lcd.dimensions()
image = Image.new('P', (width, height))    
draw = ImageDraw.Draw(image)


while True:
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
        #Adjust to taste.
        
        feed = feedparser.parse(url)
        #Live updating
