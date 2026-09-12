start = int(input("시작 곱을 입력해 주세요 : "))  # 2
end = int(input("마지막 곱을 입력해주세요 : ")) # 5
print(type(start))
print(type(end))
while start < end + 1:
     print(f"8 * {start} = {8 * start} ")
     start += 1