from mountapi import version


def test_version_contains_name():
    assert hasattr(version, '__name__')


def test_version_contains_description():
    assert hasattr(version, '__description__')


def test_version_contains_url():
    assert hasattr(version, '__url__')


def test_version_contains_version():
    assert hasattr(version, '__version__')


def test_version_contains_build():
    assert hasattr(version, '__build__')


def test_version_contains_author():
    assert hasattr(version, '__author__')


def test_version_contains_author_email():
    assert hasattr(version, '__author_email__')


def test_version_contains_license():
    assert hasattr(version, '__license__')


def test_version_contains_copyright():
    assert hasattr(version, '__copyright__')
