# -*- coding: utf-8 -*-
"""This module reads the configuration files.

Created on: 11/23/2021
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""
from enum import Enum

class Env(str, Enum):
    """Available environments."""

    dev = "DEV"
    pre = "PRE"
    pro = "PRO"