from datetime import date, datetime , timedelta


class DeadLine:

    number_days = timedelta(days=180)

    def __init__(self, name, surname, d0, d1):
        self.name = name
        self.surname = surname
        self.d0 = d0
        self.d1 = d1
        self.sum_date = d1 - d0


    def sum(self):
        return self.d1 - self.d0

    def adding_date(self, other):
        return self.sum() + other.sum_date

    def date_update(self):
        return self.d0 + DeadLine.number_days


dilnoza = DeadLine('Dilnoza', 'Baratova', date(2022, 5, 18), date(2022, 6, 3))
dilnoza_1 = DeadLine('Dilnoza', 'Baratova', date(2022, 6, 5), date(2022, 7, 9))

print(dilnoza.sum())
print(dilnoza.adding_date(dilnoza_1))
print(dilnoza.date_update())


