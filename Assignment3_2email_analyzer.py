# 2 ნაწილი
# 1) შექმენით ფაილი email_analyzer.py
# მოცემული გაქვთ ცვლადი text = "ჩვენი გუნდის წევრები არიან: saba.ananidze@itstep.com, მეგობარი დიმა dima123@gmail.com და კიდევ ერთი ტესტური მისამართი test_user@yahoo.com"
text = "ჩვენი გუნდის წევრები არიან: saba.ananidze@itstep.com, მეგობარი დიმა dima123@gmail.com და კიდევ ერთი ტესტური მისამართი test_user@yahoo.com"
# 2) გამოიყენეთ re.findall-ი და შესაბამისი რეგექს პატერნი, რომ ტექსტიდან ამოიღოთ მხოლოდ ელფოსტის მისამართები სიის სახით. 
import re
# 3) მიღებული სია, გადააქციეთ ერთ ინდივიდუალურ სტრინგად რომელთა ქვესტრინგები იქნება შეერთებული "+" ით
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
# შედეგი უნდა იყოს - "saba.ananidze@itstep.com+dima123@gmail.com+test_user@yahoo.com"
result = "+".join(emails)
print(result)