# Fashion-mnist���ݼ�����

1. ���ݼ��������ܣ�FashionMNIST ��һ����� MNIST ��д���ּ���ͼ�����ݼ���
�亭�������� 10 �����Ĺ� 7 �����ͬ��Ʒ������ͼƬ��FashionMNIST �Ĵ�С��
��ʽ��ѵ����/���Լ�������ԭʼ�� MNIST ��ȫһ�¡�60000/10000 ��ѵ����������
���֣�28x28 �ĻҶ�ͼƬ�������ֱ��������������Ļ���ѧϰ�����ѧϰ�㷨���ܣ�
�Ҳ���Ҫ�Ķ��κεĴ��롣
���ݼ�Ԥ��������ʾ��

![Fashion-mnistԤ��](img/fashion-mnist.png)

���ݼ��ļ�������ʾ��

| Name | Content | Examples | Size | Link | MD5 Checksum|
| --- | --- |--- | --- |--- |--- |
| `train-images-idx3-ubyte.gz`  | ѵ����ͼƬ  | 60,000|26 MBytes | [Download](http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/train-images-idx3-ubyte.gz)|`8d4fb7e6c68d591d4c3dfef9ec88bf0d`|
| `train-labels-idx1-ubyte.gz`  | ѵ������ǩ  |60,000|29 KBytes | [Download](http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/train-labels-idx1-ubyte.gz)|`25c81989df183df01b3e8a0aad5dffbe`|
| `t10k-images-idx3-ubyte.gz`  | ���Լ�ͼƬ  | 10,000|4.3 MBytes | [Download](http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/t10k-images-idx3-ubyte.gz)|`bef4ecab320f06d8554ea6380940ec79`|
| `t10k-labels-idx1-ubyte.gz`  | ���Լ���ǩ  | 10,000| 5.1 KBytes | [Download](http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/t10k-labels-idx1-ubyte.gz)|`bb300cfdad3c16e7a12a480ee83cd310`|

2. ʹ�÷���
```
    """ �÷�ʾ�� """

    # ��д���ݼ����ϼ�Ŀ¼
    root = r'E:\MindsporeVision\dataset\fashion-mnist'

    # ʵ����
    # ע�⣺����ͼƬΪHWC��ʽ����Ϊmapֻ֧��HWC������ͼƬ����Ϊuint8����0-255��
    fashion_mnist = _FashionMNIST(root, is_train=True)

    # ����һЩ��������shuffle��num_parallel_workers�ȵ�
    dataset = ds.GeneratorDataset(fashion_mnist,
                                  column_names=["image", "label"],
                                  num_parallel_workers=1,
                                  shuffle=False,
                                  sampler=None)

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

3. ���ݼ�Ŀ¼�ṹ�����Ŀ¼�ṹ�����治һ�����ű����޷���ȷ���У�
```
fashion-mnist/
    t10k-labels-idx1-ubyte
    train-labels-idx1-ubyte
    train-images-idx3-ubyte
    t10k-images-idx3-ubyte
```


