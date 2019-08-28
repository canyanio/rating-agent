from graphql.language import ast  # type: ignore

from graphene.types import Scalar  # type: ignore
from graphene.types.scalars import MIN_INT, MAX_INT  # type: ignore


class BigInt(Scalar):
    """
    BigInt is an extension of the regular Int field that supports Integers bigger than a signed 32-bit integer.
    """

    @staticmethod
    def big_to_float(value):
        num = int(value)
        if num > MAX_INT or num < MIN_INT:
            return float(int(num))
        return num

    serialize = big_to_float
    parse_value = big_to_float

    @staticmethod
    def parse_literal(node):
        if isinstance(node, ast.IntValue):
            num = int(node.value)
            if num > MAX_INT or num < MIN_INT:
                return float(int(num))
            return num
