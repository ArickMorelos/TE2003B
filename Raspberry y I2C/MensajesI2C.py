from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import time as t
import serial

i2c = busio.I2C(SCL, SDA)
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
disp.fill(0)
disp.show()

def names():
    image = Image.new('1', (128, 64))
    width = disp.width
    height = disp.height
    image = Image.new('1', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    draw.rectangle((100,100,width,height), outline=100, fill=255)

    draw.text((15, 16), 'Fernando Estrada', font=font, fill=255)
    draw.text((15, 26), 'Arick Morelos', font=font, fill=255)
    draw.text((15, 36), 'Guillermo Ramos', font=font, fill=255)
    
    # Muestra Texto
    disp.image(image)
    disp.show()
    t.sleep(2)
    
    
def entrada():

    image1 = Image.new('1', (128, 64))
    width = disp.width
    height = disp.height
    image1 = Image.new('1', (width, height))
    #draw.rectangle((0,0,width,height), outline=0, fill=0)
    draw = ImageDraw.Draw(image1)
    font = ImageFont.load_default()
    #raw.text((30, 16), 'Oskar Villa', font=font, fill=255)
    draw.line((5,15, 100, 15), fill=255)
    draw.line((5,50, 100, 50), fill=255)
    
    draw.text((15, 16), 'Inserte su mensaje', font=font, fill=255)
    message = input("Inserte su mensaje : ")
    
    if (len(message) >= 50):
        draw.text((15, 16), 'Mensaje mayor a 50 caracteres', font=font, fill=255)
        t.sleep(3)
    else:
        draw.text((15, 26), message, font=font, fill=255)
    
    # Muestra Texto
    disp.image(image1)
    disp.show()
    t.sleep(3)


def uart():
    image2 = Image.new('1', (128, 64))
    width = disp.width
    height = disp.height
    #image = Image.new('1', (width, height))
    draw2 = ImageDraw.Draw(image2)
    font = ImageFont.load_default()
    #$draw2.rectangle((100,100,width,height), outline=100, fill=255)

    s= serial.Serial("/dev/ttyACM0",9600)
    print(s.name)
    for i in range (7):
        x = s.readline()
        print (x)
    s.close()
    
    # Muestra Texto
    disp.image(image2)
    disp.show()
    t.sleep(2)
    
names()
entrada()
uart()
