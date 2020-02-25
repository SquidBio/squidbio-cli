import os

from .cmds import clone_project, clone_seq, config, diff_project, diff_seq, lint_seq


class SquidBio(object):
    """A platform for collaborative DNA projects"""

    def __str__(self):
        return "A platform for collaborative DNA projects"

    def diff(self, path='.'):
        if os.path.isdir(path):
            diff_project(path)
        else:
            diff_seq(path)

    def lint(self, seq_path):
        lint_seq(seq_path)

    def clone(self, url, seq=False):
        if seq:
            clone_seq(url)
        else:
            clone_project(url)

    def config(self):
        config()
