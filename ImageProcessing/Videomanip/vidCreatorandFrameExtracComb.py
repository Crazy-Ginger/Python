import cv2
import argparse
import os
ap = argparse.ArgumentParser()
ap.add_argument("-ext","--extension", required=False,default='png',help="extention name. default is 'png'.")
ap.add_argument("-o","--output",required=False,default="output.mp4",help="output vidoe file")
args=vars(ap.parse_args())
