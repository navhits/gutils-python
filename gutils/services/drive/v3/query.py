"""
This module contains the query builder for the Drive API.
"""
import typing
import datetime
import warnings

from gutils.services.enums import QueryFields, Operator, MimeType

# pylint: disable=invalid-name
class Query:
    """
    Query builder class for the Drive API.
    """
    def __init__(self) -> None:
        self.data = list()

    def FIELD(self, field: typing.Union[QueryFields, str]) -> 'Query':
        """
        The field name to be queried for
        """
        self.data.append(f"{field}")
        return self

    @property
    def EQUALS(self) -> 'Query':
        """
        Operator equals (=)
        """
        self.data.append(f"{Operator.EQUALS}")
        return self

    @property
    def NOT_EQUALS(self) -> 'Query':
        """
        Operator not equals (!=)
        """
        self.data.append(f"{Operator.NOT_EQUALS}")
        return self

    @property
    def CONTAINS(self) -> 'Query':
        """
        Operators contains (is in)
        """
        self.data.append(f"{Operator.CONTAINS}")
        return self

    @property
    def NOT(self) -> 'Query':
        """
        Operator not (!)
        """
        self.data.append(f"{Operator.NOT}")
        return self

    @property
    def IN(self) -> 'Query':
        """
        Operator in (inside of)
        """
        self.data.append(f"{Operator.IN}")
        return self

    @property
    def AND(self) -> 'Query':
        """
        Operator and (&&)
        """
        self.data.append(f"{Operator.AND}")
        return self

    @property
    def OR(self) -> 'Query':
        """
        Operator or (||)
        """
        self.data.append(f"{Operator.OR}")
        return self

    @property
    def HAS(self) -> 'Query':
        """
        Operator has (has a value)
        """
        self.data.append(f"{Operator.HAS}")
        return self

    @property
    def LESS_THAN(self) -> 'Query':
        """
        Operator less than (<)
        """
        self.data.append(f"{Operator.LESS_THAN}")
        return self

    @property
    def LESS_THAN_EQUALS(self) -> 'Query':
        """
        Operator less than or equals (<=)
        """
        self.data.append(f"{Operator.LESS_THAN_EQUALS}")
        return self

    @property
    def GREATER_THAN(self) -> 'Query':
        """
        Operator greater than (>)
        """
        self.data.append(f"{Operator.GREATER_THAN}")
        return self

    @property
    def GREATER_THAN_EQUALS(self) -> 'Query':
        """
        Operator greater than or equals (>=)
        """
        self.data.append(f"{Operator.GREATER_THAN_EQUALS}")
        return self

    def VALUE(self, value: typing.Union[str, int, float, datetime.datetime, MimeType]) -> 'Query':
        """
        The value to search for
        """
        if isinstance(value, datetime.datetime):
            warnings.warn("Timezone for Datetime objects should be in UTC",
                          UserWarning, stacklevel=2)
            value = value.strftime("%Y-%m-%dT%H:%M:%S")
        if isinstance(value, bool):
            value = str(value).lower()
        self.data.append(f"'{value}'")
        return self

    def __str__(self) -> str:
        """
        Returns the query as a string.
        """
        return ''.join(self._lines()).strip()

    def _lines(self) -> typing.Generator[str, None, None]:
        for item in self.data:
            if not item:
                continue
            yield " " + item
