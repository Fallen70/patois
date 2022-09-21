
AJE = """Title: Aje
Tri: Aje
Date: 2010-12-03 10:20
Category: patois
Tags: A
Trad: Content
"""

AJE_LESS = """Title: Aje
Tri: Aje
Date: 2010-12-03 10:20
Category: patois
"""


def test_from_file(tmp_path):
    from tools.word import Word, UNDEFINED
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
    assert w.path == p

    p.write_text(AJE_LESS)
    w = Word.from_file(p)
    assert w.title == "Aje"
    assert w.tri == "Aje"
    assert w.tags == UNDEFINED
    assert w.category == "patois"
    assert w.trad == UNDEFINED
    assert w.path == p


def test_to_french_simple(aje):

    words , errors = aje.to_french()
    print( words, errors )
    print( aje.__dict__)
    assert len(words) == 1
    assert len(errors) == 0

    w = words[0]
    assert w.title == "Content"
    assert w.tri == "Content"
    assert w.tags == "C"
    assert w.category == "français"
    assert w.trad == "Aje"

def test_to_french_no_title(aje):
    from tools.word import UNDEFINED

    aje.title = UNDEFINED 
    words , errors = aje.to_french()
    assert len(words) == 0
    assert len(errors) == 1
    assert errors == [aje.path]

def test_to_french_no_tri(aje):
    from tools.word import UNDEFINED

    aje.tri = UNDEFINED 
    words , errors = aje.to_french()
    assert len(words) == 0
    assert len(errors) == 1
    assert errors == [aje.path]

def test_to_french_no_tags(aje):
    from tools.word import UNDEFINED

    aje.tags = UNDEFINED 
    words , errors = aje.to_french()
    assert len(words) == 0
    assert len(errors) == 1
    assert errors == [aje.path]

def test_to_french_no_trad(aje):
    from tools.word import UNDEFINED

    aje.tags = UNDEFINED 
    words , errors = aje.to_french()
    assert len(words) == 0
    assert len(errors) == 1
    assert errors == [aje.path]

def test_to_french_no_category(aje):
    from tools.word import UNDEFINED

    aje.category = UNDEFINED 
    words , errors = aje.to_french()
    assert len(words) == 0
    assert len(errors) == 1
    assert errors == [aje.path]
