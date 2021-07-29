class Human:
    """This is a class Human"""

    def __init__(self, name, surname, sex, age, nationality, salary, job):
        self.name = name
        self.surname = surname
        self.sex = sex
        self.age = age
        self.nationality = nationality
        self.__salary = salary
        self.job = job

    def __call__(self, *args, **kwargs):
        pass

    def __str__(self):
        return f'Person name is {self.name} and age is {self.age}'

    def decorator_function(func):
        def wrapper():
            func()
            return 'Nice to meet you!!!'
        return wrapper()

    def say_hi(self):
        print(f'Hi, I am {self.name}')

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def quit_job(self):
        self.job = None

    def eat(self):
        pass

    def drink(self):
        pass

    def change_name(self, new_name):
        self.name = new_name


class Child(Human):
    def __init__(self, name, surname, sex, age, nationality, job, salary):
        super().__init__(name, surname, sex, age, nationality, job, salary)

    def quit_job(self):
        print('Oops, I am too young, so I have no job to quit')

    def cry(self):
        print('Waa waa waa waa')


if __name__ == '__main__':

    David = Human(
        name='David',
        surname='Smith',
        sex='male',
        age=32,
        nationality='american',
        salary=2000,
        job='software engineer')
    Joe = Child(
        name='Joe',
        surname='Smith',
        sex='male',
        age=5,
        nationality='american',
        salary=None,
        job=None)
    print(David.__doc__)
    David.say_hi()
    David.quit_job()
    print(David.job)
    Joe.quit_job()
    David.set_salary(5000)
    David.get_salary()
