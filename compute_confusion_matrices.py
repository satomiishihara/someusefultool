# compute confusion matrices

# select a class of samples classfying by model and get the result.
# use the result to get the matrices
# https://zhuanlan.zhihu.com/p/111234566
# https://blog.csdn.net/qq_40243750/article/details/124255865

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

def get_confusion_matrices(label_true, label_pred, label_name, save_path='./fig/confusion_matrices.jpg', title='Confusion matrices'):
    cm = confusion_matrix(y_true=label_true, y_pred=label_pred, normalize='true')

    plt.imshow(cm, cmap='Blues')
    plt.title(title)
    plt.xlabel('Predict label')
    plt.ylabel('Truth label')
    plt.yticks(range(label_name.__len__()), label_name)
    plt.xticks(range(label_name.__len__()), label_name, rotation=45)

    plt.tight_layout()
    plt.colorbar()

    for i in range(label_name.__len__()):
        for j in range(label_name.__len__()):
            color = (1, 1, 1) if i == j else (0, 0, 0)
            value = float(format('%.2f' % cm[i, j]))
            plt.text(i, j, value, verticalalignment='center', horizontalalignment='center', color=color)
    plt.savefig(save_path, bbox_inches='tight', dpi=300)



label_true = np.random.randint(0, 7, size=50)
label_pred = np.random.randint(0, 7, size=50)
label_name = ['Surprise', 'Fear', 'Disgust', 'Happiness', 'Sadness', 'Anger', 'Neutral']
get_confusion_matrices(label_true, label_pred, label_name)


# example of code

# y_gt = []
# y_pred = []
# for index, (labels, imgs) in enumerate(data_set):
#     labels_pd = model(imgs)
#     predict_np = np.argmax(labels_pd.cpu().detach().numpy(), axis=1)
#     labels_np = labels.numpy()
#
#     y_pred.append(predict_np)
#     y_gt.append(labels_np)
#
# get_confusion_matrices(label_true=y_gt,
#                        label_pred=y_pred,
#                        label_name=label_name)