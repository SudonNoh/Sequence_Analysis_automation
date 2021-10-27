# module
import pandas as pd


class excel_controller:

    def __init__(self):
        self.data = ''
        self.data_value = []
        self.data_header = []

    # excel 읽어오기
    def call_excel(self, file_route):

        self.data = pd.read_excel(file_route)
        # if "signal peptide == NaN" or "Sequence == NaN", remove
        self.data = self.data.dropna(subset=['Signal peptide', 'Sequence'])
        self.data_value = self.data.values.tolist()
        self.data_header = self.data.columns.tolist()
        return self.data_value, self.data_header


class seq_controller:

    def __init__(self):
        self.end_number = ''
        self.start_number = ''
        self.seq = ''
        self.signal_peptide = ''
        self.new_seq = []

    # Signal peptide 첫 번호, 끝 번호 찾기
    def string_control(self, fulltext):
        self.end_number = fulltext[fulltext.find('..')+2:fulltext.find(';')]
        self.start_number = fulltext[fulltext.find('SIGNAL')+len('SIGNAL'):fulltext.find('..')]
        return int(self.start_number), int(self.end_number)

    # Sequence 자르기
    def sequence_slice(self, sequence, signal_text):
        start_num, end_num = self.string_control(signal_text)
        self.seq = sequence[start_num-1:end_num]
        return self.seq

    # Sequence 붙이기
    def combine_seq(self, sequence, signal_text, chain_list):
        self.signal_peptide = self.sequence_slice(sequence, signal_text)

        self.new_seq = []
        for i in chain_list:
            full_seq = self.signal_peptide + i
            self.new_seq.append(full_seq)
        return self.new_seq
