from __future__ import annotations

import contextlib
import shutil
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Type

import jinja2
import json_schema_for_humans as json2schema
import typer
from json_schema_for_humans import generate
from packaging.version import Version


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


CLI = typer.Typer()


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
        _create_schemas(schemas, output_dir=tmpdir)
        _create_examples(examples, output_dir=tmpdir)
        _create_schema_references(schemas, output_dir=tmpdir)
        _create_index_file(examples, schemas, output_dir=tmpdir)
        _copy_to_output_directory(src=tmpdir, dst=output_dir)


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


def _grouped_schemas(schemas):
    grouped = defaultdict(list)
    for schema in schemas:
        grouped[schema.name].append(schema)
    return grouped


def _grouped_examples(examples):
    grouped = defaultdict(lambda: defaultdict(None))
    for example in examples:
        group = grouped[example.name]
        group[example.version] = example
    return grouped


def _copy_to_output_directory(src, dst):
    if dst.exists():
        print(
            f"== Warning location not empty, deleting destination: {dst} ==",
            file=sys.stderr,
        )
        shutil.rmtree(dst)
    shutil.move(src, dst)


def _create_index_file(examples, schemas, output_dir):
    s = _grouped_schemas(schemas)
    e = _grouped_examples(examples)
    env = _jinja_env()
    template = env.get_template("index.jinja")
    with open(output_dir / "index.html", "w") as f:
        print(template.render(schemas=s, examples=e), file=f)


def _create_schema_references(schemas, output_dir):
    for schema in schemas:
        reference = output_dir / f"{schema.full_name}.html"
        with contextlib.redirect_stdout(sys.stderr):
            json2schema.generate.generate_from_filename(schema.path, f"{reference}")


def _create_examples(examples, output_dir):
    for example in examples:
        src = example.path
        dest = output_dir / f"{example.full_name}.json"
        shutil.copyfile(src, dest)


def _create_schemas(schemas, output_dir):
    for schema in schemas:
        src = schema.path
        dest = output_dir / f"{schema.full_name}.json"
        shutil.copyfile(src, dest)


if __name__ == "__main__":
    CLI()
