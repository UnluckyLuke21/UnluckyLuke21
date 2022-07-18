import cv2

image = cv2.imread("example.jpeg")

cv2.imshow('frame', image)

while True:

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()