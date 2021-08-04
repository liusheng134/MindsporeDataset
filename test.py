# import os, sys
#
# # BASE_DIR = os.path.dirname(os.path.abspath(__file__))       # __file__获取执行文件相对路径，整行为取上一级目录
# # sys.path.append(BASE_DIR)
#
#
# import mindspore as ms
#
# # print(sys.path)
#
#
# # print(__file__)
# # print(os.path.abspath(__file__))
# #
# # print(os.path.dirname(os.path.abspath(__file__)))
#
#
# """ read label binary file.
#     Args:
#         file_name (string): file path of *-label-idx3-ubyte.
#     Note:
#         file format
#         [offset] [type]          [value]          [description]
#         0000     32 bit integer  0x00000801(2049) magic number (MSB first)
#         0004     32 bit integer  60000            number of items
#         0008     unsigned byte   ??               label
#         0009     unsigned byte   ??               label
#         ........
#         xxxx     unsigned byte   ??               label
#         The labels values are 0 to 9.
# """






import struct
import gzip


def un_gz(file_name):
    # 获取文件的名称，去掉后缀名
    f_name = file_name.replace(".gz", "")
    # 开始解压
    g_file = gzip.GzipFile(file_name)
    # 读取解压后的文件，并写入去掉后缀名的同名文件（即得到解压后的文件）
    open(f_name, "wb+").write(g_file.read())
    g_file.close()


# un_gz('D:\\python36\\config.gz')

file_name = r'E:\MindsporeVision\mnist\t10k-images-idx3-ubyte.gz'

un_gz(file_name)
# bin_data = open(file_name, "rb").read()  # 以二进制打开文档
# head = struct.unpack_from('>IIII', bin_data, 0)  # 取前4个整数，返回一个元组
#
# print(head)


















# # def test():
# #     a = 12.1251
# #     packa = struct.pack('f', a)
# #     print(f"packa= {packa}")
# #
# #     unpacka = struct.unpack_from('f', packa, 0)
# #     print(unpacka)
# #
# #
# # test()
#
# # 训练集文件
# train_images_idx3_ubyte_file = 'MNIST_data/train-images.idx3-ubyte'
# # 训练集标签文件
# train_labels_idx1_ubyte_file = 'MNIST_data/train-labels.idx1-ubyte'
#
# # 测试集文件
# test_images_idx3_ubyte_file = 'MNIST_data/t10k-images.idx3-ubyte'
# # 测试集标签文件
# test_labels_idx1_ubyte_file = 'MNIST_data/t10k-labels.idx1-ubyte'
#
#
# def decode_idx3_ubyte(idx3_ubyte_file):
#     """
#     解析idx3文件的通用函数
#     :param idx3_ubyte_file: idx3文件路径
#     :return: 数据集
#     """
#     # 读取二进制数据
#     bin_data = open(idx3_ubyte_file, 'rb').read()
#
#     # 解析文件头信息，依次为魔数、图片数量、每张图片高、每张图片宽
#     offset = 0
#     fmt_header = '>iiii'  # 因为数据结构中前4行的数据类型都是32位整型，所以采用i格式，但我们需要读取前4行数据，所以需要4个i。我们后面会看到标签集中，只使用2个ii。
#     magic_number, num_images, num_rows, num_cols = struct.unpack_from(fmt_header, bin_data, offset)
#     print('魔数:%d, 图片数量: %d张, 图片大小: %d*%d' % (magic_number, num_images, num_rows, num_cols))
#
#     # 解析数据集
#     image_size = num_rows * num_cols
#     offset += struct.calcsize(fmt_header)  # 获得数据在缓存中的指针位置，从前面介绍的数据结构可以看出，读取了前4行之后，指针位置（即偏移位置offset）指向0016。
#     print(offset)
#     fmt_image = '>' + str(
#         image_size) + 'B'  # 图像数据像素值的类型为unsigned char型，对应的format格式为B。这里还有加上图像大小784，是为了读取784个B格式数据，如果没有则只会读取一个值（即一副图像中的一个像素值）
#     print(fmt_image, offset, struct.calcsize(fmt_image))
#     images = np.empty((num_images, num_rows, num_cols))
#     # plt.figure()
#     for i in range(num_images):
#         if (i + 1) % 10000 == 0:
#             print('已解析 %d' % (i + 1) + '张')
#             print(offset)
#         images[i] = np.array(struct.unpack_from(fmt_image, bin_data, offset)).reshape((num_rows, num_cols))
#         # print(images[i])
#         offset += struct.calcsize(fmt_image)
#     #        plt.imshow(images[i],'gray')
#     #        plt.pause(0.00001)
#     #        plt.show()
#     # plt.show()
#
#     return images
#
#
# def decode_idx1_ubyte(idx1_ubyte_file):
#     """
#     解析idx1文件的通用函数
#     :param idx1_ubyte_file: idx1文件路径
#     :return: 数据集
#     """
#     # 读取二进制数据
#     bin_data = open(idx1_ubyte_file, 'rb').read()
#
#     # 解析文件头信息，依次为魔数和标签数
#     offset = 0
#     fmt_header = '>ii'
#     magic_number, num_images = struct.unpack_from(fmt_header, bin_data, offset)
#     print('魔数:%d, 图片数量: %d张' % (magic_number, num_images))
#
#     # 解析数据集
#     offset += struct.calcsize(fmt_header)
#     fmt_image = '>B'
#     labels = np.empty(num_images)
#     for i in range(num_images):
#         if (i + 1) % 10000 == 0:
#             print('已解析 %d' % (i + 1) + '张')
#         labels[i] = struct.unpack_from(fmt_image, bin_data, offset)[0]
#         offset += struct.calcsize(fmt_image)
#     return labels
#
#
# def load_train_images(idx_ubyte_file=train_images_idx3_ubyte_file):
#     """
#     TRAINING SET IMAGE FILE (train-images-idx3-ubyte):
#     [offset] [type]          [value]          [description]
#     0000     32 bit integer  0x00000803(2051) magic number
#     0004     32 bit integer  60000            number of images
#     0008     32 bit integer  28               number of rows
#     0012     32 bit integer  28               number of columns
#     0016     unsigned byte   ??               pixel
#     0017     unsigned byte   ??               pixel
#     ........
#     xxxx     unsigned byte   ??               pixel
#     Pixels are organized row-wise. Pixel values are 0 to 255. 0 means background (white), 255 means foreground (black).
#
#     :param idx_ubyte_file: idx文件路径
#     :return: n*row*col维np.array对象，n为图片数量
#     """
#     return decode_idx3_ubyte(idx_ubyte_file)
#
#
# def load_train_labels(idx_ubyte_file=train_labels_idx1_ubyte_file):
#     """
#     TRAINING SET LABEL FILE (train-labels-idx1-ubyte):
#     [offset] [type]          [value]          [description]
#     0000     32 bit integer  0x00000801(2049) magic number (MSB first)
#     0004     32 bit integer  60000            number of items
#     0008     unsigned byte   ??               label
#     0009     unsigned byte   ??               label
#     ........
#     xxxx     unsigned byte   ??               label
#     The labels values are 0 to 9.
#
#     :param idx_ubyte_file: idx文件路径
#     :return: n*1维np.array对象，n为图片数量
#     """
#     return decode_idx1_ubyte(idx_ubyte_file)
#
#
# def load_test_images(idx_ubyte_file=test_images_idx3_ubyte_file):
#     """
#     TEST SET IMAGE FILE (t10k-images-idx3-ubyte):
#     [offset] [type]          [value]          [description]
#     0000     32 bit integer  0x00000803(2051) magic number
#     0004     32 bit integer  10000            number of images
#     0008     32 bit integer  28               number of rows
#     0012     32 bit integer  28               number of columns
#     0016     unsigned byte   ??               pixel
#     0017     unsigned byte   ??               pixel
#     ........
#     xxxx     unsigned byte   ??               pixel
#     Pixels are organized row-wise. Pixel values are 0 to 255. 0 means background (white), 255 means foreground (black).
#
#     :param idx_ubyte_file: idx文件路径
#     :return: n*row*col维np.array对象，n为图片数量
#     """
#     return decode_idx3_ubyte(idx_ubyte_file)
#
#
# def load_test_labels(idx_ubyte_file=test_labels_idx1_ubyte_file):
#     """
#     TEST SET LABEL FILE (t10k-labels-idx1-ubyte):
#     [offset] [type]          [value]          [description]
#     0000     32 bit integer  0x00000801(2049) magic number (MSB first)
#     0004     32 bit integer  10000            number of items
#     0008     unsigned byte   ??               label
#     0009     unsigned byte   ??               label
#     ........
#     xxxx     unsigned byte   ??               label
#     The labels values are 0 to 9.
#
#     :param idx_ubyte_file: idx文件路径
#     :return: n*1维np.array对象，n为图片数量
#     """
#     return decode_idx1_ubyte(idx_ubyte_file)
