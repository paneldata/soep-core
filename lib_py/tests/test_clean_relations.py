import unittest
from pathlib import Path
from shutil import copytree, rmtree
from tempfile import mkdtemp
from typing import Tuple

import pandas
from networkx import DiGraph

from ..clean_relations import VariableGraph, QuestionsVariablesGraph


class GraphTestCase(unittest.TestCase):
    def setUp(self):
        self.tmpdir_path = Path(mkdtemp())
        self.tmp_project_path = self.tmpdir_path.joinpath("test-study")
        test_data = Path("lib_py/test_data/")
        copytree(test_data, self.tmp_project_path)

    def tearDown(self):
        rmtree(self.tmpdir_path)
        return super().tearDown()

    def assertIsInGraph(self, node: Tuple[str], graph: DiGraph):
        """Assertion to test presence of a node in a networkx graph.
        
        Args:
            node: Node to test existence for.
            graph: Node must exist in this graph.

        """
        self.assertTrue(
            graph.has_node(node), msg=f"Node {node} is not in Graph",
        )

    def assertHasEdge(self, from_node: Tuple[str], to_node: Tuple[str], graph: DiGraph):
        """Assertion to test presence of an edge in a networkx graph
        
        Args:
            from_node: Node from wich the edge must originate.
            to_node: Node to which the edge must point.
            graph: Graph in which this relation must exist.
        """

        self.assertTrue(
            graph.has_edge(from_node, to_node),
            msg=f"Edge from {from_node} to {to_node} is not in graph.",
        )


class TestVariableGraph(GraphTestCase):
    def setUp(self):
        super().setUp()
        self.generations = pandas.read_csv(
            self.tmp_project_path.joinpath("metadata/generations.csv")
        )
        _variables = pandas.read_csv(
            self.tmp_project_path.joinpath("metadata/variables.csv")
        )
        self.variables = {
            (row["study"], row["dataset"], row.get("name", row.get("variable")))
            for _, row in _variables.iterrows()
        }

        return super().setUp()

    def test_graph_instance(self):
        graph = VariableGraph(self.generations, self.variables)
        self.assertIsInstance(graph, VariableGraph)
        self.assertIs(self.generations, graph._generations)
        self.assertIs(self.variables, graph._variables)
        self.assertIsInstance(graph.graph, DiGraph)
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
        expected_transitive_node = (
            self.generations["output_study"][1],
            self.generations["output_dataset"][1],
            self.generations["output_version"][1],
            self.generations["output_variable"][1],
        )

        networkx_graph: Graph = graph.graph
        self.assertIsInGraph(expected_node, networkx_graph)
        self.assertHasEdge(expected_node, excepted_related_node, networkx_graph)
        self.assertHasEdge(expected_node, excepted_related_node, networkx_graph)
        self.assertHasEdge(expected_node, expected_transitive_node, networkx_graph)

    def test_get_transformations(self):
        graph = VariableGraph(self.generations, self.variables)
        version = self.generations["input_version"][1]

        transformations = graph.get_transformations(version=version)
        self.assertListEqual(
            [
                "origin_study_name",
                "origin_dataset_name",
                "origin_variable_name",
                "target_study_name",
                "target_dataset_name",
                "target_variable_name",
            ],
            list(transformations.columns.values),
        )
        self.assertListEqual(
            [
                "some-study",
                "some-dataset",
                "some-other-variable",
                "some-study",
                "some-dataset",
                "final-variable",
            ],
            [
                transformations["origin_study_name"][0],
                transformations["origin_dataset_name"][0],
                transformations["origin_variable_name"][0],
                transformations["target_study_name"][0],
                transformations["target_dataset_name"][0],
                transformations["target_variable_name"][0],
            ],
        )
        self.assertNotIn(
            "some-irrelevant-variable", transformations["origin_variable_name"]
        )


class TestQuestionsVariablesGraph(GraphTestCase):
    def setUp(self):
        super().setUp()
        self.logical_variables = pandas.read_csv(
            self.tmp_project_path.joinpath("metadata/logical_variables.csv")
        )

        return super().setUp()

    def test_questions_variables_graph_instance(self):
        graph = QuestionsVariablesGraph(
            question_to_variable_relations=self.logical_variables
        ).graph
        self.assertIsInstance(graph, DiGraph)
        question = (
            self.logical_variables["study"][0],
            self.logical_variables["questionnaire"][0],
            self.logical_variables["question"][0],
            self.logical_variables["item"][0],
        )
        variable = (
            self.logical_variables["study"][0],
            self.logical_variables["dataset"][0],
            self.logical_variables["variable"][0],
        )
        self.assertIsInGraph(question, graph)
        self.assertIsInGraph(variable, graph)
        self.assertHasEdge(question, variable, graph)


class TestGraphAddition(GraphTestCase):
    def setUp(self):
        super().setUp()
        self.logical_variables = pandas.read_csv(
            self.tmp_project_path.joinpath("metadata/logical_variables.csv")
        )
        self.generations = pandas.read_csv(
            self.tmp_project_path.joinpath("metadata/generations.csv")
        )
        _variables = pandas.read_csv(
            self.tmp_project_path.joinpath("metadata/variables.csv")
        )
        self.variables = {
            (row["study"], row["dataset"], row.get("name", row.get("variable")))
            for _, row in _variables.iterrows()
        }
        self.variables_graph = VariableGraph(self.generations, self.variables)
        self.questions_variables_graph = QuestionsVariablesGraph(self.logical_variables)
        self.variables_graph.fill()
        self.questions_variables_graph.fill()

    def test_addition(self):
        combined_graph = self.variables_graph + self.questions_variables_graph
        self.assertIsInstance(combined_graph, DiGraph)
        combined_graph = self.questions_variables_graph + self.variables_graph