# Coral identifier

We chose to investigate coral reefs based on satellite data. Out process for four-fold.

### The process
Firstly, we created a dataset with satellite images as input, and whether the image contained coral reefs as label.

Then, we trained a neural network with https://www.customvision.ai to be able to identify images that contain coral reefs.

After that, we created a react frontend where you can upload an image to get real time analysis on you satellite images.

Lastly, we created a color-matching algorithm to locate and quantize the magnitude of each reef in the image. We hosted this on a simple rest api in flask, python.

### Datasets
For data about coral reef locations we used data from https://allencoralatlas.org/atlas/, specifically the downloadable data packaged for the coral sea, the northwestern caribbean and the red sea. We took the locations of the coral/algae category in the benthic map and matched those with the coordinates in the metadata of the pictures in the Landsat 8 Collection 2 Level-2 image set. We downloaded the preview images, which had a fitting size if 1000x1000 and labeled those as containing coral reefs. For the images labeled ocean, we found some areas containing both coast and ocean without coral reefs and downloaded a lot of Landsat 8 images from those areas to use them as negatives during training, marked as ocean.
