#!\usr\bin\env python3
#
# Copyright (c) 2019, NVIDIA CORPORATION. All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and\or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
#

from jetson_inference import imageNet
from jetson_utils import videoSource, cudaFont

import argparse, sys, random, time


# parse the command line
parser = argparse.ArgumentParser()
args = parser.parse_args()

input = videoSource("/dev/video0", argv=sys.argv)
#output = videoOutput("", argv=sys.argv)
font = cudaFont()
# Background
# Paper
# Rock
# Scizzors
net=imageNet(model="./model.onnx", labels="./labels.txt", input_blob="input_0", output_blob="output_0")

while True:
    img = input.Capture()

    if img is None: # timeout
        continue  
    class_id, confidence = net.Classify(img)

    class_label=net.GetClassLabel(class_id)

    #print(class_label, confidence)
    randomvar = random.randint(0,2)
    move = "0"
    if confidence > 0.9:
        move = class_label
        if randomvar == 0:
            computer_move = "rock"
        if randomvar == 1:
            computer_move = "paper"
        if randomvar == 2:
            computer_move = "scizzors"
        if move == "rock":
            if computer_move == "rock":
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou tie")
                print("The computer played " + computer_move)
                print("You played " + move)
            if computer_move == "paper":
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou Lose")
                print("The computer played " + computer_move)
                print("You played " + move)
            if computer_move == "scizzors":
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou Win")
                print("The computer played " + computer_move)
                print("You played " + move)
        if move == "paper":
            if computer_move == "rock":
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou Win")
                print("The computer played " + computer_move)
                print("You played " + move)
            if computer_move == "paper":
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou Tie")
                print("The computer played " + computer_move)
                print("You played " + move)
            if computer_move == "scizzors":
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou Lose")
                print("The computer played " + computer_move)
                print("You played " + move)
        if move == "scizzors":
            if computer_move == "rock":
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou Lose")
                print("The computer played " + computer_move)
                print("You played " + move)
            if computer_move == "paper":
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou Win")
                print("The computer played " + computer_move)
                print("You played " + move)
            if computer_move == "scizzors":
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou Tie")
                print("The computer played " + computer_move)
                print("You played " + move)
        #output.Render(img)
        time.sleep(1)
