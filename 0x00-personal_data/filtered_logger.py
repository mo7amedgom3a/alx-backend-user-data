#!/usr/bin/env python3
import re


def filter_datum(fields: list, redaction: str,
                 message: str, separator: str) -> str:
    """
    Returns the log message obfuscated
    The function should use a regex to replace occurrences of
    certain field values.
    """

    for field in fields:
        message = re.sub(rf'{field}=.+?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message
