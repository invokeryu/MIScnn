import os.path

from radiomics import featureextractor
import six
import json


class Pyradiomics_feature:
    def __init__(self, config_path):
        self.config_path = config_path
        self.extractor = featureextractor.RadiomicsFeatureExtractor(config_path)
        self.cache_features_path = "./predictions"
        print('Extraction parameters:\n\t', self.extractor.settings)
        print('Enabled filters:\n\t', self.extractor.enabledImagetypes)
        print('Enabled features:\n\t', self.extractor.enabledFeatures)

    def catch_features(self, img_path = None, mask_path = None):
        assert img_path is not None and mask_path is not None, "img_path and mask_path is required"
        result = self.extractor.execute(img_path, mask_path)
        print('Result type:', type(result))  # result is returned in a Python ordered dictionary)
        print('')
        print('Calculated features')
        for k, v in six.iteritems(result):
            print('\t', k, ':', v)
        return result