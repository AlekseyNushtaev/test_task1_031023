from unittest import TestCase
from main import get_unique_names, get_top_names, get_super_names

class TestNames(TestCase):
    def setUp(self) -> None:
        self.courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python",
                   "Frontend-разработчик с нуля"]

        self.mentors = [
            ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
             "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина",
             "Азамат Искаков",
             "Роман Гордиенко"],
            ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
             "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев",
             "Никита Шумский",
             "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов",
             "Евгений Грязнов",
             "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
            ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
             "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая",
             "Денис Ежков",
             "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
            ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
             "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин",
             "Михаил Ларченко"]
        ]
    def test_is_not_none_1(self):
        self.assertIsNotNone(get_unique_names(self.mentors))
    def test_is_not_none_2(self):
        self.assertIsNotNone(get_top_names(self.mentors))
    def test_is_not_none_3(self):
        self.assertIsNotNone(get_super_names(self.mentors, self.courses))
    def test_in_1(self):
        self.assertIn('Адилет', get_unique_names(self.mentors))
    def test_in_2(self):
        self.assertIn(['Александр', 10], get_top_names(self.mentors))
    def test_in_3(self):
        self.assertIn(['Python-разработчик с нуля', 'Java-разработчик с нуля', 'Антон, Евгений, Максим'],
                      get_super_names(self.mentors, self.courses))
    def test_greater_1(self):
        self.assertGreater(len(get_unique_names(self.mentors)), 15)
    def test_greater_2(self):
        self.assertGreater(len(get_top_names(self.mentors)), 2)
    def test_greater_3(self):
        self.assertGreater(len(get_super_names(self.mentors, self.courses)), 5)