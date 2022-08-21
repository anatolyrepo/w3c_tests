from deepdiff import DeepDiff


class Assertions:
    """
    Типовые проверки для тестов.

    """

    @staticmethod
    def is_equal(expected, actual):
        assert expected == actual, f'Expected object {expected} is not equal to actual object {actual}'

    @staticmethod
    def deep_diff_equal(first, second):
        r = DeepDiff(first, second)
        assert not r, r

    @staticmethod
    def deep_diff_not_equal(first, second):
        r = DeepDiff(first, second)
        assert r, r
