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

    def test_public_repos_url(self, mock_org):
        """test public_repos_url"""
        mock_org.return_value = {
            "repos_url": "https://api.github.com/orgs/google/repos"
        }
        client = GithubOrgClient("google")
        result = client.public_repos_url()
        self.assertEqual(result, "https://api.github.com/orgs/google/repos")

    @patch("client.GithubOrgClient.get_json")
    def test_public_repos(self, mock_get_json):
        """ test public_repos"""
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"}
        ]

        with patch('client.GithubOrgClient._public_repos_url', new_callable=unittest.mock.PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "https://api.github.com/orgs/test_org/repos"
            client = GithubOrgClient("test_org")

            result = client.public_repos()

            self.assertEqual(result, ["repo1", "repo2"])

            mock_public_repos_url.assert_called_once()

            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/test_org/repos")
