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
        self._graph = networkx.Graph()
        self._filled = False

    @property
    def graph(self):
        return self._graph.copy()

    @property
    def filled(self):
        return self._filled

    def fill(self):
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
        self._filled = True
