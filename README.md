# Training GUI Documentation.
**Important:** `"/Bert_TCN/finance/pretrain/bert/base-uncased/pytorch_model.bin"` is missing (too large to upload to GitHub.)

## Requirements:
For a full list of requirements, see [requirements.txt](https://github.com/k78ma/GUI-training/blob/master/requirements.txt). <br>
Details on how to use this requirements file to create an environment, see below.

## Starting the GUI through terminal
1. Clone the repository.
2. Create a conda environment named `gui` with `conda create --name gui`.
3. Activate the environment using `conda gui`.
4. Install the required packages using `pip install -r requirements.txt`
4. Switch to the correct directory with `cd GUI-training`.
5. Make sure you've added the missing file `"/Bert_TCN/finance/pretrain/bert/base-uncased/pytorch_model.bin"`.
6. Run the GUI using `python gui.py`.

## Usage of GUI
### Main Tab
- Set session name, training data, and output directory on the "Main" tab.
- Help and quit buttons are available at the bottom. <br> <br>
![Main Page](https://user-images.githubusercontent.com/77073162/209293167-8c0b0e24-06e8-4141-a364-df90cf042522.png)
---
### Parameter Settings Tab
- Then, training hyperparameters can be set using the "Parameters" tab.
- Recommended parameters can be automatically inserted (shown in picture) using the bottom-left "Use default" button.
- After inputting parameters, they can be set and saved using the "Set parameters" button. <br> <br>
![Parameters](https://user-images.githubusercontent.com/77073162/209293200-cee27aa3-c119-4219-ac79-b01d8e4151c5.png)
### About Parameters
- `Epochs:` Number of iterations through the entire training dataset (Default = 50)
- `Learning rate:` Tuning parameter for optimization algorithm that determines the step size at each iteration (Default = 0.0001)
- `Batch size:` Number of samples processed before the model is updated (Default = 8)
- `Validation ratio:` Fraction of dataset that is set aside for validation (Default = 0.4)
- `Pre-trained:` True/False flag for loading a pre-trained model as the starting point (Default = False)
---
### Training and Progress Bars (Main Tab)
- After setting parameters, use the "Start training" button to begin training.
- The top progress bar will show the total progress of the training process (current epoch / total epochs).
- The bottom progress bar will show the progress of the current epoch.
- After finishing, a pop-up will appear indicating that training has finished. <br> <br>
![Progress Bar](https://user-images.githubusercontent.com/77073162/208041536-9b932eb4-a284-46f8-b933-7867b94db08a.png) &nbsp;	&nbsp;	&nbsp;	![Pop-up](https://user-images.githubusercontent.com/77073162/208041943-b6cdd719-e53d-412f-acca-b37f1ec4eb3e.png)
---
### Plots (Train/Val Loss, FP, FN, PGI)
- After training, loss, FP rate, FN rate, and PGI plots are available in their respective tabs. An example loss graph is shown below. 
- The plots support panning, zooming, saving, and custom configuration, all done through the bottom toolbar. 
- Hovering over a given plot point with your mouse will show coordinates in the bottom right, allowing you to view exact models. <br> <br>
- The PGI tab has a button at the bottom (above toolbar) that provides a pop-up explaining our novel PGI metric.
![Loss plot](https://user-images.githubusercontent.com/77073162/209293233-132dae05-cc63-48bb-9e53-13d92ae64378.png)

