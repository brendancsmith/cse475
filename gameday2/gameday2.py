#!/usr/bin/env python27
# encoding: utf-8

from pyvotecore.schulze_method import SchulzeMethod


def run_example():
    ballots = [
        {'count': 3, 'ballot': [['A'], ['C'], ['D'], ['B']]},
        {'count': 9, 'ballot': [['B'], ['A'], ['C'], ['D']]},
        {'count': 8, 'ballot': [['C'], ['D'], ['A'], ['B']]},
        {'count': 5, 'ballot': [['D'], ['A'], ['B'], ['C']]},
        {'count': 5, 'ballot': [['D'], ['B'], ['C'], ['A']]}
    ]
    result = SchulzeMethod(
        ballots,
        ballot_notation=SchulzeMethod.BALLOT_NOTATION_GROUPING)

    return result.as_dict()
