import cv2 as cv

f = open("coords.txt", "w")


# mouse callback function to write points selected
def get_coord(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        # Shows points selected
        cv.putText(img, "coordinates (%d,%d)" % (x, y), (60, 60), 2, 1, (0, 255, 0))
        print('('+str(x)+','+str(y)+")")
        f.write(str(x) + "\n")
        f.write(str(y) + "\n")


img = cv.imread("cert1.jpg")
# Displaying Image in a seperate window
cv.namedWindow('image')
cv.setMouseCallback('image', get_coord)
while (1):
    cv.imshow('image', img)
    if cv.waitKey(10) & 0xFF == 27:  # Press Escape Key to terminate window
        break
cv.destroyAllWindows()
f.close()
