#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Steepest Ascent Hill Climbing
"""
from ag_frame.algorithms import base
from ag_frame.algorithms import utils


class SAHC(base.Algorithm):
    """Steepest Ascent Hill Climbing."""

    _name = "Steepest Ascent Hill Climbing"

    def __init__(self):
        super(SAHC, self).__init__()
        self.size_var = []
        self.domains = None
        self.precision = 40
        self.max_retry = 500

    @classmethod
    def is_implemented(cls):
        """Check if the Clase is finnal."""
        return True

    def execute(self, function):
        """The algorithm implementation."""
        self.size_var = []
        self.domains = function.get_domain_restrictions

        for i in range(function.nr_args):
            size = utils.get_nr_bits(self.domains[i], self.precision)
            self.size_var.append(size)

        global_best = None
        best_found = False
        retry = self.max_retry
        while retry > 0:
            big_string = '0' * sum(self.size_var)
            big_string = utils.randomise_a_string(big_string)

            best = big_string if not best_found else global_best
            best_found = False
            new = best
            for i in range(len(big_string)):
                new = utils.mutate(best, i)

                args_best = self.string_to_args(best)
                args_new = self.string_to_args(new)

                f_best = function(*args_best)
                f_new = function(*args_new)

                if f_new < f_best:
                    best = new
                    break
            retry -= 1
            # Base case when there is no global_best
            if global_best is None:
                global_best = best
                continue

            # Compera the global_best with the new generated best
            args_global_best = self.string_to_args(global_best)
            args_best = self.string_to_args(best)
            if function(*args_best) < function(*args_global_best):
                global_best = best
                best_found = True

        return self.string_to_args(global_best)
