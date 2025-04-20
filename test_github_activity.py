import pytest
from typer.testing import CliRunner
from github_activity import app
from unittest.mock import patch
import requests

runner = CliRunner()

# Test: Invalid username (GitHub returns 404)
@patch("github_activity.requests.get")
def test_invalid_username(mock_get):
    mock_get.return_value.status_code = 404
    result = runner.invoke(app, ["thisuserdoesnotexist12345"])
    assert result.exit_code != 0
    assert "Failed to fetch activity" in result.output

# Test: API failure (e.g. timeout or network error)
@patch("github_activity.requests.get")
def test_api_failure(mock_get):
    mock_get.side_effect = requests.exceptions.RequestException("Network error")
    result = runner.invoke(app, ["torvalds"])
    assert result.exit_code != 0
    assert "Failed to fetch activity" in result.output