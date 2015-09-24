#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is a module gets today's date."""

import datetime

CURDATE = None


def get_current_date():
    """Return today's date

    Args:
        (int): Current day

    Returns:
        date: the year, month, day

    Examples:
        >>> import task_01
        >>> print task_01.CURDATE
        None
        >>> print task_01.get_current_date()
        datetime.date(2015, 9, 24)
    """
    return datetime.date.today()

if __name__ == '__main__':
    CURDATE = get_current_date()
    print CURDATE
