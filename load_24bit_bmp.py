from ST7735 import TFT,TFTColor,init_tft
from machine import freq

freq(250000000)
(spi,tft)=init_tft()
tft.show_24bit_bmp('kduinologo16.bmp')
spi.deinit()
freq(125000000)
