from Uniprot.api.logic import excel_controller, seq_controller


exc_c = excel_controller()
seq_c = seq_controller()

filename = "C:/Users/SD NOH/PycharmProjects/OpenInnovation/data/file1.xlsx"

data_value, data_header = exc_c.call_excel(filename)

chain_list = [
     'DIQMTQSPSSLSASVGDRVTITCRASQGIRNYLAWYQQKPGKAPKLLIYAASTLQSGVPSRFSGSGSGTDFTLTISSLQPEDVATYYCQRYNRAPYTFGQGTKVEIKRTVAAP'
     'SVFIFPPSDEQLKSGTASVVCLLNNFYPREAKVQWKVDNALQSGNSQESVTEQDSKDSTYSLSSTLTLSKADYEKHKVYACEVTHQGLSSPVTKSFNRGEC',
     'EVQLVESGGGLVQPGRSLRLSCAASGFTFDDYAMHWVRQAPGKGLEWVSAITWNSGHIDYADSVEGRFTISRDNAKNSLYLQMNSLRAEDTAVYYCAKVSYLSTASSLDYWGQ'
     'GTLVTVSSASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKKVEPKSCDK'
     'THTCPPCPAPELLGGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAPIEKT'
     'ISKAKGQPREPQVYTLPPSRDELTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSKLTVDKSRWQQGNVFSCSVMHEALHNHYTQKSLSLSPGK',
     'QVQLVQSGVEVKKPGASVKVSCKASGYTFTNYYMYWVRQAPGQGLEWMGGINPSNGGTNFNEKFKNRVTLTTDSSTTTAYMELKSLQFDDTAVYYCARRDYRFDMGFDYWGQG'
     'TTVTVSSASTKGPSVFPLAPCSRSTSESTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTKTYTCNVDHKPSNTKVDKRVESKYGPPC'
     'PPCPAPEFLGGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSQEDPEVQFNWYVDGVEVHNAKTKPREEQFNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKGLPSSIEKTISKA'
     'KGQPREPQVYTLPPSQEEMTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSRLTVDKSRWQEGNVFSCSVMHEALHNHYTQKSLSLSLGK',
     'EIVLTQSPATLSLSPGERATLSCRASKGVSTSGYSYLHWYQQKPGQAPRLLIYLASYLESGVPARFSGSGSGTDFTLTISSLEPEDFAVYYCQHSRDLPLTFGGGTKVEIKRT'
     'VAAPSVFIFPPSDEQLKSGTASVVCLLNNFYPREAKVQWKVDNALQSGNSQESVTEQDSKDSTYSLSSTLTLSKADYEKHKVYACEVTHQGLSSPVTKSFNRGEC'
 ]

seq_name = [
    'Adalimumab-LC',
    'Adalimumab-HC',
    'Pembrilizumab-LC',
    'Pembrilizumab-HC'
]

new_file = []
# data_value에서 1행을 꺼내 row_data에 할당
for row_data in data_value:
    count_col = 0

    # new_row_data는 Sequence name과 새롭게 추가되는 New Sequence를 일시적으로 담을 list
    new_row_data = []
    for each_data, header in zip(row_data, data_header):
        count_col += 1
        new_row_data.append(each_data)
        if count_col == 5: # signal peptide column number로 변수로 설정
            # seq_c.combine_seq에 사용할 signal_text를 지정
            signal_text = each_data

        if count_col == 6: # Sequence column number로 변수로 설정
            # Sequence를 자르고 붙이는 과정을 진행
            x = seq_c.combine_seq(each_data, signal_text, chain_list=chain_list)
            # 새로 만든 Sequence list인 x의 요소 하나씩 꺼내 new_file에 저장
            for i, j in zip(x, seq_name):
                add_data = [j, i]
                # new_row_data는 4번 연속 사용되어야 하기 때문에 새로 만든 Sequence와 Sequence name을 add_data에 추가한 후
                # new_row_data와 합쳐 append_data에 할당
                append_data = new_row_data + add_data
                new_file.append(append_data)

for p in new_file:
    print(p)

new_header = data_header + ['Sequence name', 'New Sequence']

import pandas as pd

new_dataframe = pd.DataFrame(new_file, columns=new_header, index=None)
