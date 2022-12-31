from pathlib import Path
import os

ROOT_DIR = Path(__file__).parent.parent  # This is your Project Root

METADATA_PATH = os.path.join(ROOT_DIR, 'data/mimic-cxr/mimic-cxr-2.0.0-metadata.csv')
SPLIT_PATH = os.path.join(ROOT_DIR, 'data/mimic-cxr/mimic-cxr-2.0.0-split.csv')
CHEXPERT_PATH = os.path.join(ROOT_DIR, 'data/mimic-cxr/mimic-cxr-2.0.0-chexpert.csv')
NEGIBOX_PATH = os.path.join(ROOT_DIR, 'data/mimic-cxr/mimic-cxr-2.0.0-negbio.csv')

