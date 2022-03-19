# Coral identifier

We chose to investigate coral reefs based on satellite data. Out process for four-fold.

### The process
Firstly, we created a dataset with satellite images as input, and whether the image contained coral reefs as label.

Then, we trained a neural network with https://www.customvision.ai to be able to identify images that contain coral reefs.

After that, we created a react frontend where you can upload an image to get real time analysis on you satellite images.

Lastly, we created a color-matching algorithm to locate and quantize the magnitude of each reef in the image. We hosted this on a simple rest api in flask, python.