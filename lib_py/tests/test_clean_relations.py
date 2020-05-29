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
        self.generations = pandas.read_csv(
            self.tmp_project_path.joinpath("metadata/generations.csv")
        )
        self.variables = pandas.read_csv(
            self.tmp_project_path.joinpath("metadata/variables.csv")
        )

        return super().setUp()

    def tearDown(self):
        rmtree(self.tmpdir_path)
        return super().tearDown()

    def assertIsInGraph(self, node, graph: Graph):
        """Assertion to test presence of a node in a networkx graph"""
        self.assertTrue(
            graph.has_node(node), msg=f"Node {node} is not in Graph",
        )

    def test_graph_instance(self):
        graph = VariableGraph(self.generations, self.variables)
        self.assertIsInstance(graph, VariableGraph)
        self.assertIs(self.generations, graph._generations)
        self.assertIs(self.variables, graph._variables)
        self.assertIsInstance(graph.graph, Graph)
        self.assertFalse(graph.filled)

    def test_filled_graph(self):
        graph = VariableGraph(self.generations, self.variables)
        graph.fill()
        self.assertTrue(graph.filled)
        expected_node = (
            self.generations["input_study"][0],
            self.generations["input_dataset"][0],
            self.generations["input_version"][0],
            self.generations["input_variable"][0],
        )
        excepted_related_node = (
            self.generations["output_study"][0],
            self.generations["output_dataset"][0],
            self.generations["output_version"][0],
            self.generations["output_variable"][0],
        )
        networkx_graph: Graph = graph.graph
        self.assertIsInGraph(expected_node, networkx_graph)
        self.assertTrue(
            networkx_graph.has_edge(expected_node, excepted_related_node),
            msg=f"Edge from {expected_node} to {excepted_related_node} is not in graph.",
        )
