import os

import nibabel as nib
import numpy as np

import Reza_functions as RF
import models as M

print("Starting test.py...")
IMG = 'input/test_files/IMG_0078.nii.gz'
MASK = 'input/test_files/MASK_0078.nii.gz'
WEIGHT = 'input/test_files/weight_lung.hdf5'

if (os.path.exists(IMG) and
    os.path.exists(MASK) and
    os.path.exists(WEIGHT)):
    print("Test files have been uploaded")
else:
    raise Exception("Some of test files are missing")

print("Prepare data...")
Data_train = []
FOV_train = []

try:
    vol = nib.load(IMG)
    seg = nib.load(MASK)
except Exception:
    raise Exception("Validation test failed")


vol_ims, lung, around_lung, FOV = RF.return_axials(vol, seg)
segmentation = seg.get_fdata()

for idx in range(vol.shape[0]):
    if ~(np.sum(np.sum(np.sum(segmentation[idx, :, :]))) == 0):
        Data_train.append(vol_ims[idx, :, :])
        FOV_train.append(FOV[idx, :, :])

if (len(Data_train) == 0 or
    len(FOV_train) == 0):
    raise Exception("Preparation result is empty")

Data_train = np.array(Data_train)
FOV_train = np.array(FOV_train)

alpha = np.int16(np.floor(Data_train.shape[0] * 0.7))
en_d = Data_train.shape[0]
Test_img = Data_train[alpha:en_d, :, :]
FOV_te = FOV_train[alpha:en_d, :, :]

Test_img  = np.expand_dims(Test_img, axis=3)
te_data2 = Test_img /255.
print("Data ready")

print("Predict Model...")
try:
    model = M.BCDU_net_D3(input_size = (512,512,1))
    model.summary()
    model.load_weights(WEIGHT)
    predictions = model.predict(te_data2, batch_size=2, verbose=1)
except:
    raise Exception("Model installation error")

predictions = np.squeeze(predictions)
predictions = np.where(predictions>0.5, 1, 0)
Estimated_lung = np.where((FOV_te - predictions)>0.5, 1, 0)

print ("All tests have finished successfully!!")

