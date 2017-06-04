from mountapi import version


def test_version_data_exists():
    assert version.__name__
    assert version.__description__
    assert version.__url__
    assert version.__version__
    assert version.__build__
    assert version.__author__
    assert version.__author_email__
    assert version.__license__
    assert version.__copyright__
