class student:
    def __init__(self, f, l):
        self.first = f
        self.last = l

    def input(self):
        self.grades = []
        self.num = int(input('How many grades? '))
        for i in range(self.num):
            grade = float(input('What are the grades? '))
            self.grades.append(grade)
        return self.grades, self.num

    def ave(self):
        sum = 0
        for i in range(self.num):
            sum = sum + self.grades[i]
            self.average = sum/self.num
        return self.average

    def highLow(self):
        self.high = 0
        self.low = 100
        for i in range(self.num):
            if self.grades[i] > self.high:
                self.high = self.grades[i]
            if self.grades[i] < self.low:
                self.low = self.grades[i]
        return self.high, self.low

    def printG(self):
        for i in range(self.num):
            print(self.grades[i])
        print(self.ave())
        print(self.highLow())
        # print(self.low)


jm = student("Jaime", "Mitchell")

z = jm.input()
print(jm.first, jm.last)
y = jm.printG()
