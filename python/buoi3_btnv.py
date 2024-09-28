phanmodau: str = """[ Man Narrating ] This is the story
Đây là một câu truyện cách đây rất lâu.
03:01
a time of myth and legend,
Thời đại của những bí ẩn và truyền thuyết.
03:04
when the ancient gods were petty and cruel,
Khi những vị thần cổ đại nhỏ nhen và độc ác,
03:07
and they plagued mankind with suffering.
và họ đầy đọa nhân loại bằng đau khổ.
03:10
Only one man dared to challenge their power--
Chỉ một chàng trai đã dám đứng lên thách thức sức mạnh của họ
03:12
Hercules.
Hercules.
03:16
Hercules possessed a strength the world had never seen,
Hercules được ban một sức mạnh chưa từng thấy
03:18
a strength surpassed only by the power of his heart.
một sức mạnh chỉ có thể bị vượt qua
03:22
He journeyed the earth, battling the minions
Anh đi khắp thế giới, chiến đấu với bè
03:25
the all-powerful queen of the gods.
vị hoàng hậu của các vị thần đầy quyền lực.
03:29
But wherever there was evil,
Nhưng bất cứ nơi đâu có tội ác,
03:32
wherever an innocent would suffer,
nơi đâu có người dân vô tội bị áp bức,
03:34
there would be... Hercules.
nơi đó sẽ có Hercules.
03:37"""

# \n là 1 escape character biểu diễn kí tự xuống dòng, để làm rõ điều này, xem đoạn code sau
khong3hai5 = """He journeyed the earth, battling the minions
Anh đi khắp thế giới, chiến đấu với bè
03:25"""
khong3hai5_ = "He journeyed the earth, battling the minions\nAnh đi khắp thế giới, chiến đấu với bè\n03:25"
print(khong3hai5 == khong3hai5)
print(khong3hai5 in phanmodau)
print(khong3hai5_ in phanmodau)


# yêu cầu:
# 1. code xác định (in ra màn hình) kiểu dữ liệu của biến phanmodau_
# 2. tạo biến tachdong là 1 list 39 phần tử, trog đó mỗi phần tử là 1 dòng của phanmodau, tham khảo https://www.w3schools.com/python/ref_string_split.asp
tachdong: list = phanmodau.split('\n')
print('@@@@@@', tachdong)
# 3. code xác định khong3hai5_ và khong3hai5 (theo như code dòng 47 và 48 thì chúng đều nằm trong phanmodau) xuất hiện từ index bao nhiêu của phanmodau
# tham khảo https://www.w3schools.com/python/ref_string_find.asp
# 4. phanmodau là 1 đoạn phụ đề phim, có 13 câu phụ đề, mỗi phụ đề gồm 3 dòng là tiếng anh, tiếng việt và dòng thời gian
# code 1 vòng for, tạo 1 list caccauphude có 13 phần tử, mỗi phần tử là 1 câu phụ đề (chứa 3 dòng)
# gợi ý: tạo caccauphude là 1 list trống trước, tạo i là 1 số nguyên lặp lại từ 0 đến 2 qua các vòng lặp, lặp trong list tachdong
# trong mỗi vòng lặp, nếu i = 0 thì tạo 1 chuỗi phantuhientai là phần tử hiện tại
# nếu i = 1 hoặc i = 2 thì cộng '\n' vào phantuhientai, cộng tiếp phần tử hiện tại vào phantuhientai
# nếu i = 2 thì thêm phantuhientai vào caccauphude: `caccauphude.append(phantuhientai)`
caccauphude: list = []  # caccauphude: list = list()
i = 0
# for lap in tachdong:
#     if i == 0:  # phân biệt == và is
#         phantuhientai = lap
#         i += 1
#     # else:  # i != 0
#     #     phantuhientai += '\n' + lap  # pythonnic
#     #     if i == 1:
#     #         i += 1
#     #     else:  # i != 1
#     #         caccauphude.append(phantuhientai)
#     #         i = 0
#     elif i == 1:
#         phantuhientai += '\n' + lap  # pythonnic
#         # phantuhientai = phantuhientai + '\n' + lap
#         i += 1
#     elif i == 2:
#         # phantuhientai += '\n' + lap  # pythonnic
#         phantuhientai = phantuhientai + '\n' + lap
#         caccauphude.append(phantuhientai)
#         i = 0

# 5. đề xuất cách làm khác ở câu 4, tham khảo "Sử dụng Enumerate Object trong vòng lặp" https://www.geeksforgeeks.org/enumerate-in-python/
for thutu, lap in enumerate(tachdong):
    du: int = thutu % 3
    if du == 0:  # chia 3 dư 0
        phantuhientai = lap
    else:  # không chia hết cho 3
        phantuhientai += '\n' + lap  # pythonnic
        if du == 2:
            caccauphude.append(phantuhientai)

print(caccauphude)
print('###################', len(caccauphude))
# 6. tạo 1 dictionary, đánh số thứ tự cho list caccauphude bằng cách tương tự như câu 4, ví dụ
# {
#     '1': '[ Man Narrating ] This is the story',
#     '2': 'Đây là một câu truyện cách đây rất lâu.',
#     '3': '03:01', '4': 'a time of myth and legend,',
#     ...
# }
# làm câu 6, dùng hàm enumerate()
# 7. ép kiểu tachdong sang tuple, nhận xét về sự thay đổi
tachdong: tuple = tuple(tachdong)
# 8. ép kiểu tachdong sang set, nhận xét về sự thay đổi
tachdong: set = set(tachdong)
# 9. tiếp tục ép kiểu tachdong về lại list, giải thích đầu ra của câu lệnh sau `print(tachdong.index('Hercules.'))`  # tham khảo https://www.w3schools.com/python/ref_list_index.asp
tachdong: list = list(tachdong)
print(len(tachdong))
# chú ý: câu sau sẽ dùng kết quả của câu trước, nếu không làm được câu trước thì tạo thủ công kết quả của nó rồi làm tiếp câu sau

# for i in range(5):  #
#     print(i)
#
# def range(start, stop=None, step=1):
#     pass
#
# range(5)  # start=5, stop=None, step=1
# range(5, 8)  # start=5, stop=8, step=1
# range(step=3, start=1)  # step=3, start=1, stop=None