class Date:
    '''
    Date


    Example:
    date = Date(2019, 5, 22)
    print(date)



    '''
    DAY_OF_MONTH = ((31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  #
                    (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31))  #

    def __init__(self, year, month, day):
        '''
        year:  int otherwise TypeError
        month: int 1 < month <= 12

        '''

        self.is_valid_date(year, month, day)
        self.__year = year
        self.__month = month
        self.__day = day

    def __str__(self):
        return self.date

    def __repr__(self):
        return f'Date({self.__year!r}, {self.__month!r}, {self.__day!r})'

    @staticmethod
    def is_leap_year(year):
        return False  #

    @classmethod
    def get_max_day(cls, year, month):
        leap_year = 1 if cls.is_leap_year(year) else 0
        return cls.DAY_OF_MONTH[leap_year][month - 1]

    @property
    def date(self):
        return f'{self.__day}.{self.__month}.{self.__year}'

    @classmethod
    def is_valid_date(cls, year, month, day):
        if not isinstance(year, int):
            raise TypeError('year must be int')
        if not isinstance(month, int):
            raise TypeError('month must be int')
        if not isinstance(day, int):
            raise TypeError('day must be int')

        if not 0 < month <= 12:
            raise ValueError('month must be 0 < month <= 12')

        if not 0 < day <= cls.get_max_day(year, month):
            raise ValueError('invalid day for this month and year')

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise TypeError('Date must be str')
        value = value.split('.')
        if len(value) != 3:
            raise ValueError('Invalid date format')

        try:
            day = int(value[0])
            month = int(value[1])
            year = int(value[2])
            self.is_valid_date(year, month, day)
        except:
            raise ValueError('Invalid date format')

        self.__day = day
        self.__month = month
        self.__year = year

    @property
    def day(self):
        return self.__day

    #     @day.setter
    #     def day(self, value):
    #         value = int(value)
    #         self.is_valid_date(self.__year, self.__month, value)
    #         self.__day = value

    @property
    def month(self):
        return self.__month

    #     @month.setter
    #     def month(self, value):
    #         value = int(value)
    #         self.is_valid_date(self.__year, value, self.__day)
    #         self.__month = value

    @property
    def year(self):
        return self.__year

    #     @year.setter
    #     def year(self, value):
    #         value = int(value)
    #         self.is_valid_date(value, self.__month, self.__day)
    #         self.__year = value

    def add_day(self, day):
        while day > self.DAY_OF_MONTH[1][self.__month]:
            self.__month += 1
            day -= self.DAY_OF_MONTH[1][self.__month]
        if self.__day + day > self.DAY_OF_MONTH[1][self.__month]:
            self.__month += 1
            self.__day = self.__day + day - self.DAY_OF_MONTH[1][self.__month]
        pass

    def add_month(self, month):
        while month > 12:
            self.__year += 1
            month -= 12
        if self.__month + month > 12:
            self.__year += 1
            self.__month = self.__month + month - 12

    def add_year(self, year):
        self.__year += year

    @staticmethod
    def day_counter(date1):
        return date1.__year * 365 + date1.month * 30 + date1.day

    @staticmethod
    def date2_date1(date2, date1):
        return Date.day_counter(date2) - Date.day_counter(date1)



if __name__ == "__main__":
    date1 = Date(2019, 12, 31)
    print(date1.__str__())
    date1.add_year(100)
    print(date1.__str__())
    date1.add_month(18)
    print(date1.__str__())
    date1.add_day(100)
    print(date1.__str__())

    date2 = Date(2019, 12, 31)
    date3 = Date(1999, 12, 31)
    print(Date.date2_date1(date2, date3))
