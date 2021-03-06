import sys, os
sys.path.insert(0, '../')
# sys.path.append(os.path.join(os.path.dirname(__file__), '../', 'lib'))
import lib.textCropper as tc
import numpy as np
from matplotlib import pyplot as plt
import cv2
import math, random
from lib.profiler import *
import itertools
import Image
import pytesseract


def find_text(img):
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
  cl1 = clahe.apply(gray)
  cv2.imwrite('placeholder.jpg', cl1)
  cv2_im = cv2.imread('placeholder.jpg',0)
  pil_im = Image.fromarray(cv2_im)
  return pytesseract.image_to_string(pil_im, lang="eng")

def test_text_cropper():
  if len(sys.argv) > 1:
    image_name= sys.argv[1]
  else:
    image_name = "emergency_stop"
  img = cv2.imread('images/' + image_name + '.jpg')
  croppedRegions = tc.TextCropper.cropTextRegionsFromImage(img, 20)
  for i in range(len(croppedRegions)):
    plt.subplot(len(croppedRegions), 1, i+1)
    if croppedRegions[i].size != 0:
      b,g,r = cv2.split(croppedRegions[i])
      rgbImg = cv2.merge([r,g,b])
      # cv2.imwrite('fallout_'+str(i)+'.jpg', croppedRegions[i])
      print find_text(rgbImg)
      plt.imshow(rgbImg)
  plt.show()

if __name__ == "__main__":
  test_text_cropper()