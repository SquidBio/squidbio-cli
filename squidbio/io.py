import json
import os
from collections import OrderedDict

from Bio import Alphabet, SeqIO
from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio.SeqRecord import SeqRecord

from .const import seq_types
from .parse_seq import parse_seq


def make_seq(seq_data, seq_name):
    seq = SeqRecord(
        id=seq_name,
        name=seq_name,
        seq=Seq(
            seq_data['Sequence'],
            alphabet=Alphabet.DNAAlphabet()
        )
    )

    seq.features = [SeqFeature(
        FeatureLocation(
            a['start'],
            a['end'],
            a['strand']
        ),
        type=a['type'],
        qualifiers = OrderedDict({
            'label': a['label'],
            'note': a['note'],
        })
    ) for a in seq_data.get('Annotations', [])]
 
    if not os.path.exists(seq_name):
        os.makedirs(seq_name)

    with open('{}/README.md'.format(seq_name), 'w') as f:
        f.write(seq_data.get('ReadMe', ''))

    with open('{}/.sequence.json'.format(seq_name), 'w') as f:
        f.write(json.dumps(seq_data))

    SeqIO.write(seq, "{}/sequence.fasta".format(seq_name), "fasta")
    SeqIO.write(seq, "{}/sequence.gb".format(seq_name), "genbank")


def read_seq(seq_path='sequence.fasta'):
    ext = seq_path[seq_path.rfind('.') + 1:]
    seq_type = seq_types.get(ext)
    if not seq_type:
        print('SquidBio can only read Fastas, GenBank files, and SnapGene files')
        return
    seq_data = parse_seq(seq_path, seq_type)
    return seq_data


def make_project(project_data, project_name):
    if not os.path.exists(project_name):
        os.makedirs(project_name)

    with open('{}/README.md'.format(project_name), 'w') as f:
        f.write(project_data.get('ReadMe', ''))

    with open('{}/.project.json'.format(project_name), 'w') as f:
        f.write(json.dumps(project_data))
