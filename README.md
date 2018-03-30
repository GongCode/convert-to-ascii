# Convert to ASCII

This project will convert both images and videos to block ASCII art and then print them to console.
Example Image:
![Mountain](https://github.com/danielferriss/convert-to-ascii/blob/master/media/mountain.jpg)
![10 Pixellized Mountain](https://github.com/danielferriss/convert-to-ascii/blob/master/media/10pixellation.png)
(10 pixellation)
You can also change how pixellated the result is:
![30 Pixellized Mountain](https://github.com/danielferriss/convert-to-ascii/blob/master/media/30pixellation.png)
(30 pixellation)

You can convert videos as well.

![Zebra Video](https://github.com/danielferriss/convert-to-ascii/blob/master/media/zebra.gif)
![Pixellated Zebra Video](https://github.com/danielferriss/convert-to-ascii/blob/master/media/pixelzebra.gif)
Pixellation works the same way on videos as shown earlier.

## Getting Started

Clone the repo to your machine 

### Prerequisites

Packages required:
* numpy
* skimage
* tqdm
* cv2

Install these with:
```
pip install (package)
```

### Installing

Clone repo to your machine

```
git clone https://github.com/danielferriss/convert-to-ascii.git
```

## Deployment

I haven't made this into an actual package so just place the folder in and do 
```
from (filename) import (methods you want to use)
```

## Built With

* [numpy](http://http://www.numpy.org/) - Used for array operations
* [skimage](https://http://scikit-image.org/docs/dev/api/skimage.html) - Used for image processing
* [cv2](https://https://opencv.org/) - Used for video processing
* [tqdm](https://pypi.python.org/pypi/tqdm) - Used to make progress bar

## Author

* **Daniel Ferriss** - [website](https://danielferriss.com)
