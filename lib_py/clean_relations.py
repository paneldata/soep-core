"""Create cleaned up relational files

There are two files that define relationships beetween variables and 
between variables and questions.

* generations.csv defines relationships beetween variables
* logical_variables.csv defines relationships between questions and variables 

These relationships are not "clean", they contain relationships with entities
that are not part of the actual data.
The unclean relations are needed to establish the relationship between questions
and variables. 
The relationships are transitive.
Before we can throw away old relationships, we have to create the transitive closure
for all relations.
Otherwise we would loose relationships when we remove relationships to old variables.
"""


import networkx
import pandas


class VariableGraph:
    def __init__(self, generations: pandas.DataFrame, variables: pandas.DataFrame):
        self._generations = generations
        self._variables = variables
        self._graph = networkx.DiGraph()
        self._filled = False

    @property
    def graph(self) -> networkx.DiGraph:
        return self._graph.copy()

    @property
    def filled(self):
        return self._filled

    def fill(self):
        if self.filled:
            return
        for _, row in self._generations.iterrows():
            input_node = (
                row["input_study"],
                row["input_dataset"],
                row["input_version"],
                row["input_variable"],
            )
            output_node = (
                row["output_study"],
                row["output_dataset"],
                row["output_version"],
                row["output_variable"],
            )
            self._graph.add_edge(input_node, output_node)
        self._graph = networkx.algorithms.dag.transitive_closure(self._graph)
        self._filled = True

    def get_transformations(self, version):
        if not self.filled:
            self.fill()
        transformations = pandas.DataFrame(
            columns=[
                "origin_study_name",
                "origin_dataset_name",
                "origin_variable_name",
                "target_study_name",
                "target_dataset_name",
                "target_variable_name",
            ]
        )

        for node in self._graph.nodes(data=False):
            if node[2] != version:
                continue
            for related_node in self._graph.neighbors(node):
                if related_node[2] != version:
                    continue
                transformations = transformations.append(
                    pandas.Series(
                        self._create_transformations_row(node, related_node),
                        index=transformations.columns,
                    ),
                    ignore_index=True,
                )

        return transformations

    @classmethod
    def _create_transformations_row(cls, origin, target):
        return cls._remove_version(origin) + cls._remove_version(target)

    @staticmethod
    def _remove_version(node):
        return node[0:2] + node[3:]
