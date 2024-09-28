import pandas as pd
import numpy as np
import json

# cào 2 bảng trong trang web dưới, quan tâm đến bảng phía sau
url = 'https://en.wikipedia.org/wiki/History_of_Python'
dfs = pd.read_html(url)
df = dfs[1]

# yêu cầu: lấy ra 2 cột 'Version', 'Release date', gán vào biến df2
# _________df2 = df[['Version', 'Release date']]

# yêu cầu: thay đổi cột 'Version' dòng số 12, 27, 28 thành giá trị -1  # df2['Version'][i]

# yêu cầu: thay đổi cột 'Release date' dòng số 15, 27 thành giá trị None (numpy.nan)  # df2['Release date'][i]
# yêu cầu: thay đổi cột 'Version' dòng số 5 thành giá trị None (numpy.nan)

# yêu cầu: giải thích lỗi sai của câu lệnh sau, sửa lại cho đúng
df['Release date'] = df['Release date'].str.replace(r'\[\d+\]', '', regex=True)
df2['Ver_Reda'] = df['Version'].astype(str) + '___' + pd.to_datetime(df['Release date'])

# yêu cầu: lưu df2 vào file ver_reda.csv  # to_csv()

# yêu cầu: tạo ra 1 dictionary từ nội dung df2  # df2.to_json() -> str; json.loads() -> dict

# yêu cầu: bỏ các dòng dữ liệu không đầy đủ từ biến df2, gán vào biến drna  # .dropna()

# yêu cầu: bỏ các cột dữ liệu không đầy đủ từ biến df2, gán vào biến drna_  # axis=1

# yêu cầu: thay các giá trị None (np.nan) ở cột 'Version' bằng giá trị trung bình của cả cột, ở cột 'Release date' bằng giá trị 0 rồi gán vào biến filna
