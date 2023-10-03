def get_unique_names(mentors: list[list[str]]) -> list[str]:
    all_list = []
    for m in mentors:
        all_list.extend(m)
    all_names_list = []
    for mentor in all_list:
        name = mentor.split()[0]
        all_names_list.append(name)
    unique_names = set(all_names_list)
    all_names_sorted = list(unique_names)
    all_names_sorted.sort()
    return all_names_sorted

def get_top_names(mentors: list[list[str]]) -> list[list[str, int]]:
    all_list = []
    for m in mentors:
        all_list.extend(m)
    all_names_list = []
    for mentor in all_list:
        name = mentor.split()[0]
        all_names_list.append(name)
    unique_names = set(all_names_list)
    popular = []
    for name in unique_names:
        popular.append([name, all_names_list.count(name)])
    popular.sort(key=lambda x: x[1], reverse=True)
    return popular[:3]

def get_super_names(mentors: list[list[str]], courses: list[str]) -> list[list[str]]:
    mentors_names = []
    for m in mentors:
        course_names = []
        for name in m:
            course_names.append(name.split()[0])
        mentors_names.append(course_names)
    print(mentors_names)
    pairs = []
    super_list = []
    for id1 in range(len(mentors_names)):
        for id2 in range(len(mentors_names)):
            if id1 != id2:
                intersection_set = set(mentors_names[id1]) & set(mentors_names[id2])
                if len(intersection_set) > 0:
                    pair = {courses[id1], courses[id2]}
                    if pair not in pairs:
                        pairs.append(pair)
                        all_names_sorted = sorted(intersection_set)
                        super_list.append([courses[id1], courses[id2], ', '.join(all_names_sorted)])
    return super_list

if __name__ == "__main__":

    courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python",
               "Frontend-разработчик с нуля"]

    mentors = [
        ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
         "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина",
         "Азамат Искаков",
         "Роман Гордиенко"],
        ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
         "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
         "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
         "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
        ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
         "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая",
         "Денис Ежков",
         "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
        ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
         "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
    ]
    print(get_unique_names(mentors))
    print(get_top_names(mentors))
    print(get_super_names(mentors, courses))