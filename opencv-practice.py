import cv2 as cv
cam = cv.VideoCapture(0)
result, image = cam.read()


if result:

  cv.imshow("Display", image)
  # cv.imwrite("testing.png", image)
  cv.waitKey(0)
  cv.destroyWindow("Display")

else:
  print("No image was detected.")
