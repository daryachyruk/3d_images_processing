import numpy as np
import skimage
import cv2
from skimage.io import imshow, imsave
from numpy import clip
from skimage import img_as_float
from matplotlib import pyplot as plt


def main():
    import cv2 as cv
    from matplotlib import pyplot as plt
    from skimage.morphology import disk
    from skimage.filters.rank import enhance_contrast_percentile
    from skimage.io import imread
    from PIL import Image, ImageDraw

    def tobinary(name_img):
        image = Image.open(name_img)
        draw = ImageDraw.Draw(image)
        width = image.size[0]
        height = image.size[1]
        # _____________
        max_y = 0
        min_y = height
        max_x = 0
        min_x = width
        # __________________
        pix = image.load()
        # factor = 100
        for i in range(width):
            for j in range(height):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                S = a + b + c
                if S > 200:
                    a, b, c = 255, 255, 255
                    if i > max_x:
                        max_x = i
                    if j > max_y:
                        max_y = j
                    if i < min_x:
                        min_x = j
                    if j < min_y:
                        min_y = j
                else:
                    a, b, c = 0, 0, 0
                draw.point((i, j), (a, b, c))
        area = (min_x, min_y, max_x, max_y)
        cropped = image.crop(area)
        cropped.save('bin_thresh.jpg', "JPEG")
        del draw
        return min_x

    def get_corner_params(image_name):
        image = Image.open(image_name)
        draw = ImageDraw.Draw(image)
        width = image.size[0]
        height = image.size[1]
        # _____________
        x1 = x2 = x3 = x4 = y1 = y2 = y3 = y4 = 0
        pix = image.load()
        # __________________
        for i in range(width):
            for j in range(height):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                S = a + b + c
                if S > 200:
                    x3 = i
                    y3 = j
                    counter_x = counter_y = 0
                    for n in range(height % 4):
                        if pix[x3-counter_x-1, y3+counter_y][0] > 255:
                            draw.point((x3-counter_x, y3+counter_y), (75, 0, 130))
                            print("1, ", x3-counter_x, ',', y3+counter_y)
                            counter_x += 1
                            continue
                        elif pix[x3-counter_x-1, y3+counter_y+1][0] > 255:
                            draw.point((x3 - counter_x, y3 + counter_y), (75, 0, 130))
                            print("2, ", x3 - counter_x, ',', y3 + counter_y)
                            counter_x += 1
                            counter_y += 1
                            continue
                        elif pix[x3 - counter_x, y3 + counter_y + 1][0] > 255:
                            draw.point((x3 - counter_x, y3 + counter_y), (75, 0, 130))
                            print("3, ", x3 - counter_x, ',', y3 + counter_y)
                            counter_y += 1
                            continue
                        else:
                            print('x3=', x3, ', y3= ', y3, ', x2 = ', x3-counter_x, ', y2= ', y3+counter_y)
                            break

        image.save('privet.jpg', 'JPEG')
        del draw
        return

    hsv_min = np.array((0, 54, 5), np.uint8)
    hsv_max = np.array((187, 255, 253), np.uint8)


    def find_countours(image_filtered):
        img = cv.imread(image_filtered)
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)  # меняем цветовую модель с BGR на HSV
        thresh = cv.inRange(hsv, hsv_min, hsv_max)  # применяем цветовой фильтр
        _, contours0, hierarchy = cv.findContours(thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        # перебираем все найденные контуры в цикле
        for cnt in contours0:

            rect = cv.minAreaRect(cnt)  # пытаемся вписать прямоугольник
            box = cv.boxPoints(rect)  # поиск четырех вершин прямоугольника
            box = np.int0(box)  # округление координат
            area = int(rect[1][0] * rect[1][1])  # вычисление площади

            if area > 25:
                print('contour ', cnt)
                print(box)
                cv.drawContours(img, [box], 0, (255, 0, 0), 2)  # рисуем прямоугольник

        thresh = cv.inRange(hsv, hsv_min, hsv_max)
        _, contours0, hierarchy = cv.findContours(thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        for cnt in contours0:
            if len(cnt) > 4:
                ellipse = cv.fitEllipse(cnt)
                cv.ellipse(img, ellipse, (0, 0, 255), 2)

        cv.imshow('contours', img)  # вывод обработанного кадра в окно
        plt.imsave('contours.jpg', img)

        cv.waitKey()
        cv.destroyAllWindows()


   # img = imread('example.jpg', 0)
   # r = img[:, :, 0]
   # noisy_image = r
    #penh = enhance_contrast_percentile(noisy_image, disk(5), p0=.1, p1=.9)
    #ret, thresh1 = cv.threshold(penh, 100, 255, cv.THRESH_BINARY)
    #plt.imsave("thresh_1.jpg", thresh1)
    #tobinary('thresh_1.jpg')
    #get_corner_params('bin_thresh.jpg')
    find_countours('thresh_1.jpg')



if __name__ == "__main__":
    main()
