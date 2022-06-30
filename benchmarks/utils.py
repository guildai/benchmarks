import sys
from unittest.mock import patch

from guild.main import main

def run_with_args(args):
    args = ["", "run"] + args
    with patch.object(sys, 'argv', args):
        main()