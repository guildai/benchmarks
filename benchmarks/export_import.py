import os
import shutil
from tempfile import mkdtemp

from .utils import command_with_args, run_with_args


def try_cleanup():
    try:
        command_with_args(["runs", "rm", "-y"])
    except SystemExit:
        pass


def seed_runs():
    run_with_args(["msg=[hello,hi,hola]", "-y"])


class TimeSuite:
    def setup(self):
        self.cwd = os.getcwd()
        os.chdir(
            os.path.join(os.getenv("ASV_ENV_DIR", ""), "project", "examples", "hello")
        )
        seed_runs()
        self.exported_dir_to_import = mkdtemp()
        command_with_args(["export", "-y", self.exported_dir_to_import])

    def teardown(self):
        try_cleanup()

    def time_export_with_copy(self):
        command_with_args(["export", "-y", mkdtemp()])

    def time_export_with_move(self):
        try_cleanup()
        # Not ideal at all here, but we need to make sure that when executing multiple runs here,
        # we don't move the runs the first time and then do nothing subsequent times.
        seed_runs()
        command_with_args(["export", "-y", "--move", mkdtemp()])

    def time_import_with_copy(self):
        # would be nice to omit this, but otherwise setup only runs once and we perform multiple
        # iterations of the import. As a result, we only do the work on the first iteration.
        try_cleanup()
        command_with_args(["import", "-y", self.exported_dir_to_import])

    def time_import_with_move(self):
        # would be nice to omit this, but otherwise setup only runs once and we perform multiple
        # iterations of the import. As a result, we only do the work on the first iteration.
        try_cleanup()
        backup_dir = os.path.join(mkdtemp(), "dummy")
        # Not ideal at all here, but we need to make sure that when executing multiple runs here,
        # we don't move the runs the first time and then do nothing subsequent times.
        shutil.copytree(self.exported_dir_to_import, backup_dir)
        command_with_args(["import", "-y", "--move", backup_dir])
