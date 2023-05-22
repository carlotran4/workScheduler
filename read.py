import csv
from datetime import datetime


class Shift:
    def __init__(self, start: datetime, end: datetime) -> None:
        start_time = start
        end_time = end

def get_shifts(schedule_path: str) -> list[Shift]:
    