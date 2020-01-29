from Bio import SeqIO


def parse_seq(seq_file, seq_type):
    seq_data = {}
    
    with open(seq_file, 'r') as f:
        seq = next(SeqIO.parse(f, seq_type))

    seq_data['name'] = seq.name
    seq_data['seq'] = str(seq.seq)
    seq_data['annotations'] = [{
        'label': a.qualifiers.get('label', [None])[0],
        'note': a.qualifiers.get('note', [None])[0],
        'type': a.type,
        'start': int(a.location.start),
        'end': int(a.location.end),
        'strand': a.location.strand,
    } for a in seq.features]
    
    return seq_data
