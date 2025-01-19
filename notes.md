## How does the YOLO Model Work?

- YOLO Modelling: Performs Image Classification and Object Detection. (Where exactly is the object in the image)
Neural Network Output: Bounding Box, Class, Confidence.

- Output may look like: [Pc, Bx, By, Bw, Bh, C1, C2, C3, C4, C5, C6, C7, C8] 
- We can train a neural network that can classify the object and give the bounding boxes
- Where the X_Train may be the image and then they y_train will be the vector of the bounding boxes and the class [Pc, Bx, By, Bw, Bh, C1, C2, C3, C4, C5, C6, C7, C8]

- If we want more than 1 Bounding Box: We need to use a grid of cells where we can encode a vector that determines the bounding box and the class for each cell. 
- Note if we can have a 4x4 grid and then a vector of 8 for the output then we have 4x4x8 grid for the output. Y_train

### There are a couple issues still with this Approach:
- There may be multiple bounding boxes for the image.
- What if there are multiple objects within the same cell? This means the vector can only represent 1 class. 

- Solution: We can use a non-max suppression to remove the bounding boxes that are overlapping.
- Done by IOU (Intersection Over Union) if it shares more than 50% of the area with the max then we can remove the bounding box.

- Solution: How about we have a larger vector with mutliple anchor boxes. 
- The idea of having multiple anchor boxes per grid cell is to enable the detection of objects of different sizes in the same grid cell.
- anchor boxes are basically like having different sized boxes per each grid cell that can detect smaller medium and larger objects from a grid cell. 

## Architecture of YOLO
- CNN with convolutional layers
- 2 Fully connected layers with output ex: 7x7x30
- 7x7 is the grid size and 30 is the output vector size. 
- 30 is the output vector size. 



### Important Steps
- Training the Model
- 