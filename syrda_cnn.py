# -*- coding: utf-8 -*-
"""Syrda_CNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UCosIrMvgUhwsY9LIOJ_wBK7bINUXGN-
"""

import torch
import torch.nn as nn
import torchvision.transforms as T
from PIL import Image
import matplotlib.pyplot as plt

# Загружаем файл
image = Image.open('bmw-seraya-na-zakate.jpg')

# Конвертируем изображение в тензор
Input = T.ToTensor()(image)

# Расширяем размерность
Input = Input.unsqueeze(0)
print('Input Tensor :',Input.shape)


# Определим операцию свертки
conv = nn.Conv2d(in_channels=3, out_channels=2,
                 kernel_size=7,stride=5, bias=True)
# Применяем операцию свертки
output = conv(Input)

print('Output Tensor :',output.shape)

# Сжимаем размерность
Out_img = output.squeeze(0)

# Конвертируем тензор в изображение
Out_img = T.ToPILImage()(Out_img)

# Вывододим сравнение изображений
fig, axarr = plt.subplots(1, 2, figsize=(12, 6))
axarr[0].imshow(image)
axarr[0].set_title('Input Image')
axarr[0].axis('off')

axarr[1].imshow(Out_img)
axarr[1].set_title('Output Image')
axarr[1].axis('off')

plt.show()

import numpy as np
import cv2

# Загрузка изображения
image = cv2.imread('957-lamborghini-WallFizz.jpg')

# Определение ядра свертки
kernel = np.array([[-1, -1, -1],
                   [-1, 8, -1],
                   [-1, -1, -1]])

# Применение свертки
result = cv2.filter2D(image, -1, kernel)

# Отображение исходного изображения и результирующего изображения
cv2.imwrite('result.jpg', result)

image = Image.open('957-lamborghini-WallFizz.jpg')
result = Image.open('result.jpg')

image

result