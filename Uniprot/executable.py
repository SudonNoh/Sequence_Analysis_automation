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

q = SignalP_controller()
q.site_enter(site_route)
time.sleep(5)

result_data = []
count_for = 0
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

    else:
        q.back_and_clear()
        count_for += 1
        if len(seq_data) == count_for:
            q.finish()
            print("SignalP 검색이 끝났습니다.")
            save_excel = export_logic(result_data, standard_variable, seq_header, file_route,
                                      file_number=str(seq_data.index(i) + 1))



#
# # 위에서 나온 결과 데이터(result_data)를 한 행씩 추출
# final_list = []
# for i in range(len(result_data)):
#     # 위 데이터의 8번째 요소를 추출
#     row_list = result_data[i][8].split()
#
#     count_overScore = 0
#     new_row_list = []
#     k = ""
#
#     # 이제 안에 있는 요소들을 하나씩 추출해 C행에 해당하는 열인지 확인하고
#     # 만약 C행에 해당하는 요소(j)이면 standard_variable과 비교
#     num = 0
#     for j in range(len(row_list)):
#         if j == 2+(5*num):
#             num += 1
#
#             if float(row_list[j]) >= standard_variable:
#                 count_overScore += 1
#                 k = k+row_list[j - 2]+"  "+row_list[j - 1]+"  "+row_list[j]+" / "\
#                     # + row_list[j + 1]+"  "+row_list[j + 2]+"\n "
#
#                 print(row_list[j - 2], "  ", row_list[j - 1], "  ", row_list[j], "  ", row_list[j + 1], "  ",
#                       row_list[j + 2], "**")
#             else:
#                 print(row_list[j - 2], "  ", row_list[j - 1], "  ", row_list[j], "  ", row_list[j + 1], "  ",
#                       row_list[j + 2])
#
#     result_data[i].append(count_overScore)
#     result_data[i].append(k)
#     final_list.append(result_data[i])
#
# final_header = seq_header + ['Result', 'Count_OverScore', 'index_OverScore']
# final_pd = pd.DataFrame(final_list, columns=final_header)
#
# raw_sheet = final_pd[['Entry', 'Entry name', 'Protein names', 'Gene names', 'Signal peptide', 'Sequence']]
# new_sheet = final_pd[['Entry', 'New Sequence', 'Result', 'Count_OverScore', 'index_OverScore']]
#
# # Create a pandas Excel writer using xlsxwriter as the engine.
# writer = pd.ExcelWriter('SignalP_'+file_route[-10:], engine='xlsxwriter')
#
# # Write each dataframe to a different worksheet
# raw_sheet.to_excel(writer, sheet_name='Raw data')
# new_sheet.to_excel(writer, sheet_name='New data')
#
# # Close the Pandas Excel writer and output the Excel file.
# writer.save()
