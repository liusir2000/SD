# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 10:46:47 2024

@author: Administrator
"""

from transformers import ViltProcessor, ViltForQuestionAnswering
model = ViltForQuestionAnswering.from_pretrained ("dandelin/vilt-b32-finetuned-vqa")
from PIL import Image
import torch
processor = ViltProcessor.from_pretrained ("dandelin/vilt-b32-finetuned-vqa")
import os



def writelog(linestr):
    if os.path.exists(resultfile):
        with open(resultfile,'a') as f:
            f.write(linestr+'\n')
    else:
        with open(resultfile,'w') as f:
            f.write(linestr+'\n')  

    
def getWeather(filename,text):
    try:
        image = Image.open(filename).convert('RGB')        
        # prepare inputs
        inputs = processor(image, text, return_tensors="pt")  
        # forward pass
        with torch.no_grad():
            outputs = model(**inputs)        
        logits = outputs.logits
        idx = logits.argmax(-1).item()
        return model.config.id2label[idx]
    except:
        return 'error'


yourImagesDir = r'.\xjhImages'
yourOutputfile = 'xjh_Is_it_sunny_result.csv'

params = [[yourImagesDir,yourOutputfile]]
for param in params:
    sourcedir = param[0]
    resultfile = param[1]
    for root, dirs, files in os.walk(sourcedir, topdown=False):
        for name in files:
            afilename = os.path.join(root, name)
            #tq = getWeather(afilename,'What weather is this?')  #M1
            tq = getWeather(afilename,'Is this sunny?')          #M2
            #tq = getWeather(afilename,'Is there sunshine on the ground?')    #M3           
            #tq = getWeather(afilename,"Is there sunshine?")      #M4
            linestr = name+','+name.split('.')[0].lower()+','+ tq
            writelog(linestr)        
            print(linestr)            

    
