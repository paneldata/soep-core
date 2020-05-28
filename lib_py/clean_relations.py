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


class VariableGraph:
    pass
