# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 16:06:29 2020

@author: LetinAR
"""
import cv2
import os
import moviepy.editor as mv
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
   
ffmpeg_extract_subclip("lefteye_video.avi", 0, 10, targetname="lefteye_cutted.avi")
ffmpeg_extract_subclip("righteye_video.avi", 0, 10, targetname="righteye_cutted.avi")

clip = mv.VideoFileClip("lefteye_cutted.avi")
clip.write_videofile("lefteye_cutted.mp4")

clip = mv.VideoFileClip("righteye_cutted.avi")
clip.write_videofile("righteye_cutted.mp4")

