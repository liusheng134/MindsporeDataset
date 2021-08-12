# DIV2K ���ݼ�����

1. DIV2K ���ݼ�
DIV2K���ݼ���һ���·���������ͼ��ԭ����ĸ�������2K�ֱ��ʣ�ͼ�����ݼ����˴��������ݼ����ڳ��ֱ�����
DIV2K���ݼ�����800��ѵ��ͼ��100����֤ͼ���100�Ų���ͼ����NTIRE�����к�Set5��Set14��һ����Ϊ��׼���ݼ���

2. ʹ�÷���
```
    """ �÷�ʾ�� """

    # ��д���ݼ����ϼ�Ŀ¼
    root = r'E:\MindsporeVision\dataset\DIV2K'

    # ʵ������ע��ͼƬΪHWC��BGR��ʽ������ѵ��ʱ��Ҫת��ΪCHW��RGB��ʽ
    dataset = DIV2K(root, is_train=True, scale=2)

    # ����һЩ��������shuffle��num_parallel_workers�ȵ�
    dataset = ds.GeneratorDataset(dataset,
                                  column_names=["image", "label"],
                                  num_parallel_workers=1,
                                  num_samples=None,
                                  shuffle=False)

    # ��һЩ������ǿ���������Ҫ��ǿ���԰���δ���ע�͵�
    # ���Ȱ����ݼ�����Ϊuint8����Ϊmapֻ֧��uint8
    dataset = dataset.map(operations=ctrans.TypeCast(mstype.uint8), input_columns="image")
    dataset = dataset.map(operations=ctrans.TypeCast(mstype.uint8), input_columns="label")

    # �˴���д����Ҫ��������ǿ����
    transform = [cvision.Resize(448),
                 cvision.RandomCrop(448)]
    dataset = dataset.map(operations=transform, input_columns="image")
    dataset = dataset.map(operations=transform, input_columns="label")

    # ��ʾһ��ͼƬ
    for index, data in enumerate(dataset.create_dict_iterator(output_numpy=True)):
        if index>5:
            break
        if index != 5:
            continue

        # print(index)
        print(data["image"].shape, data["label"].shape)
        plt.subplot(2, 1, 1)
        plt.imshow(data["image"].squeeze())
        plt.title("data")

        plt.subplot(2, 1, 2)
        plt.imshow(data["label"].squeeze())
        plt.title("label")
    plt.show()
```

3. ���ݼ�Ŀ¼�ṹ�����Ŀ¼�ṹ�����治һ�����ű����޷���ȷ���У�
```
DIV2K/
    DIV2K_valid_HR
    DIV2K_train_HR
```

4. ���ڸ����ݼ�����ϸ��Ϣ����ο���https://data.vision.ee.ethz.ch/cvl/DIV2K/
