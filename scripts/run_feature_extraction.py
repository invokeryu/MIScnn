import json
import os

from pyradiomics_feature import Pyradiomics_feature

extractor = Pyradiomics_feature("param.yaml")

if not os.path.exists("./features"):
    os.makedirs("./features")

for patient_idx in os.listdir("./data"):
    img = os.path.join("./data", patient_idx, "imaging.nii.gz")
    mask = os.path.join("predictions", f"{patient_idx}.nii.gz")
    result = extractor.catch_features(img, mask)

