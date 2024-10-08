# -*- coding: utf-8 -*-
"""Week2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gWs2hI_ZjnMqKTLmjP0UyEdeUfejU7gW

# Matrix Inverse

$$
A = \begin{bmatrix}
-2 & 6 \\
8 & -4
\end{bmatrix}
$$

$$
det(A) = (-2)*(-4)-6*8 = -40
$$

* $det(A) \ne $ 0 so A is invertible

* $$
A^{-1} = \frac{1}{det(A)}*\begin{bmatrix} -4 & -6 \\ -8 & -2 \end{bmatrix} = \frac{-1}{40}*\begin{bmatrix} -4 & -6 \\ -8 & -2 \end{bmatrix} = \begin{bmatrix} 0.1 & 0.15 \\ 0.2 & 0.05 \end{bmatrix}
$$


* $$A^{-1} = \begin{bmatrix} 0.1 & 0.15 \\ 0.2 & 0.05 \end{bmatrix}$$

# Eigenvector and eigenvalue

* $$ A = \begin{bmatrix} 0.9 & 0.2 \\ 0.1 & 0.8 \end{bmatrix} $$

* $$ det(A - λI) = 0 \\
 => (0.9-λ)*(0.8-λ) - 0.1*0.2 = 0 \\
$$
 $$
 =>  λ = \begin{cases} 1 \\ 0.7 \end{cases}
 $$

* $$
Av = λv
$$

$$ \begin{bmatrix} 0.9 & 0.2 \\ 0.1 & 0.8  \end{bmatrix} . \begin{bmatrix} a\\b \end{bmatrix} = \begin{bmatrix} a\\b \end{bmatrix}$$

\begin{cases}
0.9a + 0.2b = a \\  
0.1a + 0.8b = b
\end{cases}
$$ => v = \begin{bmatrix} 1\\2 \end{bmatrix}$$

# Cosine Similarity
$$
x = \begin{bmatrix} 1 \\2 \\3 \\4 \end{bmatrix}
y=  \begin{bmatrix} 1\\0\\ 3\\0 \end{bmatrix}
$$

$$
cs(x, y) = \frac{x \cdot y}{\|x\| \|y\|} = \frac{1.1 + 2.0+3.3+4.0}{\sqrt{1^2 + 2^2 + 3^2 + 4^2}.\sqrt{1^2 + 0^2 + 3^2 + 0^2}} = \frac{1}{\sqrt{3}}
$$
"""

import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import cv2

#Exercise 1
def compute_vector_length (vector):
    len_of_vector = np.sqrt(np.sum(vector**2))
    return len_of_vector

def compute_dot_product (vector1, vector2 ):
    result = np.dot(vector1, vector2)
    return result

def matrix_multi_vector (matrix, vector):
    result = np.dot(matrix, vector)
    return result

def matrix_multi_matrix (matrix1, matrix2):
    result = np.dot(matrix1, matrix2)
    return result

def inverse_matrix (matrix):
    result = np.linalg.inv(matrix)
    return result

#Exercise 2
def compute_eigenvalues_eigenvectors (matrix) :
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues , eigenvectors

#Exercise 3
def compute_cosine (v1 , v2) :
    cos_sim = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    return cos_sim

#Exercise 4
foreground = cv2.imread('GreenBackground.png', 1)
newBackground = cv2.imread('NewBackground.jpg', 1)
obj = cv2.imread('Object.png', 1)

foreground = cv2.resize(foreground, (678, 381))
newBackground = cv2.resize(newBackground, (678, 381))
obj = cv2.resize(obj, (678, 381))

def compute_difference (bg_img, input_img):
    difference_single_channel = cv2.absdiff(bg_img, input_img)
    return difference_single_channel

def compute_binary_mask ( difference_single_channel ) :
    _, difference_binary = cv2.threshold(difference_single_channel, 0, 255, cv2.THRESH_BINARY)
    return difference_binary

def replace_background (bg1_image, bg2_image, ob_image):
    difference_single_channel = compute_difference(bg1_image, ob_image)
    binary_mask = compute_binary_mask(difference_single_channel)
    output = np.where(binary_mask == 255, ob_image, bg2_image)
    return output


difference_single_channel = compute_difference (foreground, obj)
difference_single_channel_rgb = cv2.cvtColor(difference_single_channel, cv2.COLOR_BGR2RGB)
replacedImg = replace_background(foreground, newBackground, obj)
replacedImg = cv2.cvtColor(replacedImg, cv2.COLOR_BGR2RGB)
plt.imshow(replacedImg)