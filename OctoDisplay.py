import I2C_LCD_driver
from time import *
import subprocess
import string

ip_address = subprocess.check_output(['hostname','-I'])
ip_address = ip_address.decode('utf-8')
ip_address = ip_address[:len(ip_address)-1]

hostname = subprocess.check_output(['whoami'])
hostname = hostname.decode('utf-8')
hostname = hostname[:len(hostname)-1]

mylcd = I2C_LCD_driver.lcd()
mylcd.lcd_display_string(hostname, 1)
mylcd.lcd_display_string(ip_address, 2)
