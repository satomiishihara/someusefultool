# this file is drawing att_map with ori fig
# save dir: fig

import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt



def visulize_attention_ratio(img_path, attention_mask, ratio=0.5, cmap="jet"):
    """
    img_path: 读取图片的位置
    attention_mask: 2-D 的numpy矩阵
    ratio:  放大或缩小图片的比例，可选
    cmap:   attention map的style，可选
    """
    print("load image from: ", img_path)
    img_name = img_path.split("\\")[-1]
    # print(img_name)
    # load the image
    img = Image.open(img_path, mode='r')
    img_h, img_w = img.size[0], img.size[1]
    plt.subplots(nrows=1, ncols=1, figsize=(0.02 * img_h, 0.02 * img_w))

    # scale the image
    img_h, img_w = int(img.size[0] * ratio), int(img.size[1] * ratio)
    img = img.resize((img_h, img_w))
    plt.imshow(img, alpha=1)
    plt.axis('off')

    # normalize the attention mask
    mask = cv2.resize(attention_mask, (img_h, img_w))
    normed_mask = mask / mask.max()
    normed_mask = (normed_mask * 255).astype('uint8')
    # print(normed_mask.shape)
    plt.imshow(normed_mask, alpha=0.5, interpolation='nearest', cmap=cmap)
    # plt.show()
    plt.savefig('./fig/' + 'att_map' + img_name)

# test
imgpath = r'D:\RAFDB\noaug\train\0\train_00006_aligned.jpg'
attention_mask = np.random.randn(100, 100)


visulize_attention_ratio(imgpath, attention_mask)
