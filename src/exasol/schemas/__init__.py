from __future__ import annotations
import contextlib
import sys

from packaging.version import Version
from collections import defaultdict
import shutil
import jinja2
from typing import Type
from dataclasses import dataclass
import json_schema_for_humans as json2schema
from json_schema_for_humans import generate
from tempfile import TemporaryDirectory
from pathlib import Path
import typer

CLI = typer.Typer()


@dataclass(frozen=True)
class Schema:
    name: str
    version: str
    path: Path

    @property
    def full_name(self):
        return f"{self.name}-{self.version}"


@dataclass(frozen=True)
class Example:
    name: str
    version: str
    path: Path

    @property
    def full_name(self):
        return f"{self.name}-{self.version}-example"


def _json_files(path: Path, output_type: Type[Schema | Example]):
    files = path.glob("**/*.json")
    return (
        output_type(
            name=f.parent.name, version=Version(f.name.removesuffix(".json")), path=f
        )
        for f in files
    )


def _jinja_env() -> jinja2.Environment:
    env = jinja2.Environment(
        loader=jinja2.PackageLoader("exasol.schemas", "templates"),
        autoescape=jinja2.select_autoescape(),
    )
    return env


@CLI.command(name="generate")
def generate_static_page(
    schema_dir: Path = Path("./schemas"),
    example_dir: Path = Path("./examples"),
    output_dir: Path = Path("./gh-pages"),
):
    schemas = set(_json_files(schema_dir, output_type=Schema))
    examples = set(_json_files(example_dir, output_type=Example))

    with TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)

        # copy raw schemas
        for schema in schemas:
            src = schema.path
            dest = tmpdir / f"{schema.full_name}.json"
            shutil.copyfile(src, dest)

        # copy examples
        for example in examples:
            src = example.path
            dest = tmpdir / f"{example.full_name}.json"
            shutil.copyfile(src, dest)

        # generate & copy references
        for schema in schemas:
            reference = tmpdir / f"{schema.full_name}.html"
            with contextlib.redirect_stdout(sys.stderr):
                json2schema.generate.generate_from_filename(schema.path, f"{reference}")

        # create index file, linking references and schema
        def grouped_schemas(schemas):
            grouped = defaultdict(list)
            for schema in schemas:
                grouped[schema.name].append(schema)
            return grouped

        def grouped_examples(examples):
            grouped = defaultdict(lambda: defaultdict(None))
            for example in examples:
                group = grouped[example.name]
                group[example.version] = example
            return grouped

        s = grouped_schemas(schemas)
        e = grouped_examples(examples)
        env = _jinja_env()
        template = env.get_template("index.jinja")
        with open(tmpdir / "index.html", "w") as f:
            print(template.render(schemas=s, examples=e), file=f)

        # copy to destination
        if output_dir.exists():
            shutil.rmtree(output_dir)
        shutil.move(tmpdir, output_dir)


if __name__ == "__main__":
    CLI()
