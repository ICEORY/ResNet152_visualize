import pdf2image
import os

root = "feature_png/"
if not os.path.isdir(root):
    os.mkdir(root)
count = 0
images = pdf2image.convert_from_path('feature_pdf/all.pdf')
for img in images:
    img.save("%s/%d.PNG"%(root, count))
    count += 1
