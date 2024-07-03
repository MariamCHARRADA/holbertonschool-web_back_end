#!/usr/bin/env python3
"""Parameterize and patch as decorators """

import unittest
from parameterized import parameterized
from utils import access_nested_map, memoize
from unittest.mock import patch, Mock
from unittest import mock, TestCase
from client import GithubOrgClient


class TestGithubOrgClient(TestCase):
    """class for testing GithubOrgClient"""

    @parameterized.expand([("google",
                            {"login": "google",
                             "id": 1}),
                           ("abc",
                            {"login": "abc",
                             "id": 2})])
    @patch("client.GithubOrgClient.get_json")
    def test_org(self, org_name, expected_value, mock_get_json):
        """test GithubOrgClient"""
        mock_get_json.return_value = expected_value
        client = GithubOrgClient(org_name)
        result = client.org

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, expected_value)
