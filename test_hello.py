import unittest
from hello import hello


class TestHello(unittest.TestCase):
    """Test suite for hello() function"""
    
    def test_default_greeting(self):
        """Test default greeting returns 'Hello, World!'"""
        result = hello()
        self.assertEqual(result, 'Hello, World!')
    
    def test_custom_name(self):
        """Test greeting with custom name"""
        result = hello('Alice')
        self.assertEqual(result, 'Hello, Alice!')
    
    def test_multiple_names(self):
        """Test greeting with various names"""
        test_cases = [
            ('Bob', 'Hello, Bob!'),
            ('Charlie', 'Hello, Charlie!'),
            ('Acme AI Labs', 'Hello, Acme AI Labs!'),
        ]
        for name, expected in test_cases:
            with self.subTest(name=name):
                self.assertEqual(hello(name), expected)
    
    def test_empty_string_raises_error(self):
        """Test that empty string raises ValueError"""
        with self.assertRaises(ValueError) as context:
            hello('')
        self.assertIn('empty', str(context.exception).lower())
    
    def test_whitespace_only_raises_error(self):
        """Test that whitespace-only string raises ValueError"""
        with self.assertRaises(ValueError):
            hello('   ')
    
    def test_non_string_raises_type_error(self):
        """Test that non-string input raises TypeError"""
        invalid_inputs = [123, 45.67, [], {}, True]
        for invalid_input in invalid_inputs:
            with self.subTest(input=invalid_input):
                with self.assertRaises(TypeError) as context:
                    hello(invalid_input)
                self.assertIn('string', str(context.exception).lower())
    
    def test_none_uses_default(self):
        """Test that None uses default 'World'"""
        result = hello(None)
        self.assertEqual(result, 'Hello, World!')


if __name__ == '__main__':
    unittest.main()
