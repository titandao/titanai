import json
import pytest
from titanai import TitanAI, process_data

def test_sdk_version():
    sdk = TitanAI()
    assert sdk.version == "0.1.0"

def test_process_data():
    result = process_data([1, 2, 3])
    assert result == "[1, 2, 3]"

def test_process_dict():
    sdk = TitanAI()
    result = sdk.process({"name": "TitanAI"})
    assert "TitanAI" in result
