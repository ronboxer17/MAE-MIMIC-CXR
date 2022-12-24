import glob
import os
from typing import Dict, List

import pandas as pd
from src.config import ROOT_DIR, METADATA_PATH, SPLIT_PATH, CHEXPERT_PATH, NEGIBOX_PATH


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


