"""
    В классе учится n учеников. Известны их имена.
    Известно так же кто был в гостях у Кати, кто был у Васи и т.д.
    Определить, есть ли в классе хотя бы один человек, который не был в гостях ни у кого из своих одноклассников.
    Если есть такие ученики, то вывести их имена, если нет, то сообщить об этом.

    Использовать множество
"""

words = ['hello', 'daddy', 'hello', 'mum']

statuses = {'guest_kate', 'guest_vasya'}

students = [
    {
        'name': 'Евгений',
        'status': {
            'guest_kate',
            'guest_vasya',
        }
    },
    # {
    #     'name': 'Михаил',
    #     'status': {
    #         'guest_kate',
    #         'guest_vasya',
    #
    #     }
    # },
    # {
    #     'name': 'Вадим',
    #     'status': {
    #         'guest_vasya'
    #     }
    # },

]

# print(students[0]['status'].difference())
# print(len(students[0]['status']))

