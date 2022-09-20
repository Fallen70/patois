

AJE = """Title: Aje
Tri: Aje
Date: 2010-12-03 10:20
Category: patois
Tags: A
Trad: Content
"""

def test_from_file(tmp_path):
    from tools.word import Word
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "aje.md"
    p.write_text(AJE)
    w = Word.from_file(p)
    assert w.title == "Aje"
    assert w.tri == "Aje"
    assert w.tags == "A"
    assert w.category == "patois"
    assert w.trad == "Content"

