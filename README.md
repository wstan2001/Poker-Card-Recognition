# Poker-Card-Recognition
Screen scraping mini project conducted to detect bias in PokerStars pocket cards.

## Intro

I'm a big fan of poker, and my go-to is the PokerStars web app. However, I've been harboring a sneaking suspicion that poker software programs may be incentivized to rig the deck and let the users play bigger hands to make the game more exciting. I wanted to put part of this hypothesis to the test by collecing data about the pocket pairs I receive in PokerStars and seeing if the results match the expected distribution for a truly random deck of cards!

I decided to work in Python for convenience, but even so, I had little idea where to start. After doing a bit of research online, I began to see how to make Python interface with my Mac's screenshot capabilities and file systems, and how to build a script for image recognition. See the sources in the final section for more details.

## Screen Scraping

In poker, every player is dealt two private cards at the start of every round. Here's what it looks like on PokerStar:

<img src="/images/cards1.png" alt="PokerStars Display"/>

In the above image, you can see that my hand is the nine of diamonds and the ten of diamonds (9dTd). I needed a way to have my program take a screenshot of the part of the screen containing my cards. In reality, the only information I needed were the suits and values of each card, for a total of four screenshots per hand. Resource 1 (the Medium article) was a huge help for this and helped me structure my code. However, there were some unforeseen difficulties that I will touch on later.

The two main modules/packages that I worked with were pyscreenshot for screenshots and the Python Imaging Library (PIL or Pillow) for manipulating and interfacing with image files. 

In order to take a screenshot, I had to pass in the coordinates of opposite verticles of the rectangle section I wanted to capture. To do this on a Mac, I used cmd+shift+4 to enter screenshot mode, which displayed the coordinates of points on the screen next to my cursor:

<img src="/images/screenshot.JPG" alt="screenshot on mac"/>

For the sake of consistency, so that I didn't have to use a new set of coordinates everytime, I had to standardize my PokerStars screen placement. This would end up causing some troubles with my first approach of image hashing... Anyways, after I took a snap using pyscreenshot, I could then save the file. The PIL module then allowed me to open and work with my images. The primary way I interfaced with the images was through the getdata() method, which returned a sequence-like object of the flattened RBG pixel values. I had to first cast this object into a list in order to manipulate it.

## Attempt 1: Image Hashing

The first thing I tried followed the guidelines from the Medium article.

## Attempt 2: ML & CNN

## Conclusion

## Resources
