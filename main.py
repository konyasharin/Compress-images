import time

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from QuadTree import QuadTree

if __name__ == '__main__':
    """
    # чтение и вывод изображения
    img = mpimg.imread('split-Croatia.jpg')
    print(img.shape)
    plt.imshow(img)
    plt.show()

    # делим изображение на 4 и выводим первую четверть
    split_img = split4(img)
    print(split_img[0].shape)
    plt.imshow(split_img[0])
    plt.show()

    # удобный вывод 4 изображений
    fig, axs = plt.subplots(2, 2)
    axs[0, 0].imshow(split_img[0])
    axs[0, 1].imshow(split_img[1])
    axs[1, 0].imshow(split_img[2])
    axs[1, 1].imshow(split_img[3])
    plt.show()

    # объединение 4 картинок в 1
    full_img = concatenate4(split_img[0], split_img[1], split_img[2], split_img[3])
    plt.imshow(full_img)
    plt.show()

    # выводит средний цвет для каждой четверти
    means = np.array(list(map(lambda x: calculate_mean(x), split_img))).astype(int).reshape(2, 2, 3)
    print(means)
    plt.imshow(means)
    plt.show()
    """
    img = mpimg.imread('split-Croatia.jpg')
    quadtree = QuadTree().insert(img)

    plt.imshow(quadtree.get_image(10))
    plt.show()
    plt.imshow(quadtree.get_image(7))
    plt.show()
    plt.imshow(quadtree.get_image(3))
    plt.show()
    plt.imshow(quadtree.get_image(1))
    plt.show()


