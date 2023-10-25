from enum import StrEnum


class Status(StrEnum):
    OPENED = "OPN"
    ASSIGNED = "ASG"
    CLOSED = "CLS"

    def values(cls):
        results = []
        for element in cls:
            el = (element.value, element.value)
            results.append(el)
        return results
