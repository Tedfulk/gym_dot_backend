from enum import Enum
from typing import Type


class StrEnum(str, Enum):
    """Enum with string values."""

    def __str__(self) -> str:
        """Return the value of the enum as a string.
        Example:
            >>> class MyEnum(StrEnum):
            ...     one = "one string"
            ...     two = "two string"
            >>> str(MyEnum.one) === "one string"
        """
        return self.value

    @staticmethod
    def get_enum_by_values(instance: Type["StrEnum"]) -> list[str]:
        """Get enum by value.
        Example:
            >>> class MyEnum(StrEnum):
            ...     one = "one string"
            ...     two = "two string"
            >>> StrEnum.get_enum_by_values(MyEnum) === ["one string", "two string"]
        """
        return [member.value for member in instance]

    @staticmethod
    def get_enum_by_names(instance: Type["StrEnum"]) -> list[str]:
        """Get enum by name.
        Example:
            >>> class MyEnum(StrEnum):
            ...     one = "one string"
            ...     two = "two string"
            >>> StrEnum.get_enum_by_names(MyEnum) === ["one", "two"]
        """
        return [member.name for member in instance]
