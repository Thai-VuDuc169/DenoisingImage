import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import pathlib
import os
from BoundaryExtraction import extractInBound 
np.random.seed(42)

current_folder_path = str(pathlib.Path(__file__).parent.absolute())
print("Hello {}!, the current folder path is '{}' in this system"
        .format(os.getlogin(), current_folder_path ))


img = cv.imread(current_folder_path + "//TestConnectedComponent2.png", 0) # "//ImgTestResource//VietAnh2.jpg"
_, img = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
# img = cv.xphoto.oilPainting(src= img, size= 6, dynRatio= 1)
# img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# plt.imshow(img, "gray")
# plt.show()

def getNeighborsLabels(img, x, y, labels): # 8-connectivity
  # điểm (0, 0)
  if (x == 0 and y == 0): return []
  # biên trên của img
  if (x == 0):
    if labels[x][y-1] == 0: return []
    else: return labels[x][y-1]
  # biên trái của img
  if (y == 0):
    if (labels[x-1][y] == 0 and labels[x-1][y+1] == 0): return []
    else:
      temp_list = []  
      if labels[x-1][y] != 0: temp_list.append(labels[x-1][y]) 
      if labels[x-1][y+1] != 0: temp_list.append(labels[x-1][y+1]) 
      return temp_list
  # biên phải của img
  if (y == img.shape[1] - 1):
    if (labels[x][y-1] == 0 and labels[x-1][y-1] == 0 
        and labels[x-1][y] == 0):
      return []
    else:
      temp_list = []  
      if labels[x][y-1] != 0: temp_list.append(labels[x][y-1]) 
      if labels[x-1][y-1] != 0: temp_list.append(labels[x-1][y-1]) 
      if labels[x-1][y] != 0: temp_list.append(labels[x-1][y])
      return temp_list
  # phần an toàn
  if (labels[x][y-1] == 0 and labels[x-1][y-1] == 0 and 
      labels[x-1][y] == 0 and labels[x-1][y+1] == 0):
    return []
  else:
    temp_list = []
    if labels[x][y-1] != 0: temp_list.append(labels[x][y-1]) 
    if labels[x-1][y-1] != 0: temp_list.append(labels[x-1][y-1]) 
    if labels[x-1][y] != 0: temp_list.append(labels[x-1][y])
    if labels[x-1][y+1] != 0: temp_list.append(labels[x-1][y+1])
    return temp_list

def getUnion(*args):
  final_list = list(set().union(*args))
  return final_list

def minLabelsList(linked):
  # idea: min elements of the nested array then union arrays, count them 
    for i in range(len(linked)):
      try:
        linked[i] = min(linked[i])
      except:
        # trường hợp xảy ra linked[i] chứa [] - a empty list
        continue

def connectComponent(img):
  h, w = img.shape
  labels = np.zeros_like(img)
  next_label = 1
  linked = [] # Equivalent Labels: SetID <=> label(not 0); Equivalent Labels <=> link to labels
  for row in range(h):
    for column in range(w):
      if img[row][column] != 0:
        neighbors_labels = getNeighborsLabels(img, row, column, labels)
        if not neighbors_labels:  # neighbors is empty
          # linked[NextLabel] = set containing NextLabel
          linked.append([])
          labels[row][column] = next_label
          next_label += 1
        else:
          try:
            # find the smallest label
            labels[row][column] = min(neighbors_labels)
            for label in neighbors_labels:
              linked[label-1] = getUnion(linked[label-1], neighbors_labels)
          except:
            continue
  #second pass
  # if (not linked):
  #      print("failldlldll")
  minLabelsList(linked)
  for row in range(h):
    for column in range(w):
      if labels[row][column] != 0: 
        labels[row][column] = linked[ (labels[row][column])-1 ]
  true_val_labels = set().union(linked)  
  return true_val_labels, labels 

# present result with colors
def genColor(num_colors):
  temp_colors = []
  for i in range(num_colors):
    color = list(np.random.choice(range(256), size=3))
    temp_colors.append(color)
  return temp_colors

def showResult(labels_val, labels):
  color_list = genColor(len(labels_val)) # tạo ra mảng chứa số lượng màu tương ứng với các labels
  color_dict = dict(zip(labels_val, color_list)) # key: labels; value: mỗi màu tương ứng với từng labels
  result = np.zeros((labels.shape[0], labels.shape[1], 3)) # mảng chứa kết quả
  for row in range(labels.shape[0]):
    for column in range(labels.shape[1]):
      if(labels[row][column] != 0):
        # gán các màu tương ứng với từng labels trong color_dict
        result[row, column] = color_dict[labels[row][column]]  
  return result

# main
labels_val, labels = connectComponent(img)
result = showResult(labels_val, labels).astype(int)
print(labels)
print("labels' value: ", labels_val)
plt.subplot(121)
plt.title("INPUT IMAGE")
plt.imshow(img, "gray")
plt.axis('off')
plt.subplot(122)
plt.title("RESULT")
plt.imshow(showResult(labels_val, labels).astype(int))
plt.axis('off')
plt.show()






# =============A EXAMPLE USE THE SKIMAGE LIBARARY===============

# from skimage import measure
# from skimage import filters
# import matplotlib.pyplot as plt
# import numpy as np

# n = 12
# l = 256
# np.random.seed(1)
# im = np.zeros((l, l))
# points = l * np.random.random((2, n ** 2))
# im[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1
# im = filters.gaussian(im, sigma= l / (4. * n))
# blobs = im > 0.7 * im.mean()

# all_labels = measure.label(blobs)
# blobs_labels = measure.label(blobs, background=0)

# plt.figure(figsize=(9, 3.5))
# plt.subplot(131)
# plt.imshow(blobs, cmap='gray')
# plt.axis('off')
# plt.subplot(132)
# plt.imshow(all_labels, cmap='nipy_spectral')
# plt.axis('off')
# plt.subplot(133)
# plt.imshow(blobs_labels, cmap='nipy_spectral')
# plt.axis('off')

# plt.tight_layout()
# plt.show()