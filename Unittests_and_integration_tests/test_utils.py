#!/usr/bin/env python3
"""Parameterize a unit test """

import unittest
from parameterized import parameterized
from utils import access_nested_map, memoize
from unittest.mock import patch, Mock
from unittest import mock, TestCase


class TestAccessNestedMap(unittest.TestCase):
    """testing nested map"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, map, path, expected):
        """test method"""
        output = access_nested_map(map, path)
        self.assertEqual(output, expected)

    @parameterized.expand(
        [
            ({}, ("a",), "a"),
            ({"a": 1}, ("a", "b"), "b"),
        ]
    )
    def test_access_nested_map_exception(self, map, path, wrong):
        """test that a KeyError is raised for the following inputs"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)
            self.assertEqual(wrong, e.exception)


class TestGetJson(unittest.TestCase):
    """TestGetJson class"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, test_url, test_payload):
        """Test get_json returns the expected result"""
        with patch("utils.requests.get") as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response


class TestMemoize(TestCase):
    """Class for testing memoize"""

    def test_memoize(self):
        """Test memoize"""

        class TestClass:
            """test class"""

            def a_method(self):
                """returns 42"""
                return 42

            @memoize
            def a_property(self):
                """returns memoized"""
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as mock_method:
            test_instance = TestClass()

            result1 = test_instance.a_property
            result2 = test_instance.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            mock_method.assert_called_once()
