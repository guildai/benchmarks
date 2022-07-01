import os
from tempfile import mkdtemp

from .utils import command_with_args, run_with_args

# we can't run these examples with python 3.8+, because this example needs tensorflow 1.x, and
#  isn't available on python 3.8+

# class TimeSuite:
#     def setup(self):
#         self.cwd = os.getcwd()
#         os.chdir(os.path.join(os.getenv("ASV_ENV_DIR", ""), "project", "examples", "tensorflow"))

#     def time_guild_ops(self):
#         command_with_args(["ops"])

#     def time_guild_run_train_default(self):
#         run_with_args(["epochs=1", "--no-gpus", "-y"])

#     def time_guild_compare(self):
#         command_with_args(["compare", "--table", "1"])

#     def time_runs_info(self):
#         command_with_args(["runs", "info"])

#     def time_runs_info_scalars(self):
#         command_with_args(["runs", "info", "-s"])

#     def time_run_mnist_directly(self):
#         run_with_args(["mnist.py", "--no-gpus", "-y", "epochs=1"])

#     def time_guild_compare_csv(self):
#         command_with_args(["compare", "1", "2", "--csv", os.path.join(mkdtemp(), "compare.csv")])
