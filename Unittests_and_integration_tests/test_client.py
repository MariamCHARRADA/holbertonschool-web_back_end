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


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient."""

    @classmethod
    def setUpClass(cls):
        """Set up class method to mock requests.get with example payloads."""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            """Side effect function to mock requests.get(url).json()."""
            if url == 'https://api.github.com/orgs/testorg':
                return Mock(json=lambda: org_payload)
            elif url == 'https://api.github.com/orgs/testorg/repos':
                return Mock(json=lambda: repos_payload)
            else:
                raise ValueError(f"Unexpected URL: {url}")

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Tear down class method to stop the patcher."""
        cls.get_patcher.stop()

    @parameterized_class('org_payload, repos_payload, expected_repos, apache2_repos', [
        (org_payload, repos_payload, expected_repos, apache2_repos),
    ])
    def test_public_repos_integration(
            self,
            org_payload,
            repos_payload,
            expected_repos,
            apache2_repos):
        """Integration test for GithubOrgClient.public_repos method."""
        client = GithubOrgClient('testorg')

        # Test public_repos method
        repos = client.public_repos()

        # Assertions
        self.assertEqual(repos, expected_repos)
        apache2_repos_actual = client.public_repos("apache-2.0")
        self.assertEqual(apache2_repos_actual, apache2_repos)
