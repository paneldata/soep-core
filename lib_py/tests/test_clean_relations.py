import unittest
from pathlib import Path
from shutil import copytree, rmtree
from tempfile import mkdtemp

import pandas
from networkx import Graph

from ..clean_relations import VariableGraph


class TestVariableGraph(unittest.TestCase):
    def setUp(self):
        self.tmpdir_path = Path(mkdtemp())
        self.tmp_project_path = self.tmpdir_path.joinpath("test-study")
        test_data = Path("lib_py/test_data/")
        copytree(test_data, self.tmp_project_path)

        return super().setUp()

    def tearDown(self):
        rmtree(self.tmpdir_path)
        return super().tearDown()

    def test_graph_instance(self):
        generations = pandas.read_csv(
            self.tmp_project_path.joinpath("metadata/generations.csv")
        )
        variables = pandas.read_csv(
            self.tmp_project_path.joinpath("metadata/variables.csv")
        )
        graph = VariableGraph(generations, variables)
        self.assertIsInstance(graph, VariableGraph)
        self.assertIs(generations, graph._generations)
        self.assertIs(variables, graph._variables)
        self.assertIsInstance(graph.graph, Graph)
        self.assertFalse(graph.filled)
