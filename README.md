# SD
Code and sample data related to reversing sunshine duration (SD) and solar radiation (SR) with video images.
(1) weatherFromImages.py is used to retrieve weather type (or weather it is sunny etc.) from video images (screenshot images of a 10-minute interval), the source images directory should be set, output is a csv file recording weather type (content: image filename, timestamp, weather type).  
(2) weather2SD.py is used to retrieve hourly and daily SD from the weather type csv file, output is a hourly SD csv file and a daily SD csv.
(3) SD2SR.py is used to retrieve the daily SR from the daily SD csv.
(4) images.zip is the sample data of video images


Need packages: aquacropeto, transformers, PIL, Torch 
