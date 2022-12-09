import glob
import os
from typing import Dict, List

import pandas as pd
from src.utils import ROOT_DIR

METADATA_PATH = os.path.join(ROOT_DIR, 'data/mimic-cxr/mimic-cxr-2.0.0-metadata.csv')
SPLIT_PATH = os.path.join(ROOT_DIR, 'data/mimic-cxr/mimic-cxr-2.0.0-split.csv')
CHEXPERT_PATH = os.path.join(ROOT_DIR, 'data/chexpert/mimic-cxr-2.0.0-chexpert.csv')
NEGIBOX_PATH = os.path.join(ROOT_DIR, 'data/negibox/mimic-cxr-2.0.0-negibox.csv')


def _create_id_path_dict() -> Dict[str, str]:
    df_split = pd.read_csv(SPLIT_PATH)
    paths = _create_list_of_all_paths_jpg_files('data/mimic-cxr/files')
    return {
        id: path
        for id in df_split['dicom_id'].values for path in paths
        if id in path
        }


def _create_list_of_all_paths_jpg_files(path: str) -> List[str]:
    all_jpgs = glob.glob(os.path.join(ROOT_DIR, f'{path}/**/*.jpg'), recursive=True)
    return [j.replace('\\', '/') for j in all_jpgs]


print(_create_id_path_dict())