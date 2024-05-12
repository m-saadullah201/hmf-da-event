from pydantic import BaseModel
from enum import Enum


class RunMode(Enum):
    data = 0
    test = 1
    full = 2


class ApplicationSettings(BaseModel):
    run_mode: RunMode
    sample_size: int = 0
    database_block: bool
    limit_sample_size: bool


class DataReaderSettings(BaseModel):
    read_sample_size: int = 0
