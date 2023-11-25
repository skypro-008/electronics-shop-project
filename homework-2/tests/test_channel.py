
import pytest
from src.channel import Channel

def test_get_service():
    service = Channel.get_service()
    assert service is not None

def test_to_json(tmp_path):
    channel = Channel("123", "Test Channel", "This is a test channel", "https://www.youtube.com/testchannel", 1000, 50, 5000)
    channel.to_json()
    file_content = (tmp_path / "123.json").read_text()
    assert file_content == '{"id": "123", "title": "Test Channel", "description": "This is a test channel", "link": "https://www.youtube.com/testchannel", "subscribers": 1000, "videos": 50, "views": 5000}'