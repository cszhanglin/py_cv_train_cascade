# py_cv_train_cascade
Some scripts for training OpenCV’s cascade classifier.

gen_pos.py: Create positive description file for positive file in pos/img.
gen_neg.py: The positive image file must be cutted from image using imageclipper, and the file name is like: filename_rotateangle_x_y_width_height. This script can generate negative samples from origin image while avoiding the positive regions.
gen_negdes.py: Create negative description file.
merge_vec.py: Merge several .vec files to a single one. The author's information is inside the script.
create_sample.py: Print the command line that need to be executed to create .vec file.
train_cascade.py: Print the command line that need to be executed to train.

The parameters are in the scripts and we need to carefully set up them.