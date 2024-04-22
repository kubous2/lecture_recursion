import matplotlib.pyplot as plt

def flood_fill(image, x,y):
    if x < 0 or y < 0 or x >= len(image[0]) or y >= len(image):
        return image

    if image[y][x] == 0 or image[y][x] == 2:
        return image

    image[y][x] = 2

    plt.imshow(image)
    plt.pause(0.05)
    plt.clf()

    flood_fill(image, x+1, y)
    flood_fill(image, x-1, y)
    flood_fill(image, x, y+1)
    flood_fill(image, x, y-1)
    return image




def main():
    #img = plt.imread("files/img0.png")[:, :, 0]
    img = plt.imread("files/img1.png")[:, :, 0]
    #img = plt.imread("files/img2.png")[:, :, 0]

    image = flood_fill(img, 2, 0)

    plt.imshow(img, cmap="gray")
    plt.show(block=False)
    plt.pause(5)
    plt.clf()


if __name__ == "__main__":
    main()
