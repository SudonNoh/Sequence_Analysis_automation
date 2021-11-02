from Uniprot.api.logic2 import main_signalP, export_logic
from Uniprot.api.web_controller import SignalP_controller

import time

p = main_signalP()


file_route = "C:/Users/SD NOH/PycharmProjects/OpenInnovation/data/file1.xlsx"
site_route = "https://services.healthtech.dtu.dk/service.php?SignalP-4.1"
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

standard_variable = 0.150

seq_data, seq_header = p.change_data(file_route, chain_list, seq_name)
# seq_data = seq_data[6400:]

q = SignalP_controller()
q.site_enter(site_route)
time.sleep(5)

result_data = []
count_for = 1
for i in seq_data:
    html = q.input_seq(i[7])
    if html == "":
        break
    i.append(html)
    result_data.append(i)
    print(
        "**", seq_data.index(i)+1, "번째 Sequence 분석\n"
        " Entry: ", i[0], "\n",
        "Result: \n", html[0:500], "..."
    )

    if len(result_data) == 800:
        save_excel = export_logic(result_data, standard_variable, seq_header, file_route,
                                  file_number=str(seq_data.index(i)+1))
        result_data = []
        # Reboot controller
        q.driver.quit()
        q = SignalP_controller()
        q.site_enter(site_route)
        time.sleep(5)

    elif count_for != len(seq_data):
        print("count_for  :", count_for)
        print("len(seq_data)  :", len(seq_data))
        count_for += 1
        q.back_and_clear()

    else:
        q.finish()
        print("SignalP 검색이 끝났습니다.")
        save_excel = export_logic(result_data, standard_variable, seq_header, file_route,
                                  file_number=str(seq_data.index(i) + 1))

# file 읽기
import pandas as pd
# import os
#
# file_list = []
# dirt = 'C:/Users/SD NOH/PycharmProjects/OpenInnovation/'
# for i in os.listdir(dirt):
#     if os.path.isdir(dirt + i):
#         pass
#     elif os.path.isfile(dirt + i):
#         if i[-4:] == 'xlsx':
#             file_list.append(i)
#         else:
#             pass
#
# for i, j in zip(file_list, range(len(file_list))):
#     globals()['{}_raw'.format(i[:-5])] = pd.read_excel(i, sheet_name='Raw data')
#     globals()['{}_new'.format(i[:-5])] = pd.read_excel(i, sheet_name='New data')

route = 'C:/Users/SD NOH/PycharmProjects/OpenInnovation/'
x1_raw = pd.read_excel(route + 'SignalP__800.xlsx', sheet_name='Raw data')
x1_new = pd.read_excel(route + 'SignalP__800.xlsx', sheet_name='New data')

x2_raw = pd.read_excel(route + 'SignalP__1600.xlsx', sheet_name='Raw data')
x2_new = pd.read_excel(route + 'SignalP__1600.xlsx', sheet_name='New data')

x3_raw = pd.read_excel(route + 'SignalP__2400.xlsx', sheet_name='Raw data')
x3_new = pd.read_excel(route + 'SignalP__2400.xlsx', sheet_name='New data')

x4_raw = pd.read_excel(route + 'SignalP__3200.xlsx', sheet_name='Raw data')
x4_new = pd.read_excel(route + 'SignalP__3200.xlsx', sheet_name='New data')

x5_raw = pd.read_excel(route + 'SignalP__4000.xlsx', sheet_name='Raw data')
x5_new = pd.read_excel(route + 'SignalP__4000.xlsx', sheet_name='New data')

x6_raw = pd.read_excel(route + 'SignalP__4800.xlsx', sheet_name='Raw data')
x6_new = pd.read_excel(route + 'SignalP__4800.xlsx', sheet_name='New data')

x7_raw = pd.read_excel(route + 'SignalP__5600.xlsx', sheet_name='Raw data')
x7_new = pd.read_excel(route + 'SignalP__5600.xlsx', sheet_name='New data')

x8_raw = pd.read_excel(route + 'SignalP__6400.xlsx', sheet_name='Raw data')
x8_new = pd.read_excel(route + 'SignalP__6400.xlsx', sheet_name='New data')

x9_raw = pd.read_excel(route + 'SignalP__624.xlsx', sheet_name='Raw data')
x9_new = pd.read_excel(route + 'SignalP__624.xlsx', sheet_name='New data')

new_list = [x1_new, x2_new, x3_new, x4_new, x5_new, x6_new, x7_new, x8_new, x9_new]
raw_list = [x1_raw, x2_raw, x3_raw, x4_raw, x5_raw, x6_raw, x7_raw, x8_raw, x9_raw]

new_data = pd.concat(new_list, axis=0, ignore_index=True).drop(columns='Unnamed: 0')
raw_data = pd.concat(raw_list, axis=0, ignore_index=True).drop(columns='Unnamed: 0')

duplicate_raw_data = raw_data.drop_duplicates()

writer = pd.ExcelWriter('SignalP_final.xlsx', engine='xlsxwriter')

duplicate_raw_data.to_excel(writer, sheet_name='Raw data', index=None)
new_data.to_excel(writer, sheet_name='New data', index=None)

writer.save()
