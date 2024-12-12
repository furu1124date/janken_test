import unittest
from unittest.mock import patch
from source.player import player_pon  # 正しいインポートパスを指定

class TestPlayer(unittest.TestCase):

    @patch('builtins.input', return_value='1')
    def test_player_pon_gu(self, mock_input):
        self.assertEqual(player_pon(), 'グー')

    @patch('builtins.input', return_value='2')
    def test_player_pon_choki(self, mock_input):
        self.assertEqual(player_pon(), 'チョキ')

    @patch('builtins.input', return_value='3')
    def test_player_pon_pa(self, mock_input):
        self.assertEqual(player_pon(), 'パー')

    @patch('builtins.input', side_effect=['0', '4', '1'])
    def test_invalid_input(self, mock_input):
        self.assertEqual(player_pon(), 'グー')

if __name__ == '__main__':
    unittest.main()