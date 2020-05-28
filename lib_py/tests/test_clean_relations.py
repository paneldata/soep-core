import unittest
from pathlib import Path
from tempfile import mkdtemp
from shutil import copytree, rmtree

from ..clean_relations import VariableGraph


class TestVariableGraph(unittest.TestCase):
    def setUp(self):
        self.tmpdir_path = Path(mkdtemp())
        test_data = Path("./test_data")
        copytree(test_data, self.tmpdir_path.joinpath("metadata"))

        return super().setUp()

    def tearDown(self):
        rmtree(self.tmpdir_path)
        return super().tearDown()
