def total_pay(bill,tip):
    tip_pay=(tip/100)*bill
    total=tip_pay+bill
    print("total_pay",total)
total_pay(100,19)