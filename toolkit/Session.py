import sys
import toolkit.autodiff.CalcFlow as c


class Session(object):

    def __init__(self, name, verbose=False):
        self.name = name

        self.verbose = verbose

        if verbose:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def __enter__(self):

        if self.verbose:
            self.stdout.write("Entering Session\n")

    def __exit__(self, the_type, the_value, the_traceback):
        c.CalcFlow.full_reset()

        if self.verbose:
            self.stdout.write("Exiting Session\n")

    def __str__(self):
        return self.name
