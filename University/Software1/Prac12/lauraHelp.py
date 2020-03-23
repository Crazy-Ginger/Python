#!/usr/bin/env python3
import unittest
from itertools import product


def string_combinations(*strings):
    return map(lambda x: "".join(x), product(*strings))


def replacer(target, target_char="?", replace_with=["1", "0"]):
    # Base case: there's nothing more to replace in the string
    try:
        next_index = target.index(target_char)
    except ValueError:
        return [target]

    # Replace the next occurence of target_char
    replaced = (target[:next_index] + char for char in replace_with)
    # Recurse
    remainders = replacer(target[next_index + 1:], target_char, replace_with)

    # Get combinations of those two lists (and make them into strings)
    return string_combinations(replaced, remainders)


class ReplacerTest(unittest.TestCase):
    def test_single(self):
        self.assertEqual(
            ["1", "0"],
            list(replacer("?")),
        )

    def test_mutiple(self):
        self.assertEqual(
            ["11", "10", "01", "00"],
            list(replacer("??")),
        )

    def test_non_contiguous(self):
        self.assertEqual(
            ["1a1", "1a0", "0a1", "0a0"],
            list(replacer("?a?")),
        )

    def test_non_default_replace(self):
        self.assertEqual(
            ["1a1", "1a0", "0a1", "0a0"],
            list(replacer("bab", target_char="b")),
        )

    def test_non_default_list(self):
        self.assertEqual(
            ["AaA", "AaB", "BaA", "BaB"],
            list(replacer("?a?", replace_with=["A", "B"])),
        )


unittest.main()
