import pandas as pd
import numpy as np

new_data = pd.read_excel('C:/Users/SD NOH/PycharmProjects/OpenInnovation/SignalP_final.xlsx', sheet_name='New data')

# Count_OverScore 가 1인 값
data = new_data[new_data['Count_OverScore'] == 1]

# 지정된 열 안에 문자열을 포함한 행들을 추출
# x = data[data['New Sequence'].str.contains('문자열')]

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

# Sequence name을 빼놓고 만들는 바람에 sequence name을 따로 지정하는 명령어를 실행
for i in range(4):
    data.loc[data['New Sequence'].str.contains(chain_list[i]), 'Sequence name'] = seq_name[i]

data_hc = data.loc[data['Sequence name'].str.contains("-HC")]
data_lc = data.loc[data['Sequence name'].str.contains("-LC")]


# Unique 한 Entry 의 수
Entry_count_all = data['Entry'].value_counts()
Entry_count_hc = data_hc['Entry'].value_counts()
Entry_count_lc = data_lc['Entry'].value_counts()

# Entry name 변경
Entry_count_all.name = 'Entry_count_all'
Entry_count_hc.name = 'Entry_count_hc'
Entry_count_lc.name = 'Entry_count_lc'

all_set_4 = Entry_count_all[Entry_count_all == 4]
hc_set_2 = Entry_count_hc[Entry_count_hc == 2]
lc_set_2 = Entry_count_lc[Entry_count_lc == 2]

all_list = list(all_set_4.index)
hc_list = list(hc_set_2.index)
lc_list = list(lc_set_2.index)

all_data = data[data["Entry"].isin(all_list)]
hc_data = data_hc[data_hc["Entry"].isin(hc_list)]
lc_data = data_lc[data_lc["Entry"].isin(lc_list)]

writer = pd.ExcelWriter('filtered_data.xlsx', engine='xlsxwriter')

all_data.to_excel(writer, sheet_name='all', index=None)
hc_data.to_excel(writer, sheet_name='hc', index=None)
lc_data.to_excel(writer, sheet_name='lc', index=None)

writer.save()