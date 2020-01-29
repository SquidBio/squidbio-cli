from .cmds import clone_seq, lint_seq


class SquidBio(object):
    """A platform for collaborative DNA projects"""

    def __str__(self):
        return "A platform for collaborative DNA projects"

    def lint(self, seq_path):
        lint_seq(seq_path)

    def clone(self, seq_string):
        clone_seq(seq_string)
