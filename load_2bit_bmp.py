from ST7735 import TFT, TFTColor,init_tft
from machine import freq,Pin,SPI
from utime import sleep_ms,time

start_time = time()

freq(280000000) #Overclock CPU frequency

(spi,tft)=init_tft()

bmp_file = "/bad_apple_1377.bmp"

tft.show_2bit_bmp(bmp_file)

spi.deinit()
freq(125000000) #Overclock CPU frequency

total_time = time()-start_time
print(total_time)