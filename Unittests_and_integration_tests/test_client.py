#!/usr/bin/env python3
"""Parameterize and patch as decorators """

import unittest
from parameterized import parameterized, parameterized_class
from utils import access_nested_map, memoize
from unittest.mock import patch, Mock, PropertyMock
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos
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

    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
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
        """test public_repos"""
        repo1 = {"name": "Repo1", "license": {"key": "license1"}}
        repo2 = {"name": "Repo2", "license": {"key": "license2"}}
        repo3 = {"name": "Repo3"}
        to_mock = "client.GithubOrgClient._public_repos_url"
        mock_get_json.return_value = [repo1, repo2, repo3]

        with patch(
            to_mock,
            new_callable=PropertyMock,
            return_value="https://api.github.com/orgs/test_org/repos",
        ) as mock_public_repos_url:
            client = GithubOrgClient("test_org")

            self.assertEqual(
                client.public_repos(), [
                    "Repo1", "Repo2", "Repo3"])

            self.assertEqual(client.public_repos("license1"), ["Repo1"])
            self.assertEqual(client.public_repos("license3"), [])
            self.assertEqual(client.public_repos(123), [])

            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/test_org/repos"
            )
            mock_public_repos_url.assert_called_once_with()


    @patch("client.GithubOrgClient.get_json")
    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """test license"""
        result = GithubOrgClient.has_license(repo, license_key)

        self.assertEqual(result, expected)
