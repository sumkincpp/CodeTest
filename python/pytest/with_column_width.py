@contextmanager
def using_column_width(w: int):
    mp = pytest.MonkeyPatch()
    mp.setenv("COLUMNS", w)
    try:
        yield
    finally:
        mp.undo()

def test_foo():
    with using_column_width(120): 
        ...