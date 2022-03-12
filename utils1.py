import json


# Импортируем json


def load_candidate(filename):
    """Функция загружает Json файл"""
    file = open(filename, "r", encoding="utf - 8")
    data = json.load(file)
    file.close()
    return data


all_candidates = load_candidate("candidates.json")


def get_candidate(candidates):
    """Функция Загружает форматированную версию кандидатов для главной страницы"""
    candidates_list = ""
    for candidate in candidates:
        candidate_user = f'<pre>\nИмя кандидата - {candidate["name"]}\n' \
                         f'Позиция кандидата - {candidate["position"]}\n' \
                         f'Навыки через запятую - {candidate["skills"]}\n</pre>\n'
        candidates_list += candidate_user
    return candidates_list


def get_candidate_id(user_id, candidates):
    """Функция Загружает пользователей по id для страницы /candidate"""
    for candidate in candidates:
        if candidate["id"] == int(user_id):
            candidate_user = f'<img src="{candidate["picture"]}">\n\n' \
                             f'<pre>\nИмя кандидата - {candidate["name"]}\n' \
                             f'Позиция кандидата - {candidate["position"]}\n' \
                             f'Навыки через запятую - {candidate["skills"]}\n</pre>\n'
            break
    else:
        candidate_user = f"Кандидат с таким id не найден"
    return candidate_user


def get_candidate_skills(user_skills, candidates):
    """Функция Загружает и проверяет пользователей по навыкам для страницы /skills"""
    skill_list = ""
    all_candidate_skill = ""
    for candidate in candidates:
        skill_list = candidate["skills"].lower()
        if user_skills.lower() in skill_list:
            candidate_user = f'<pre>\nИмя кандидата - {candidate["name"]}\n' \
                             f'Позиция кандидата - {candidate["position"]}\n' \
                             f'Навыки через запятую - {candidate["skills"]}\n</pre>\n'
            all_candidate_skill += candidate_user

    if len(all_candidate_skill) < 1:
        return "Такой навык не найден"
    else:
        return all_candidate_skill
