import json

from json_file import JSONFile


def test_parsed():
    file = JSONFile("tests/test_parsed.json")
    file.write(json.dumps({"key": "value"}))
    assert file.parsed()["key"] == "value"
    file.delete()


def test_parsed_cached_changed_file():
    file = JSONFile("tests/test_parsed_cached_changed_file.json")
    file.write(json.dumps({"key": "value"}))
    file.parsed_cached()
    file.write(json.dumps({"key2": "value2"}))
    assert file.parsed_cached()["key"] == "value"
    file.delete()


def test_parsed_cached_updating_cache():
    file = JSONFile("tests/test_parsed_cached_updating_cache.json")
    file.write(json.dumps({"key": "value"}))
    file.parsed_cached()
    file.write(json.dumps({"key2": "value2"}))
    assert file.parsed_cached(True)["key2"] == "value2"
    file.delete()
