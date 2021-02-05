#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 21:34:05 2020

@author: stanley
"""

from PIL import Image
import pyscreenshot as ImageGrab
import imagehash
import threading

"""
suits appear more than once because they appear in cards 1/2
values appear more than once becase they appear in cards 1/2 and
colors red/black
"""
#SMALL SCREEN HASHES
val_dict = {
 '7f435d7973674f41': '2',
 '7f417363797d4963': '3',
 '3f3373634b417373': '4',
 '7f435f47417d4963': '5',
 '7f634f435d5d4963': '6',
 '7f41597b73776767': '7',
 '7f63494b435d4963': '8',
 '3f63595d41794b63': '9',
 '7f51454545455553': 'T',
 '7f717b7b7b5b4b67': 'J',
 '7f63696949416161': 'Q',
 '7f496b67676b6941': 'K',
 '7f7763636b634949': 'A',
 
 '7f496b67676b4941': 'K',
 '7f434f43417d4963': '5',
 '7f634f434d5d4963': '6',
 '7f43597973674f41': '2',
 '7f717b7b7b5b4367': 'J'
}


 
suit_dict = {
 'f7f7e3e3c180c1e3': 'd',
 'ffffc9808080c1c1': 'h',
 'f7e3e3e3f7c08080': 'c',
 'fff7e3c1c1c08080': 's'
}




#BIG SCREEN HASHES
val_dict = {
 'ffe1f3f3f3b3b387': 'J',
 'fca3292d2d2d2d23': 'T',
 'ef819387c7979381': 'K',
 'ffe7c7c7d3c38391': 'A',
 'ffc793bb9b8383c1': 'Q',
 'ff839bb3e7cf9b83': '2',
 'ff8393f7e7e7cf4f': '7',
 'ff83a7c7d3f999c3': '3',
 'ff839f87c3f999c3': '5',
 'ff7367c7d78383e3': '4',
 'ffc39b93c3b999c3': '8',
 'f7c39bb981e1d3c3': '9',
 'ffc3938783bb9bc3': '6',
 'ff8393f7e7e7cfcf': '7',
 'ff819387c7979381': 'K',
 'ffc399d9c39999c3': '8',
 'ffb363e3c381c3f3': '4',
 '7ff1f3fbfbbb93c3': 'J',
 'feb1a5adadadadb1': 'T',
 'ff81b3e3e9fd99c3': '3',
 'ffe7e7c3c3c3c399': 'A',
 'ffc399b9e3cf9f81': '2',
 'e781d3d7c7d3db81': 'K',
 '7f8193f3e7e7e74f': '7',
 'ffc3db87839999c3': '6',
 'f7c39999c1e1d9c3': '9',
 'ffe7e7e3c3c3c399': 'A',
 'ffc39b9b9b8393c1': 'Q',
 '7fc3dfc3c1f999c3': '5',
 'ef81d3d7c7d3db81': 'K',
 '7fc399b9e3cf9f81': '2',
 'ff81d3d7c7d3db81': 'K'
}


suit_dict = {
 'ffdb8180818181c3': 'h',
 'ffe7e3c381818080': 's',
 'ffe7e3e7e7818080': 'c',
 'ffe7e7c3c38181c3': 'd',
 'fff7e3c1c1808080': 's',
 'ffdd88808080c1c1': 'h',
 'f7e3e3e3f7808080': 'c',
 'f7f7e3e3c180c1c3': 'd'
}
  

class HashHandler:
    """
    Ideally suitval_dict should be intrisic to this class, but for
    data collection purposes I'm making it global for now
    """
    def __init__(self, screen_position, d={}):
        self.screen_position = screen_position
        self.d = d
        
    def take_screenshot(self):
        im = ImageGrab.grab(bbox = self.screen_position)
        im.save('hash.png')
        return imagehash.average_hash(Image.open('hash.png'))
    
    def identify_hash(self, image_hash):
        h = str(image_hash)
        if h in self.d:
            #print(self.d[h])
            return self.d[h]
        else:
            print("unrecognized hash: " + h)
            """
            #code for collecting hashes
            suitval = input("Enter correct suit/value: ")
            if suitval != "cancel":
                self.d[h] = suitval
                return suitval
            """
            return "?"
            
    def snap_and_id(self):
        return self.identify_hash(self.take_screenshot())
        
        
#Coordinates
#small screen
val1 = HashHandler((418, 652, 438, 675), val_dict)
suit1 = HashHandler((420, 676, 435, 686), suit_dict)
val2 = HashHandler((478, 652, 498, 675), val_dict)
suit2 = HashHandler((480, 676, 495, 686), suit_dict)

#big screen
val1 = HashHandler((545, 576, 568, 603), val_dict)
suit1 = HashHandler((547, 609, 565, 622), suit_dict)
val2 = HashHandler((625, 576, 648, 603), val_dict)
suit2 = HashHandler((627, 609, 645, 622), suit_dict)


handhist = []
prevHand = ""


def getHand():
    v1 = val1.snap_and_id()
    s1 = suit1.snap_and_id()
    v2 = val2.snap_and_id()
    s2 = suit2.snap_and_id()
    hand = v1 + s1 + v2 + s2
    print(hand)
    return hand


def collect_data():
    threading.Timer(8.0, collect_data).start()
    global prevHand
    curHand = getHand()
    if curHand[1] != '?' and curHand[3] != '?' and curHand != prevHand:
        handhist.append(curHand)
        print("NEW HAND: " + curHand)
        prevHand = curHand
        
collect_data()
        
  
    
def saveHands():
    with open("handhistory.txt", 'a') as file:
        for hand in handhist:
            file.write(hand + '\n')
    
    
                

"""
val_dict length: 19

9 was of clubs
K, 7 have color match issues?
"""
    
    
        
        