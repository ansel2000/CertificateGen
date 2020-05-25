from PIL import ImageFont, ImageDraw, Image
import cv2
import numpy as np
import Read

f1 = open("coords.txt","r")
coordinates = f1.read().split("\n")

flag=True

for i in range(len(Read.name)):
    print(i)
    if Read.category[i] == 'Pass':
        name_to_print = Read.name[i]
        date_to_print = "23/05/2020"
        subject="Machine Learning workshop"
        # Load image in OpenCV
        image = cv2.imread("cert1.jpg")

        # Convert the image to RGB (OpenCV uses BGR)
        cv2_im_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Pass the image to PIL
        pil_im = Image.fromarray(cv2_im_rgb)

        draw = ImageDraw.Draw(pil_im)
        # use a truetype font
        font = ImageFont.truetype("./fonts/Courgette-Regular.ttf", 29)  # You can change fonts from list given bottom
        font1 = ImageFont.truetype("./fonts/Tinos-Bold.ttf", 22)

        # Draw the text
        draw.text((int(coordinates[0]), int(coordinates[1])), name_to_print, font=font, fill='black')
        draw.text((int(coordinates[2]), int(coordinates[3])), subject, font=font, fill='black')
        draw.text((int(coordinates[4]), int(coordinates[5])), date_to_print, font=font1, fill='blue')

        # Get back the image to OpenCV
        cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)

        if flag:
            cv2.imshow('Certificate', cv2_im_processed)  # Shows sample image
            flag = False

        cv2.imwrite('./output/' + name_to_print + '.png', cv2_im_processed)
        cv2.waitKey(0)

        cv2.destroyAllWindows()



