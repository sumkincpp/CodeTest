from tempfile import NamedTemporaryFile
from typing import IO

# https://stackoverflow.com/questions/64429113/how-should-a-namedtemporaryfile-be-annotated
def example(tmp: IO[Any]) -> str:
    print(tmp.file)
    return tmp.name

print(example(NamedTemporaryFile()))