import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import pathlib
import os

current_folder_path = str(pathlib.Path(__file__).parent.absolute())
print("Hello {}!, the current folder path is '{}' in this system"
        .format(os.getlogin(), current_folder_path ))


img = cv.imread(current_folder_path + "//TestConnectedComponent2.png", 0) # GeomatryShape.jpeg
_, img = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)

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

def countTrueLabel(*args):
  # idea: split the array then union arrays
  return len(set().union(*args))

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
  # count_labels = len(set().union(linked))
  print (countTrueLabel(linked))
  # for column in range(w):
  #   if label[row][column] != 0:
  #     current_label = label[row][column]
  return labels, linked
# la, link = connectComponent(img)
# print(la)
# print ("asdfasdf")
# print(link)

a = [[1,2,3],[1,2,3], [2,3], [2,3], [3,4]]
print (countTrueLabel(a))


  # for row in range(h):

# def a(b):
#      b[0] = 1
#      print (b)

# img = np.array([0,2,2,2,2,2,2,2,2,2,2,2,2,2,2])
# a(img)
# print (img)
              
    
          









# titles = [ 'INPUT IMAGE', 'INNER BOUNDARY EXTRACTION', 'OUTER BOUNDARY EXTRACTION']
# images = [img, extractInBound(img), extractOutBound(img)]
# for i in range(len(titles)):
#         plt.subplot(2, 2, i+1)
#         plt.title(titles[i])
#         plt.imshow(images[i], "gray")
#         plt.xticks(ticks=[])
#         plt.yticks(ticks=[])
# plt.show()






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