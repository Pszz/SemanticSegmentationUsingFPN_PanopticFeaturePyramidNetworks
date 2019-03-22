class Path(object):
    @staticmethod
    def db_root_dir(dataset):
        if dataset == 'pascal':
            # folder that contains VOCdevkit/.
            return '/path/to/datasets/VOCdevkit/VOC2012/'
        elif dataset == 'sbd':
            # folder that contains dataset/.
            return '/path/to/datasets/benchmark_RELEASE/'
        elif dataset == 'cityscapes':
            # foler that contains leftImg8bit/
            return 'D:\\Disk\\MidTerm\\Experiment\\Code\\Semantic\\FPN\\FPN\\data\\Cityscapes'
        elif dataset == 'coco':
            return '/path/to/datasets/coco/'
        elif dataset == 'CamVid':
            return 'D:\\Disk\\MidTerm\\Experiment\\Code\\Semantic\\FPN\\FPN\\data\\CamVid'
        elif dataset == 'nyudv2':
            return 'D:\\Disk\\MidTerm\\Experiment\\Code\\Semantic\\FPN\\FPN\\data\\NYUDv2'
        else:
            print('Dataset {} not available.'.format(dataset))
            raise NotImplementedError("undefined dataset {}.".format(dataset))
