import sys
from unittest.mock import patch

from guild.main import main


def command_with_args(args):
    args = [""] + args
    with patch.object(sys, "argv", args):
        main()


def run_with_args(args):
    return command_with_args(["run"] + args)
