# KMNIST���ݼ��ļ�����
1. ���ݼ��������ܣ�KMNIST�� MNIST ���ݼ���28x28 �Ҷȣ�70,000 ��ͼ�񣩵����Ʒ��
��ԭʼ MNIST ��ʽ�� NumPy ��ʽ�ṩ������ MNIST ����������Ϊ 10 ���࣬���������
���� KMNIST ʱѡ����һ���ַ������� 10 ��ƽ�����е�ÿһ�С����ݼ�Ԥ��������ʾ��

[KMNISTԤ��](img/kmnist.png)
<center>KMNIST �� 10 ����𣬵�һ����ʾÿ����ɫ���ִ�ƽ������Ӧ��</center>

2. ʹ�÷���
```
    """ �÷�ʾ�� """

    # ��д���ݼ����ϼ�Ŀ¼
    root = r'E:\MindsporeVision\dataset\kmnist'

    # ʵ����
    dataset = KMNIST(root=root, is_train=False)

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
    transform = [cvision.Resize(28), cvision.RandomCrop(28)]
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
3. ���ݼ���Ŀ¼�ṹ������ʾ�����Ŀ¼�ṹ�����治һ�����ű����޷���ȷ���У���
```
kmnist/
    t10k-images-idx3-ubyte
    t10k-labels-idx1-ubyte
    train-images-idx3-ubyte
    train-labels-idx1-ubyte
        
```
4. ���ݼ��洢���½ṹ������ʾ��������һ�㲻��Ҫ������

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

���ڴ����ݼ�����ϸ��Ϣ��ο�: github.com/rois-codh/kmnist