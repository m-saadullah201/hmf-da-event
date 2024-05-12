from config import DATAREADER_SETTINGS
import random
from io import TextIOWrapper
from helpers import line_splitter, safe_block


def data_reader(file: TextIOWrapper):
    data = file.readlines()
    start = random.randint(0, len(data) // 2)
    sampler = slice(start, start + DATAREADER_SETTINGS.read_sample_size)
    sample_data = data[sampler]
    for line in sample_data:
        safe_block(line_splitter, {"line": line})
        # Up-next: database handler
