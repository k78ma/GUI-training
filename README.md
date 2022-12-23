# Training GUI Documentation
**Important:** Some files are missing (too large to upload to GitHub)

## Requirements:
For a full list of requirements, see [requirements.txt](https://github.com/k78ma/GUI-training/blob/master/requirements.txt).
To use this to create a conda environment for the GUI, use: <br>
`conda create --name gui --file requirements.txt`


## Starting the GUI through terminal
1. Create a conda environment named `gui` with the required packages above.
2. Activate the environment using `conda gui`.
3. Switch to the correct directory with `cd trainGUI`.
4. Run the GUI using `python gui.py`.

## Usage of GUI
- Set session name, training data, and output directory on the "Main" tab.
- Help and quit buttons are available at the bottom. <br> <br>
![Main Page](https://user-images.githubusercontent.com/77073162/209293167-8c0b0e24-06e8-4141-a364-df90cf042522.png)
---
- Then, training hyperparameters can be set using the "Parameters" tab.
- Recommended parameters can be automatically inserted (shown in picture) using the bottom-left "Use default" button.
- After inputting parameters, they can be set and saved using the "Set parameters" button. <br> <br>
![Parameters](https://user-images.githubusercontent.com/77073162/209293200-cee27aa3-c119-4219-ac79-b01d8e4151c5.png)
---
- After setting parameters, use the "Start training" button to begin training.
- The top progress bar will show the total progress of the training process (current epoch / total epochs).
- The bottom progress bar will show the progress of the current epoch.
- After finishing, a pop-up will appear indicating that training has finished. <br> <br>
![Progress Bar](https://user-images.githubusercontent.com/77073162/208041536-9b932eb4-a284-46f8-b933-7867b94db08a.png) &nbsp;	&nbsp;	&nbsp;	![Pop-up](https://user-images.githubusercontent.com/77073162/208041943-b6cdd719-e53d-412f-acca-b37f1ec4eb3e.png)
---
- After training, loss, FP rate, FN rate, and PGI plots are available in their respective tabs. An example loss graph is shown below. 
- The plots support panning, zooming, saving, and custom configuration, all done through the bottom toolbar. 
- Hovering over a given plot point with your mouse will show coordinates in the bottom right, allowing you to view exact models. <br> <br>
![Loss plot](https://user-images.githubusercontent.com/77073162/209293233-132dae05-cc63-48bb-9e53-13d92ae64378.png)

