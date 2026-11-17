"""Tiny helpers for writing lesson content.

E(q, sql)            worked example (shown with its result in the lesson)
P(sql, q=None)       "what will this query return?" question (answer in solutions)
X(level, q, sql)     exercise; level 1=easy 2=medium 3=hard
check=...            for INSERT/UPDATE/DELETE/CREATE: a SELECT that shows the effect
note=...             short tip shown under the result
"""


def E(q, sql, check=None, note=None):
    return dict(q=q, sql=sql, check=check, note=note)


def P(sql, q=None, note=None):
    d = dict(sql=sql, note=note)
    if q:
        d["q"] = q
    return d


def X(level, q, sql, check=None, note=None):
    return dict(level=level, q=q, sql=sql, check=check, note=note)


def Q(level, q, sql, kind="write", given=None, check=None, note=None):
    """Exam-style question.
    kind="write"    write the query
    kind="output"   the result table is shown; students find the query
    kind="value"    the query is shown; students fill in the result
    kind="complete" a skeleton with ____ is shown (given=...); students complete it
    """
    return dict(level=level, q=q, sql=sql, kind=kind, given=given, check=check, note=note)
