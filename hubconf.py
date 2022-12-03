import torch
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import torchvision.transforms as transforms
  
import torchvision.transforms.functional as F

from torchvision.utils import make_grid
from torchvision.io import read_image
from torchvision.utils import draw_bounding_boxes

from PIL import Image

def show(imgs):
    if not isinstance(imgs, list):
        imgs = [imgs]
    fig, axs = plt.subplots(ncols=len(imgs), squeeze=False)
    for i, img in enumerate(imgs):
        img = img.detach()
        img = F.to_pil_image(img)
        axs[0, i].imshow(np.asarray(img))
        axs[0, i].set(xticklabels=[], yticklabels=[], xticks=[], yticks=[])

def resize(image):

  im = Image.open(image)
  transform = transforms.Compose([
    transforms.PILToTensor()])
  im = transform(im)
  boxes = torch.tensor([[210, 150, 350, 430]], dtype=torch.float)
  colors = ["yellow"]
  result = draw_bounding_boxes(im, boxes, colors=colors, width=5)
  show(result)

  transform = transforms.ToPILImage()
  print(type(result))

  im = transform(result)

  return im



# V2.0
# from PIL import Image
# def resize(image):
#   im = Image.open(image)
#   print(f"Original size : {im.size}")
#   im = im.resize((400, 400))
#   print("1")
#   return im

# V1.0
# def resize(image):
#   image = request.files['img']
#   # image_path = "./images/" + image.filename
#   # image.save(image_path)
#   image = Image.open(image.stream)
#   print(f"Original size : {image.size}") # 5464x3640
#   sunset_resized = image.resize((400, 400))
#   sunset_resized.save('resized.jpeg')
#   try:
#     return send_file('resized.jpeg', download_name='resized.png', mimetype='image/png')
#   except Exception as e:
#     return str(e)