from Uniprot.api.logic import excel_controller, seq_controller
import pandas as pd

class main_signalP:

    def __init__(self):
        self.excel_control = excel_controller()
        self.sequence_control = seq_controller()
        self.signal_text = ""

    def change_data(self, file_route, chain_list, sequence_name):

        # file route의 경로를 확인하고, 경로가 맞지 않으면 FilenotFoundError 출력력
        try:
            data_value, data_header = self.excel_control.call_excel(file_route)
        except FileNotFoundError:
            raise FileNotFoundError('파일 경로를 다시 설정해주시기 바랍니다.')

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

        new_data = []
        new_header = data_header + ['Sequence name', 'New Sequence']
        for row_data in data_value:
            count_col = 0

            new_row_data = []
            for each_data, header in zip(row_data, data_header):
                count_col += 1
                new_row_data.append(each_data)
                if count_col == 5:  # signal peptide column number로 변수로 설정
                    # seq_c.combine_seq에 사용할 signal_text를 지정
                    self.signal_text = each_data

                if count_col == 6:  # Sequence column number로 변수로 설정
                    # Sequence를 자르고 붙이는 과정을 진행
                    x = self.sequence_control.combine_seq(each_data, self.signal_text, chain_list=chain_list)
                    # 새로 만든 Sequence list인 x의 요소 하나씩 꺼내 new_file에 저장
                    for i, j in zip(x, sequence_name):
                        add_data = [j, i]
                        # new_row_data는 4번 연속 사용되어야 하기 때문에 새로 만든 Sequence와 Sequence name을 add_data에 추가한 후
                        # new_row_data와 합쳐 append_data에 할당
                        append_data = new_row_data + add_data
                        new_data.append(append_data)

        return new_data, new_header


def export_logic(result_data, standard_variable, seq_header, file_route, file_number):
    final_list = []
    for i in range(len(result_data)):
        # 위 데이터의 8번째 요소를 추출
        row_list = result_data[i][8].split()

        count_overScore = 0
        new_row_list = []
        k = ""

        # 이제 안에 있는 요소들을 하나씩 추출해 C행에 해당하는 열인지 확인하고
        # 만약 C행에 해당하는 요소(j)이면 standard_variable과 비교
        num = 0
        for j in range(len(row_list)):
            if j == 2 + (5 * num):
                num += 1

                if float(row_list[j]) >= standard_variable:
                    count_overScore += 1
                    k = k + row_list[j - 2] + "  " + row_list[j - 1] + "  " + row_list[j] + " / " \
                        # + row_list[j + 1]+"  "+row_list[j + 2]+"\n "

                    print(row_list[j - 2], "  ", row_list[j - 1], "  ", row_list[j], "  ", row_list[j + 1], "  ",
                          row_list[j + 2], "**")
                else:
                    print(row_list[j - 2], "  ", row_list[j - 1], "  ", row_list[j], "  ", row_list[j + 1], "  ",
                          row_list[j + 2])

        result_data[i].append(count_overScore)
        result_data[i].append(k)
        final_list.append(result_data[i])

    final_header = seq_header + ['Result', 'Count_OverScore', 'index_OverScore']
    final_pd = pd.DataFrame(final_list, columns=final_header)

    raw_sheet = final_pd[['Entry', 'Entry name', 'Protein names', 'Gene names', 'Signal peptide', 'Sequence']]
    new_sheet = final_pd[['Entry', 'New Sequence', 'Result', 'Count_OverScore', 'index_OverScore']]

    # Create a pandas Excel writer using xlsxwriter as the engine.
    writer = pd.ExcelWriter('SignalP_' + file_number + '.xlsx', engine='xlsxwriter')

    # Write each dataframe to a different worksheet
    raw_sheet.to_excel(writer, sheet_name='Raw data')
    new_sheet.to_excel(writer, sheet_name='New data')

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()



