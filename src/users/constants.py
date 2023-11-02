from enum import StrEnum


class Role(StrEnum):
    ADMIN = "AD"
    JUNIOR = "JR"
    SENIOR = "SR"

    @classmethod
    def values(cls):
        results = []
        for element in cls:
            el = (element.value, element.value)
            results.append(el)
        return results
