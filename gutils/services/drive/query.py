import typing
import datetime
import warnings

from ..enums import QueryFields, Operator, MimeType

class Query:

    def __init__(self) -> None:
        self.data = list()

    def FIELD(self, field: typing.Union[QueryFields, str]) -> 'Query':
        self.data.append(f"{field}")
        return self

    @property
    def EQUALS(self) -> 'Query':
        self.data.append(f"{Operator.EQUALS}")
        return self

    @property
    def NOT_EQUALS(self) -> 'Query':
        self.data.append(f"{Operator.NOT_EQUALS}")
        return self
    
    @property
    def CONTAINS(self) -> 'Query':
        self.data.append(f"{Operator.CONTAINS}")
        return self
    
    @property
    def NOT(self) -> 'Query':
        self.data.append(f"{Operator.NOT}")
        return self

    @property
    def IN(self) -> 'Query':
        self.data.append(f"{Operator.IN}")
        return self
    
    @property
    def AND(self) -> 'Query':
        self.data.append(f"{Operator.AND}")
        return self

    @property
    def OR(self) -> 'Query':
        self.data.append(f"{Operator.OR}")
        return self
    
    @property
    def HAS(self) -> 'Query':
        self.data.append(f"{Operator.HAS}")
        return self
    
    @property
    def LESS_THAN(self) -> 'Query':
        self.data.append(f"{Operator.LESS_THAN}")
        return self
    
    @property
    def LESS_THAN_EQUALS(self) -> 'Query':
        self.data.append(f"{Operator.LESS_THAN_EQUALS}")
        return self
    
    @property
    def GREATER_THAN(self) -> 'Query':
        self.data.append(f"{Operator.GREATER_THAN}")
        return self
    
    @property
    def GREATER_THAN_EQUALS(self) -> 'Query':
        self.data.append(f"{Operator.GREATER_THAN_EQUALS}")
        return self

    def VALUE(self, value: typing.Union[str, int, float, datetime.datetime, MimeType]) -> 'Query':
        if isinstance(value, datetime.datetime):
            warnings.warn("Timezone for Datetime objects should be in UTC", UserWarning, stacklevel=2)
            value = value.strftime("%Y-%m-%dT%H:%M:%S")
        if isinstance(value, bool):
            value = str(value).lower()
        self.data.append(f"'{value}'")
        return self

    def __str__(self) -> str:
        return ''.join(self._lines()).strip()

    def _lines(self) -> typing.Iterable[str]:
        for thing in self.data:
            if not thing:
                continue
            yield " " + thing
