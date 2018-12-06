

noisy_image = cv.imread('example.jpg', 0)

penh = enhance_contrast_percentile(noisy_image, disk(5), p0=.1, p1=.9)

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 10),
                         sharex='row', sharey='row')
ax = axes.ravel()

ax[0].imshow(noisy_image, cmap=plt.cm.gray)
ax[0].set_title('Original')

ax[1].imshow(penh, cmap=plt.cm.gray)
ax[1].set_title('contrast enhancement')

for a in ax:
    a.axis('off')

plt.tight_layout()
plt.show()
# _____________________________________________________
img = cv.medianBlur(img, 5)
ret, th1 = cv.threshold(img, 170, 255, cv.THRESH_BINARY)

titles = ['Original Image', 'Global Thresholding (v = 127)']
images = [img, th1]
for i in range(2):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
#_________________________________________________________________


img = cv.imread('example.jpg', 0)
ret, thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)


titles = ['Original Image', 'BINARY']
images = [img, thresh1]

for i in range(2):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()


#__________________________________________________________
m = cv.imread('example.jpg', 0)

radius = 15
t = rank.otsu(m, disk(radius))

fig, ax = plt.subplots(ncols=2, figsize=(10, 5),
                       sharex=True, sharey=True)

ax[0].imshow(m, cmap=plt.cm.gray)
ax[0].set_title('Original')

ax[1].imshow(m >= t, interpolation='nearest', cmap=plt.cm.gray)
ax[1].set_title('Local Otsu ($r=%d$)' % radius)

for a in ax:
    a.axis('off')

plt.tight_layout()
plt.show()




# ________________________________________________________________


# red color - r: 128-255 g: 0-128 b: 0-128
# yellow color - r: 128-255 g: 128-255 b: 0-170
# green color - r: 0-128 g: 128-255 b: 0-154
# blue color - r: 0-128 g: 128-255 b: 128-255


def main():
    container_img = cv2.imread('example.jpg')
    print(type(container_img), container_img.shape)

    low_red = (128, 0, 0)
    high_red = (255, 128, 128)
    only_red = cv2.inRange(container_img, low_red, high_red)
    cv2.imshow('red', only_red)
    #cv2.waitKey(0)

    low_yellow = (128, 128, 0)
    high_yellow = (255, 255, 170)
    only_yellow = cv2.inRange(container_img, low_yellow, high_yellow)
    cv2.imshow('yellow', only_yellow)
    #cv2.waitKey(0)

    low_green = (128, 0, 0)
    high_green = (255, 128, 128)
    only_green = cv2.inRange(container_img, low_green, high_green)
    cv2.imshow('green', only_green)



