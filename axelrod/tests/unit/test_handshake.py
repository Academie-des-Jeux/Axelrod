"""Test for the Handshake strategy."""

import axelrod

from .test_player import TestPlayer

C, D = axelrod.Actions.C, axelrod.Actions.D


class TestHandshake(TestPlayer):

    name = "Handshake"
    player = axelrod.Handshake
    expected_classifier = {
        'memory_depth': float('inf'),
        'stochastic': False,
        'makes_use_of': set(),
        'long_run_time': False,
        'inspects_source': False,
        'manipulates_source': False,
        'manipulates_state': False
    }

    def test_strategy(self):
        # Test initial play sequence
        self.responses_test([], [], [C, D])

        self.responses_test([C, D], [C, D], [C] * 20)
        self.responses_test([C, D], [C, C], [D] * 20)
        self.responses_test([C, D], [D, C], [D] * 20)
        self.responses_test([C, D], [D, D], [D] * 20)

        self.responses_test([C, D] * 2, [D, C] * 2, [D])
        self.responses_test([C, D] * 2, [C, D] * 2, [C])
