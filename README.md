# SD
Codes and sample data related to retrieve sunshine duration (SD) and solar radiation (SR) with video images.

(1) weatherFromImages.py is used to retrieve weather type (or whether it is sunny etc.) from video images (screenshot images of a 10-minute interval), the source images directory should be set, output is a csv file recording weather type (content: image filename, timestamp, weather type).<br>
(2) weather2SD.py is used to retrieve hourly and daily SD from the weather type csv file, output is a hourly SD csv file and a daily SD csv.<br>
(3) SD2SR.py is used to retrieve the daily SR from the daily SD csv.<br>
(4) cmImages and xjhImages is the sample data of video images.The complete sample data is available at https://pan.baidu.com/s/1mNUltBQLha3kMiKjJkcFng?pwd=e3iq.



Need packages: transformers, PIL, Torch, aquacropeto
