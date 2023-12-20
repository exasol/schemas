import shutil
from pathlib import Path
from tempfile import TemporaryDirectory

from invoke import task

ROOT = Path(__file__).parent


@task
def fmt(ctx):
    """Apply code formatter to all python files in the workspace"""
    ctx.run("ruff format", pty=True)
    ctx.run("ruff check --fix --select I001 --select I002", pty=True)


@task
def build(ctx):
    """Build the static site for the JSON schemas"""
    ctx.run(
        f"schema2html --schemas {ROOT / 'schemas'} --examples {ROOT / 'examples'} --destination {ROOT / 'gh-pages'}",
        pty=True,
    )


@task
def publish_to_test(ctx, version=None):
    """Build and publishes static website of JSON schemas to test branch"""
    repo_name = "schemas"
    repo_url = f"git@github.com:exasol/{repo_name}.git"

    version = ctx.run("git rev-parse --short HEAD", hide=True).stdout.strip()
    with TemporaryDirectory() as tmp_dir:
        tmp_dir = Path(tmp_dir)
        checkout_path = tmp_dir / repo_name
        git_dir = f"--git-dir={checkout_path / '.git'}"
        work_tree = f"--work-tree={checkout_path}/"
        ctx.run(f"git clone {repo_url} {checkout_path}")
        ctx.run(f'git {git_dir} config user.email "opensource@exasol.com"')
        ctx.run(f'git {git_dir} config user.name "PublishBot"')
        ctx.run(f"git {git_dir} {work_tree} switch --orphan gh-pages-test")
        build_dir = tmp_dir / "gh-pages"
        ctx.run(
            f"schema2html --schemas {ROOT / 'schemas'} --examples {ROOT / 'examples'} --destination {build_dir}",
            pty=True,
        )
        shutil.copytree(build_dir, checkout_path, dirs_exist_ok=True)
        ctx.run(f"git {git_dir} {work_tree} add {checkout_path}/")
        ctx.run(f'git {git_dir} commit -m "Publish version: {version}"')
        ctx.run(f"git {git_dir} push -f origin gh-pages-test")
