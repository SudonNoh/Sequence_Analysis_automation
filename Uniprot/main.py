from Uniprot.api.logic import excel_controller, seq_controller
from Uniprot.api.web_controller import SignalP_controller


class main_signalP:

    def __init__(self):
        self.excel_control = excel_controller()
        self.sequence_control = seq_controller()
        self.signal_control = SignalP_controller()
        self.signal_text = ""

    def first_process(self, file_route, chain_list, sequence_name):

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

    def second_process(self, data, header, url):

        if isinstance(data, list):
            pass
            if isinstance(header, list):
                pass
                if len(data[0]) == len(header):
                    pass
                else:
                    raise ValueError('입력한 list들의 길이를 확인하세요.')
            else:
                raise TypeError("입력한 header의 타입이 list형이어야 합니다.")
        else:
            raise TypeError("입력한 data의 타입이 list형이어야 합니다.")

        try:
            self.signal_control.site_enter(url)
        except ValueError:
            raise ValueError('url을 확인해주세요.')
