import argparse
from pathlib import Path

from exasol.schemas import generate_static_page


def _parse_args():
    parser = argparse.ArgumentParser(prog="python -m exasol.schemas")
    parser.add_argument("--schemas", type=Path, required=True)
    parser.add_argument("--examples", type=Path, required=True)
    parser.add_argument("--destination", type=Path, required=True)
    return parser.parse_args()


if __name__ == "__main__":
    args = _parse_args()
    generate_static_page(
        schemas=args.schemas,
        examples=args.examples,
        destination=args.destination,
    )
