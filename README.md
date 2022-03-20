# Coral identifier

We chose to investigate coral reefs based on satellite data. Out process for four-fold:

### The process
Firstly, we created a dataset with satellite images as input and whether the image contained coral reefs as label.

Then, we trained a neural network with azure custom vision (https://www.customvision.ai) to be able to identify images that contain coral reefs.

After that, we created a react frontend where you can upload an image to get real time analysis on your satellite images.

Lastly, we created a color-matching algorithm to locate and quantify the magnitude of each reef in the image. This algorithm is also capable of outlining the coral reefs. It is accessible through a simple rest api in flask, python.

### Datasets
For data about coral reef locations we used data from https://allencoralatlas.org/atlas/, specifically the downloadable data packaged for the coral sea, the northwestern caribbean and the red sea. We took the locations of the coral/algae category in the benthic map and matched those with the coordinates in the metadata of the pictures in the "Landsat 8 Collection 2 Level-2" image set.

We downloaded the preview images, which had a fitting size of approximately 1000x1000 and labeled those as containing coral reefs. For the images labeled ocean, we found some areas containing both coast and ocean without coral reefs and downloaded many Landsat 8 images from those areas to use them as negatives during training, marked as ocean.


We used about 2000 coral and 2000 non-coral images for training.


## Training result
![bilde](https://user-images.githubusercontent.com/55250882/159153837-0d10618b-120a-4747-b25b-bfe586c5a3e9.png)


## Application
### Negative result
![bilde](https://user-images.githubusercontent.com/55250882/159137440-84ef309f-0922-4956-89f2-162e749063ac.png)


### Positive result
![bilde](https://user-images.githubusercontent.com/55250882/159137485-cde6aa6d-da3a-44cb-9c06-65c821b1f2a0.png)
