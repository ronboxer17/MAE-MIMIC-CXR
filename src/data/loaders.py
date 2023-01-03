import glob
import os
import shutil
from typing import Dict, List

import pandas as pd
from src.config import ROOT_DIR, METADATA_PATH, SPLIT_PATH, CHEXPERT_PATH, NEGIBOX_PATH


def _create_id_path_dict(folder_path: str = 'data/mimic-cxr/files') -> Dict[str, str]:
    df_split = pd.read_csv(SPLIT_PATH)
    paths = _create_list_of_all_paths_jpg_files(folder_path)
    return {
        id: path
        for id in df_split['dicom_id'].values for path in paths
        if id in path
    }


def _create_list_of_all_paths_jpg_files(path: str) -> List[str]:
    all_jpgs = glob.glob(os.path.join(ROOT_DIR, f'{path}/**/*.jpg'), recursive=True)
    return [j.replace('\\', '/') for j in all_jpgs]


def create_data_folder_for_model(ids: List[str], type=None, label=None) -> None:
    assert type in ('train', 'val', 'test'), f'{type} not one of [train, val, test]'

    ids_paths = {k: v for k, v in _create_id_path_dict().items() if k in ids}

    if type == 'test':
        folder_path = os.path.join(ROOT_DIR, 'data', type)  # TODO: change the folder_path according to our needs
    else:
        folder_path = os.path.join(ROOT_DIR, 'data', type, label)

    os.makedirs(folder_path, exist_ok=True)
    for id, source_path in ids_paths.items():
        output_path = os.path.join(folder_path, os.path.basename(source_path))
        if not os.path.isfile(output_path):
            shutil.copy(
                source_path,
                output_path
            )


if __name__ == '__main__':
    d = _create_id_path_dict()
    print(d.keys())
    create_data_folder_for_model(['02aa804e-bde0afdd-112c0b34-7bc16630-4e384014'], type='train', label=str(1))