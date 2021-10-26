from .logic import excel_controller, seq_controller


exc_c = excel_controller()
seq_c = seq_controller()

filename = "C:/Users/SD NOH/PycharmProjects/OpenInnovation/data/file1.xlsx"
data_value, data_header = exc_c.call_excel(filename)

