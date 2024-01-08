import unittest

import sys
sys.path.insert(0, '../tests')

from model import IrisModel, IrisSpecies


class TestIrisModel(unittest.TestCase):
   def test_model_initialization(self):
       new_model = IrisModel()
       self.assertIn('iris_model.joblib',new_model.model_fname_)
