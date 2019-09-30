# Verification of Signature using Siamese Network
Verification of an offline Signature by one-shot detection is performed using Siamese Networks. 

## Model Used
A Siamese Net with two CNN branches and shared weights is trained from scratch. Keras API is used, with TensorFlow backend. The Model was trained on Google Colab (link is given in ipynb file).

## Dataset
The Data used is a combination of SigWiComp 2009 and 2011, released by International Conference on Document Analysis and Recognition (ICDAR). Only offline signature written in Latin script are used. The data for this problem is uploaded on Google Drive at https://drive.google.com/open?id=1Yl0rHj967vUWGENkcnpapi1MAwa726M2. The python script for arranging the raw dataset into the desired form is also included.

## How to run
Simply run the ipynb fie `sigmodelv2.ipynb`. 

### Requirements
- Python 3
- Numpy
- Matplotlib
- TensorFlow
- Keras v 2.1.6

**Note:**
- **`adjust_files_siamese.py` is only required when using raw SigWiComp data. It is not required when using the data stored on drive.**
- **This build does not work with Keras v 2.2 or above. Please install Keras v 2.1.6 to run it.**



## Result
A subset of the full dataset was used to avoid timeout on Google Colab. Training Loss on this subset was 8.8125e-04 and Validation Loss was 0.0556

## Resources
- Research paper link: 
    https://arxiv.org/pdf/1707.02131.pdf  
    https://www.cs.cmu.edu/~rsalakhu/papers/oneshot1.pdf
- SigWiComp dataset link: http://tc11.cvc.uab.es/datasets/SigWiComp2013_1
