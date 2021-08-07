# EMNIST���ݼ��ļ�����
1. ���ݼ��������ܣ�EMNIST�Ƕ�MNIST����չ��������ҪΪ��д��ĸ�����֣���Ϊ����6�ࣺ

    + By_Class �� �� 814255 �ţ�62 �࣬����������ĸ�����֣��� NIST ������»�����ѵ��������Ի���ͼƬ��
    + By_Merge�� �� 814255 �ţ�47 �࣬ɾ����һЩ���׻�������ĸ���֣� �� NIST ������»�����ѵ��������Ի���ͼƬ��
    + Balanced : �� 131600 �ţ�47 �࣬ɾ����һЩ���׻�������ĸ���֣� ÿһ�඼��������ͬ�����ݣ�ÿһ��ѵ���� 2400 �ţ����Լ� 400 ��
    + Digits ���� 28000 �ţ�10 �࣬�����������֣�ÿһ�������ͬ�������ݣ�ÿһ��ѵ���� 24000 �ţ����Լ� 4000 ��
    + Letters : �� 145600 �ţ�26 �࣬����������ĸ��ÿһ�������ͬ���ݣ�ÿһ��ѵ����5600 �ţ����Լ� 800 ��
    + MNIST �� �� 70000 �ţ�10 �࣬�����������֣�ÿһ�������ͬ�������ݣ�ע��������Ȼ��Ŀ�ͷ��඼һ��������ͼƬ�Ĵ���ʽ��һ����EMNIST �� MNIST �Ӽ�����ռ�ı��ظ���
    
    **��������0-9��Ӧ��ǩΪ0-9, ��ĸA-Z��Ӧ��ǩΪ10-35, ��ĸa-z��Ӧ��ǩΪ36-61.**
2. ʹ�÷���
```
    """ �÷�ʾ�� """

    # �˴���д���ݼ����ϼ�Ŀ¼
    root = 'E:\MindsporeVision\dataset\emnist'

    # ʵ����
    dataset = _EMNIST(root=root, is_train=False)

    # ����һЩ��������shuffle��num_parallel_workers�ȵ�
    dataset = ds.GeneratorDataset(dataset,
                                  column_names=["image", "label"],
                                  num_parallel_workers=1,
                                  num_samples=None,
                                  shuffle=False)

    # ��һЩ������ǿ���������Ҫ��ǿ���԰���δ���ע�͵�
    # ���Ȱ����ݼ�����Ϊuint8����Ϊmapֻ֧��uint8
    dataset = dataset.map(operations=ctrans.TypeCast(mstype.uint8), input_columns="image")
    # �˴���д����Ҫ��������ǿ����
    transform = [cvision.Resize(36), cvision.RandomCrop(28)]
    dataset = dataset.map(operations=transform, input_columns="image")

    # ��ʾ10��ͼƬ
    for index, data in enumerate(dataset.create_dict_iterator(output_numpy=True)):
        if index >= 10:
            break
        print(data["image"].shape, data["label"])
        plt.subplot(2, 5, index + 1)
        plt.imshow(data["image"].squeeze(), cmap=plt.cm.gray)
        plt.title(data["label"])
    plt.show()
```
���ݼ���Ŀ¼�ṹ������ʾ�����Ŀ¼�ṹ�����治һ�����ű����޷���ȷ���У���
```
    emnist /
        emnist - mnist - train - labels - idx1 - ubyte.gz
        emnist - mnist - train - images - idx3 - ubyte.gz
        emnist - mnist - test - labels - idx1 - ubyte.gz
        emnist - mnist - test - images - idx3 - ubyte.gz
        emnist - mnist - mapping.txt
        emnist - letters - train - labels - idx1 - ubyte.gz
        emnist - letters - train - images - idx3 - ubyte.gz
        emnist - letters - test - labels - idx1 - ubyte.gz
        emnist - letters - test - images - idx3 - ubyte.gz
        emnist - letters - mapping.txt
        emnist - digits - train - labels - idx1 - ubyte.gz
        emnist - digits - train - images - idx3 - ubyte.gz
        emnist - digits - test - labels - idx1 - ubyte.gz
        emnist - digits - test - images - idx3 - ubyte.gz
        emnist - digits - mapping.txt
        emnist - balanced - mapping.txt
        emnist - balanced - test - images - idx3 - ubyte.gz
        emnist - balanced - test - labels - idx1 - ubyte.gz
        emnist - balanced - train - images - idx3 - ubyte.gz
        emnist - byclass - test - images - idx3 - ubyte.gz
        emnist - byclass - train - images - idx3 - ubyte.gz
        emnist - byclass - train - labels - idx1 - ubyte.gz
        emnist - bymerge - test - images - idx3 - ubyte.gz
        emnist - bymerge - train - images - idx3 - ubyte.gz
        emnist - bymerge - train - labels - idx1 - ubyte.gz
        emnist - bymerge - test - labels - idx1 - ubyte.gz
        emnist - bymerge - mapping.txt
        emnist - byclass - test - labels - idx1 - ubyte.gz
        emnist - byclass - mapping.txt
        emnist - balanced - train - labels - idx1 - ubyte.gz
```
3. ���ݴ洢���½ṹ������ʾ��
```
TRAINING SET LABEL FILE (train-labels-idx1-ubyte):
[offset] [type]          [value]          [description]
0000     32 bit integer  0x00000801(2049) magic number (MSB first)
0004     32 bit integer  60000            number of items
0008     unsigned byte   ??               label
0009     unsigned byte   ??               label
........
xxxx     unsigned byte   ??               label
The labels values are 0 to 9.

TRAINING SET IMAGE FILE (train-images-idx3-ubyte):
[offset] [type]          [value]          [description]
0000     32 bit integer  0x00000803(2051) magic number
0004     32 bit integer  60000            number of images
0008     32 bit integer  28               number of rows
0012     32 bit integer  28               number of columns
0016     unsigned byte   ??               pixel
0017     unsigned byte   ??               pixel
........
xxxx     unsigned byte   ??               pixel
```

���ڴ����ݼ�����ϸ��Ϣ��ο���[����](https://blog.csdn.net/Chris_zhangrx/article/details/86516331).