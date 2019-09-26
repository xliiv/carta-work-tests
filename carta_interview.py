
import os
from enum import Enum


class Datasets(Enum):
	SUPPLY_USAGE = "hospital-supply-usage.csv"
	PRICING = "pricing.csv"
	PATIENT_EXTRACT1 = "patients-extract1.xlsx"
	PATIENT_EXTRACT2 = "patients-extract2.xlsx"


def get_data_dir():
	return os.path.join(os.path.abspath(os.path.dirname(__file__)), "data")


def get_data_file(dataset):
	return os.path.join(get_data_dir(), dataset.value)
