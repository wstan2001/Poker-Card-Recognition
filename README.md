# Poker-Card-Recognition
Screen scraping mini project conducted to detect bias in PokerStars pocket cards.

## File Info

Everything in the images folder can be ignored. That is just to make this README more friendly.

hashhandler.py contains my first attempt at card recognition via hashing. I recommend you ignore this too.

DataCollect.py has the code for taking screenshots of the part of the screen containing cards and saving it locally. You most likely have to adjust the image coordinates in order to properly use it. Right now the coordinates work for my 13-inch 2017 Macbook Pro with the PokerStars window oriented a certain way.

Note that I did NOT include the trained weighted models in this repo, since those files are quite large. 

modeltrain.py is what you should run to train the model and save it as a .h5 file. You should have two models, one for cards suits and another for card values.

modeleval.py is a quick verification script to check the model accuracy.

DigRec.py is what you should run after training models and will evaluate the cards you are dealt in real time. I may add some threading code to automate this process (see hashhandler for reference).

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

The first thing I tried followed the guidelines from the Medium article. The idea is to store hashes of all possible suits and values and use the hash to identify each card. The training process for this was a bit painstaking because I had to type in each suit and value by hand and map it to the corresponding hash in a dictionary. To simplify the process a bit I converted the RGB values into greyscale using a weighted sum. This would let me use one hash for both red and black suits/values.

I worked with Python's imagehash modules and tried out three different types of hashing (ahash, phash, dhash) to see which one worked the best. Unfortunately, I kept running into problems where I would snap a photo of say a heart, find its hash, then later snap another photo of a heart, and find out it had a different hash! I did some testing and found out the order of the cards didn't matter, so I was a bit confused at what the issue was. Taking a closer look at the images I was screenshotting gave it away:

<img src="/images/cards2.png" alt="screenshot on mac"/>

Notice that in the bottom left corner of the first card's suit there is a circle displaying my profile image. This circle actually pulses light when it's my turn to act, so this was the culprit behind the varying hashes! I had to tweak the screenshot coordinates to exclude the pulsing circle. This helped somewhat, but the issue with the same suit/value giving different hashes persisted, which was extremely annoying. Originally, I was planning on having a dictionary mapping suit hashes to suit and value hashes to value. The sizes of these dictionaries should have been 4 and 13, respectively, but with the non-injective hashes the dictionaries could grow beyond this... I belive the problem was that the hashes I was using were too specific; moving the screen even a few pixels would produce totally different hashes for my pictures, so I had to align my screen with a margin of error of only a few pixels, which was a pain. I wasn't able to figure out a method to make the hashes more robust, so I decided to try something else.

## Attempt 2: ML & CNN

In all honesty, machine learning is a bit overkill for the problem I was trying to solve. I wasn't really expecting the model to generalize much. Another way of saying this is that my test set is going to look almost exactly like my training set, except perhaps shifted by a few pixels. The only generalization I needed was to account for the translations.

Thus, when I collected training data, I tried shifting my screen in various positions so that my training data was not all identical. In the end, I collected about 100 training samples for suits and maybe around 150 for the values. This is not too many compared to the 60000 training examples of the MNIST dataset, but I figured since my problem was simpler I didn't need as many samples. 

I followed the neural network architecture given in resource 2 to train my CNN. It wasn't anything too fancy, just a couple of 3x3 kernels ran on my 36x26 training examples followed by maxpooling and dropouts before finally flattening everything before the last dense layer and using softmax activation since I was trying to do classification. My training set was pretty small, so I trained over 10-12 epochs, getting 100% accuracy by the end. After evaluating and testing it in real time, the model seems to work really well! Again, I don't think overfitting is a huge concern here since I don't really need my model to generalize much.

## Conclusion

This was a fun little exercise. I was absolutely blown away at how easy it all was. The Python modules I needed all existed beforehand. There were free online guides that walked me through how to take screenshots using Python and how to design a CNN. All that remains is data collection and answering the original question: is the PokerStars software unbiased? (Updates to come!)

## Resources

1. Hashing + Screen Scraping: https://medium.com/@colebuildanddevelop/screen-scraping-for-real-time-poker-data-25053f572bab

2. ML: https://data-flair.training/blogs/python-deep-learning-project-handwritten-digit-recognition/
