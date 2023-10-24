# this file is counting num of every class in dataset
# dataset must be like this:

# /dataset
#     /0
#         /fig1.jpg or png or other
#         /fig2.jpg
#         ......
#     /1
#     /2
#     ......

import os
import matplotlib.pyplot as plt

# plt.style.use("ggplot")
path = r'D:\RAFDB\noaug\train'
class_all = os.listdir(path)
class_num = []
for aclass in class_all:
    data_path = path + '/' + aclass
    class_num.append(len(os.listdir(data_path)))

fig, ax = plt.subplots(figsize=(10,8))
ax.bar(x=class_all, height=class_num)
ax.set_title("class num distribution", fontsize=15)
xticks = ax.get_xticks()
for i in range(len(class_num)):
    xy = (xticks[i], class_num[i] * 1.03)
    s = str(class_num[i])
    ax.annotate(
        text=s,
        xy=xy,
        fontsize=15,
        color="black",
        ha="center",
        va="baseline"
    )
fig.savefig('./fig/class_num_distribution.jpg', dpi=300)
# fig.show()

print(class_all)
print(class_num)
