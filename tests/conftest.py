import pytest
from tools.word import Word

AJE = """Title: Aje
Tri: Aje
Date: 2010-12-03 10:20
Category: patois
Tags: A
Trad: Content
"""

@pytest.fixture
def aje(tmp_path):
    p = tmp_path / "aje.md"
    p.write_text(AJE)
    w = Word.from_file(p)
    return w


BEUSSE = """Title: Beusse
Tri: Beusse
Date: 2010-12-03 10:20
Category: patois
Tags: B
Trad: Ruche / Tête
"""

@pytest.fixture
def beusse(tmp_path):
    p = tmp_path / "beusse.md"
    p.write_text(BEUSSE)
    w = Word.from_file(p)
    return w

