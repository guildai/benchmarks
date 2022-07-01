import os

import guild

from .utils import run_with_args


class TimeSuite:
    def setup(self):
        self.cwd = os.getcwd()
        os.chdir(
            os.path.join(
                os.getenv("ASV_ENV_DIR", ""), "project", "examples", "dependencies"
            )
        )

    def teardown(self):
        os.chdir(self.cwd)

    def time_missing_op(self):
        try:
            run_with_args(["file-op"])
        except SystemExit:
            print("Missing op - skipping exception")

    def time_stage_required_op(self):
        run_with_args(["file", "--stage", "-y"])

    def time_staged_run_selected(self):
        run_with_args(["file-op"])

    def time_downstream_op(self):
        run_with_args(["file-op", "--stage"])
