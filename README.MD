# Verification of Signature as Genuine or Forged

Verification of an offline Signature is performed using Convolutional Neural Networks. 

## Model Used
A pretrained VGG16 model, trained on Imagenet, is used and transfer learning is performed. Keras API is used, with TensorFlow backend. The Model was trained on Google Colab (link is given in ipynb file).

## Dataset
The Data used is a combination of SigWiComp 2009 and 2011, released by International Conference on Document Analysis and Recognition (ICDAR). Only offline signature written in Latin script are used. The data for this problem is uploaded on Google Drive at https://drive.google.com/open?id=1f4CYx3tc5F3f5__ZM0GAX3VFWOZ6n5PM. The python scripts for arranging the raw dataset into the desired form are also included.

## How to run
Simply run the ipynb fie `sigmodelv1.ipynb`. 

### Requirements
- Python 3
- Numpy
- Matplotlib
- TensorFlow
- Keras

**Note: `adjust_folders.py` and `train_test_divide.py` are only required when using raw SigWiComp data. They are not required when using the data stored on drive.**

## Result
After implementing transfer learning with VGG16 and fine tuning the last conv block, the following results were obtaibed:
- Training Accuracy: 95.23%
- Validation Accuracy: 93.37%

## Resources
- Research paper link: http://cs231n.stanford.edu/reports/2016/pdfs/276_Report.pdf
- SigWiComp dataset link: http://tc11.cvc.uab.es/datasets/SigWiComp2013_1
