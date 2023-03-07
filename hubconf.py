from PIL import Image
def resize(image):
  print(image)
  im = Image.open(image)
  print(f"Original size : {im.size}")
  image = image.resize((400, 400))
  return image



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