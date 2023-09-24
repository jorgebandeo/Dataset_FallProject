"""
----------- testing plot box using (x1,y1,x2,y2) in pixels -----------

the code using imagem of data set and your label map, plot rectangle in image and reton 
to evaluation result. 

at the corret retun, the is not usse for yolo trainign, procced for normalization dataset.

Author: Jorge Bandeo

Date of criation 24/08/2023
Date of modification  24/08/2023 

"""
import cv2

# path for image test 
image_path = 'pessoas/PersonOIDv4/03531354205075ff.jpg'

# path fot file that contain label map for persons in image
txt_path = 'pessoas/PersonOIDv4/Label/03531354205075ff.txt'

# capture image
image = cv2.imread(image_path)

# capture label map for N box person 
with open(txt_path, 'r') as f:
    for line in f:
        # convet array to list 
        values = line.strip().split()
        # extract coordinates for box person (x1, y1, x2, y2)
        bbox = [float(v) for v in values[1:]]
        # plot retangel in image 
        cv2.rectangle(image, (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])), (255, 0, 0), 2)

# show image for evaluation
cv2.imshow('Image with Bounding Boxes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
