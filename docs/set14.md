# Set14 ���ݼ�����

1. Set14���ݼ���Google�о�ԱRoman Zeyde����������ڳ��ֱ�����о��������ݼ�һ������14��ͼ��һ����Ϊ����ģ�͵Ĳ���ָ�꣨һ��ʹ��PSNR/SSIM��������һ��ͼ������ͼ��ʾ��

![Set14.png](img/set14.png)

2. ʹ�÷���
```
    """ �÷�ʾ�� """

    # ��д���ݼ����ϼ�Ŀ¼
    root = r'E:\MindsporeVision\dataset\Set14'

    # ʵ����
    dataset = Set14(root, scale=2, is_train=False)

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
    # transform = [cvision.Resize(128),
    #              cvision.RandomCrop(128)]
    # dataset = dataset.map(operations=transform, input_columns="image")
    # dataset = dataset.map(operations=transform, input_columns="label")

    # ��ʾǰ5��ͼƬ(������ݼ�ֻ��14��ͼ)
    for index, data in enumerate(dataset.create_dict_iterator(output_numpy=True)):
        if index >= 5:
            break
        print(index)
        print(data["image"].shape, data["label"].shape)
        plt.subplot(2, 5, index+1)
        plt.imshow(data["image"].squeeze())
        plt.title("data")

        plt.subplot(2, 5, index +1+ 5)
        plt.imshow(data["label"].squeeze())
        plt.title("label")
    plt.show()
```

3. ���ݼ�Ŀ¼�ṹ�����Ŀ¼�ṹ�����治һ�����ű����޷���ȷ���У�
```
Set14/
    image_SRF_4
    image_SRF_3
    image_SRF_2
```

4. ���ڸ����ݼ�����ϸ��Ϣ����ο���https://sites.google.com/site/romanzeyde/research-interests
