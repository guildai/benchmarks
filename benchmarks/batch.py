import uuid

from .utils import run_with_args

import os

class TimeSuite:
    """
    An example benchmark that times the performance of various kinds
    of iterating over dictionaries in Python.
    """
    def setup(self):
        self.script = os.path.join(os.getenv("ASV_BUILD_DIR", ""), str(uuid.uuid4())+".py")
        with open(self.script, "w") as f:
            f.write("x=1\n")
            f.write("y=2\n")
            f.write("print(x+y)\n")

    def teardown(self):
        os.remove(self.script)

    def time_normal_batch(self):
        run_with_args([self.script, "x=[1,2]", "y=[2,3]"])

    def time_max_trials_less_than_full(self):
        run_with_args([self.script, "x=[1,2]", "y=[2,3]", "--max-trials", "3"])

    def time_max_trials_greater_than_full(self):
        run_with_args([self.script, "x=[1,2]", "y=[2,3]", "--max-trials", "5"])

    def time_max_trials_random_batch(self):
        run_with_args([self.script, "x=[1:100]", "--max-trials", "5"])

    def time_max_trials_optimizer_default_objective(self):
        run_with_args([self.script, "x=[1:100]", "-o", "gp"])

    def time_max_trials_optimizer_explicit_objective(self):
        run_with_args([self.script, "x=[1:100]", "-o", "gbrt", "-X", "foo", "-m10"])

