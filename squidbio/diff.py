from difflib import SequenceMatcher

def diff(seq1, seq2):
    if seq1 == seq2:
        return [('equal', 0, len(seq1), 0, len(seq2))]
    s = SequenceMatcher(None, seq1, seq2, False)
    return s.get_opcodes()

def green_print(text):
    GREEN = '\033[1;32;48m'
    END = '\033[1;37;0m'
    print('{}{}{}'.format(GREEN, text, END))

def red_print(text):
    RED = '\033[1;31;48m'
    END = '\033[1;37;0m'
    print('{}{}{}'.format(RED, text, END))

def print_diffs(diffs, seq1, seq2):
    for diff in diffs:
        diff_type = diff[0]
        if diff_type == 'equal':
            continue
        r_start, r_end, a_start, a_end = diff[1:]
        if r_start != r_end:
            print('Removed ({} - {}):'.format(r_start, r_end))
            red_print(seq1[diff[1]:diff[2]])
        if a_start != a_end:
            print('Added ({} - {}):'.format(a_start, a_end))
            green_print(seq2[diff[3]:diff[4]])
        print()
