money = int(input("교환할 돈은 얼마 ? "))

m50000 = money // 50000
money %= 50000

m10000 = money // 10000
money %= 10000

m5000 = money // 5000
money %= 5000

m1000 = money // 1000
money %= 1000

m500 = money // 500
money %= 500

m100 = money // 100
money %= 100

m50 = money // 50
money %= 50

m10 = money // 10
money %= 10

print("50000원 %d장, 10000원 %d장, 5000원 %d장, 1000원 %d장\n"
        "500원 %d개, 100원 %d개, 50원 %d개, 10원 %d개\n"
          "바꾸지 못한 돈 ==> %d원"
            % (m50000, m10000, m5000, m1000, m500, m100, m50, m10, money))