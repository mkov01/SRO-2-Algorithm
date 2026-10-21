import json
import os
from typing import List, Dict, Optional

class EventManager:
    """Менеджер каталога мероприятий университета."""
    def __init__(self, data_file: str = "events.json"):
        self.data_file = data_file
        self.events: List[Dict] = []
        self.load_data()

    def load_data(self) -> None:
        """Загрузка данных из JSON-файла (Лекция 7, 8)."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    self.events = json.load(f)
            except Exception:
                self.events = []
        else:
            self.events = []

    def save_data(self) -> None:
        """Сохранение данных в JSON-файл."""
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.events, f, ensure_ascii=False, indent=4)

    def add_event(self, event_id: int, title: str, category: str, date: str, max_seats: int) -> bool:
        """Добавление нового мероприятия с валидацией ввода (Лекция 5)."""
        if any(e['id'] == event_id for e in self.events):
            return False  # Ошибка: ID должен быть уникальным
        if max_seats <= 0 or not title.strip() or not category.strip():
            return False  # Ошибка ввода: неверные параметры

        new_event = {
            "id": event_id,
            "title": title.strip(),
            "category": category.strip(),
            "date": date.strip(),
            "max_seats": max_seats,
            "registered_users": []
        }
        self.events.append(new_event)
        self.save_data()
        return True

    def filter_events(self, category: Optional[str] = None, search_query: Optional[str] = None) -> List[Dict]:
        """Фильтрация и поиск мероприятий по категориям и строкам (Лекция 4, 6, 7)."""
        results = self.events
        if category:
            results = [e for e in results if e['category'].lower() == category.lower()]
        if search_query:
            results = [e for e in results if search_query.lower() in e['title'].lower()]
        return results

    def register_participant(self, event_id: int, student_id: str) -> str:
        """Регистрация участника на мероприятие с проверкой лимитов."""
        for event in self.events:
            if event['id'] == event_id:
                if student_id in event['registered_users']:
                    return "ALREADY_REGISTERED"
                if len(event['registered_users']) >= event['max_seats']:
                    return "NO_SEATS"
                event['registered_users'].append(student_id)
                self.save_data()
                return "SUCCESS"
        return "EVENT_NOT_FOUND"

    def cancel_registration(self, event_id: int, student_id: str) -> bool:
        """Отмена регистрации участника."""
        for event in self.events:
            if event['id'] == event_id:
                if student_id in event['registered_users']:
                    event['registered_users'].remove(student_id)
                    self.save_data()
                    return True
                return False
        return False
