import click

from datapackage import Package
from tableschema.exceptions import RelationError

STUDY = "soep-core"
VERSION = "v33"

package = Package("metadata/datapackage.json")


@click.command()
@click.argument("entity")
def validate_entity(entity):
    resource = package.get_resource(entity)
    resource.check_relations()


if __name__ == "__main__":
    validate_entity()
