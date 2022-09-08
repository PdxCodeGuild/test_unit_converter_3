import unit_converter_3;
import pytest

def test_unit_converter_3(monkeypatch):
    inputs = iter(['200', 'ft'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert unit_converter_3.unit_converter() == "200 ft is 60.96 m"
