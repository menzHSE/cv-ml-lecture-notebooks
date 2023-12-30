# Computer Vision and Machine Learning Jupyter Notebooks

## About

Author: Markus Enzweiler, markus.enzweiler@hs-esslingen.de

This repository contains some Jupyter notebooks used in my lectures at Esslingen University of Applied Sciences. The notebooks mainly use PyTorch (https://pytorch.org/) and are written for educational purposes with explanations and visualizations. For some topics there are notebooks available that use MLX for Apple SoCs (https://github.com/ml-explore/mlx) instead of PyTorch.  

**Feel free to use and contribute via pull requests.** 

## Contents

To work through all of the material, the following order is recommended. 

* `autograd`: demo of automatic differentiation in PyTorch and MLX
* `linear_regression`: demo of linear regression in PyTorch and MLX
* `perceptron`: multiple demos of perceptrons in NumPy, PyTorch and MLX. Some of the demos are very "spelled-out" to provide some insights into the inner working of gradient descent
* `multi_layer_perceptron`: multiple demos of multi-layer perceptrons in PyTorch and MLX including visualizations of decision boundaries
* `cnn`: demos of CNNs in PyTorch and MLX for image classification
* `vae`: demos and analyses of convolutional Variational Autoencoders (VAEs) using the MNIST and Celeb-A datasets in PyTorch

## Usage

There is a `requirements.txt` file in every folder that is automatically used by the notebooks, e.g. to install dependencies on Google Colab. For local setups, a `conda` environment with Jupyter kernels is recommended, e.g.

```
conda create --name cv-ml-torch python=3.10
conda activate cv-ml-torch
conda install ipykernel
git clone https://github.com/menzHSE/cv-ml-lecture-notebooks
pip install -r cv-ml-lecture-notebooks/multi_layer_perceptron/torch/requirements.txt
python -m ipykernel install --user --name=cv-ml-torch
```

Then you can open notebooks in your favorite tool (e.g. VSCode) and select the installed Jupyter kernel `cv-ml-torch` to execute the notebooks. 


## Contribute

Please submit pull requests for bugfixes and additional features. Besides NumPy, PyTorch and MLX, some JAX examples would be nice. 
