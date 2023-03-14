
drafting.py

    This is a simple cli program which can accomplish the
    simple task of drawing an image using lines. Like a CNC machine!

    Could be useful for a variety of purposes,
    like producing great image prompts for https://scribblediffusion.com/

    Or a robotics application!
    


Install:

download python 3.11~
from this folder run: pip install -r requirements.txt

How to Operate:

help:
    python main.py -h

script example:
    python main --width 150 --height 250 --scaling 4 --draw-delay 0.005

    all these arguments are optional, default size is 510x510 for the scribble diffusion window
    
    I recommend always using scaling or else the drawing takes really long. Default is 3.
    Scaling will downsample your drawing and spread out the points to fill the same size.
    
    Don't lower draw delay for web-based drawing, because it may glitch your window. 
    0.01 is the default value, but mileage may vary.

