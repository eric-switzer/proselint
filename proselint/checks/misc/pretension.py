# -*- coding: utf-8 -*-
"""Pretentious words

---
layout:     post
source:     ???
source_url: ???
title:      pretentious words
date:       2014-06-10 12:31:19
categories: writing
---

https://www.reddit.com/r/AskReddit/comments/22y54w/whats_the_most_pretentious_word_you_know/
"""
from proselint.tools import existence_check, memoize


@memoize
def check(text):
    """Check the text."""
    err = "misc.pretension"
    msg = u"Pretentious word"

    list = [
        "reconceptualize",
        "demassification",
        "attitudinally",
        "judgmentally",
        "vis-a-vis",
        "grandiloquent",
        "equestrian",
        "loquacious",
        "defenestration",
    ]

    return existence_check(text, list, err, msg, max_errors=1)
