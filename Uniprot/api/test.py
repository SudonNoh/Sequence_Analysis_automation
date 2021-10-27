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
    print(p[-1])

# 데이터 프레임에 넣기 전에, signalP에 입력하는 방법을 구축

new_header = data_header + ['Sequence name', 'New Sequence']

import pandas as pd

new_dataframe = pd.DataFrame(new_file, columns=new_header, index=None)

# 뒤로가기
driver.back()
box.clear()

from Uniprot.api.web_controller import SignalP_controller

sc = SignalP_controller()
site = "https://services.healthtech.dtu.dk/service.php?SignalP-4.1"
sc.site_enter(site)
seq = 'MWVRQVPWSF TWAVLQLSWQ SGWLLEVPNG PWRSLTFYPA WLTVSEGANA TFTCSLSNWS EDLMLNWNRL SPSNQTEKQA AFCNGLSQPV QDARFQIIQL PNRHDFHMNI LDTRRNDSGI YLCGAISLHP KAKIEESPGA ELVVTERILE TSTRYPSPSP KPEGRFQGMV IGIMSALVGI PVLLLLAWAL AVFCSTSMSE ARGAGSKDDT LKEEPSAAPV PSVAYEELDF QGREKTPELP TACVHTEYAT IVFTEGLGAS AMGRRGSADG LQGPRPPRHE DGHCSWPL'
y = sc.input_seq(sequence=seq)

p = y.find("1")
q = y.find("#", p)
x = y[p:q]
x_list = x.split()

try:
    data_value, data_header = exc_c.call_excel("C:/Users/SD NOH/PycharmProjects/OpenInnovation/data/file99.xlsx")
except FileNotFoundError:
    raise FileNotFoundError('파일 경로를 다시 설정해주시기 바랍니다.')

print('a')

chain_list=['x']
sequence_name=['y']

if isinstance(chain_list, list):
    if isinstance(sequence_name, list):
        pass
        if len(chain_list) == len(sequence_name):
            pass
        else:
            raise ValueError('chain_list 와 sequence_name 의 길이가 같아야 합니다.')
    else:
        raise TypeError('sequence_name의 type은 list형 입니다.')
else:
    raise TypeError('chain_list의 type은 list형 입니다.')

print('x')