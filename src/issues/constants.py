from enum import StrEnum


class Status(StrEnum):
    OPENED = "OPN"
    ASSIGNED = "ASG"
    CLOSED = "CLS"

    @classmethod
    def values(cls):
        results = []
        for element in cls:
            el = (element.value, element.value)
            results.append(el)
        return results
