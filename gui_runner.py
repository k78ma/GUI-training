from main_bert_tcn import NRC_Revenue_Prediction_Training
from tkinter.messagebox import showinfo

def gui_runner(root):
    print(root.param_dict)
    load_path = root.outModelInput.get() # save pretrained model
    val_ratio = 0.32  # training set and validation set
    load = (root.param_dict.get('pretrained') == "True")
    epochs = int(root.param_dict.get('epochs'))
    data_path = root.uploadInputBox.get() # input data file
    batch_size = int(root.param_dict.get('batch'))
    lr = float(root.param_dict.get('lr'))  #learning rate
    NRC_Revenue_Prediction_Training (load_path, val_ratio, load, epochs, data_path, batch_size, lr, root)
    showinfo(message='Training completed!')
    #progress()