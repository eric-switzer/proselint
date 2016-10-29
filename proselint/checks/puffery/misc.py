# -*- coding: utf-8 -*-
"""Hedging.

---
layout:     post
source:     Wikipedia manual of style
source_url: Wikipedia:Manual_of_Style/Words_to_watch
title:      puffery
date:       2016-10-29
categories: writing
---

Points out puffery.
We have removed "hit" because it requires more context to detect.
"""
from proselint.tools import existence_check, memoize


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "puffery.misc"
    msg = "Puffery"

    puffery = [
        "legendary",
        "great",
        "acclaimed",
        "visionary",
        "outstanding",
        "leading",
        "celebrated",
        "award-winning",
        "landmark",
        "cutting-edge",
        "innovative",
        "extraordinary",
        "brilliant",
        "famous",
        "renowned",
        "remarkable",
        "prestigious",
        "world-class",
        "respected",
        "notable",
        "virtuoso",
        "honorable",
        "awesome",
        "unique",
    ]

    return existence_check(text, puffery, err, msg)

