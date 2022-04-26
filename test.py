import glob

import nibabel as nib

import Reza_functions as RF

IMAGE = 'input/example'

print('Loading test case...')
Tr_list = glob.glob(IMAGE+'/*.gz')
y = Tr_list[0]
x = y[len(IMAGE)+1:len(IMAGE)+4]
vol = nib.load(y)
seg = nib.load(IMAGE+'/MASK_' + x)

print('Get the axials input and corresponding masks...')
vol_ims, lung, around_lung, FOV = RF.return_axials(vol, seg)
segmentation  = seg.get_fdata()

print('First test done.')

from keras.callbacks import ModelCheckpoint, ReduceLROnPlateau
print('Check callbacks...')
mcp_save = ModelCheckpoint('weight_lung', save_best_only=True, monitor='val_loss', mode='min')
reduce_lr_loss = ReduceLROnPlateau(monitor='val_loss', factor=0.1, patience=7, verbose=1, epsilon=1e-4, mode='min')
print('Second test done.')


import matplotlib as plt
print('Check matplotlib...')
fig,ax = plt.subplots(5, 3, figsize=[15,15])
plt.savefig('TEST_IMAGE.png')
print('Third test done.')

