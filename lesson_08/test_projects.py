import pytest
from projects_page import ProjectsPage
from config import Config


class TestProjects:
    # Фикстура для создания экземпляра класса ProjectsPage перед каждым тестом
    @pytest.fixture
    def projects_page(self):
        return ProjectsPage()

    # Фикстура для получения test_user_id из конфигурации
    @pytest.fixture
    def test_user_id(self):
        return Config.TEST_USER_ID

    # Позитивный тест: успешное создание проекта через POST запрос
    def test_create_project_success(self, projects_page, test_user_id):
        project_data = {
            "title": "Test Project Lesson 8",
            "users": {test_user_id: "admin"}
        }

        # Отправка POST запроса на создание проекта
        response = projects_page.create_project(project_data)
        # Проверка что проект успешно создан (статус 201)
        assert response.status_code == 201
        # Получение данных из ответа
        response_data = response.json()
        # Проверка что в ответе присутствует ID созданного проекта
        assert "id" in response_data

    # Позитивный тест: успешное получение проекта через GET запрос
    def test_get_project_success(self, projects_page, test_user_id):
        # Подготовка данных для создания тестового проекта
        project_data = {
            "title": "Test Project for GET Method",
            "users": {test_user_id: "admin"}
        }
        # Создание проекта для последующего получения
        create_response = projects_page.create_project(project_data)
        # Извлечение ID созданного проекта из ответа
        project_id = create_response.json()["id"]

        # Отправка GET запроса для получения проекта по ID
        response = projects_page.get_project(project_id)
        # Проверка что проект успешно получен (статус 200)
        assert response.status_code == 200
        # Получение данных из ответа
        response_data = response.json()
        # Проверка что полученный проект имеет правильный ID
        assert response_data["id"] == project_id
        # Проверка что название проекта соответствует исходному
        assert response_data["title"] == project_data["title"]

    # Позитивный тест: успешное удаление проекта через PUT запрос
    def test_delete_project_success(self, projects_page, test_user_id):
        # Подготовка данных для создания тестового проекта
        project_data = {
            "title": "Test Project for DELETE Method",
            "users": {test_user_id: "admin"}
        }
        # Создание проекта для последующего удаления
        create_response = projects_page.create_project(project_data)
        # Извлечение ID созданного проекта из ответа
        project_id = create_response.json()["id"]

        # Подготовка данных для удаления проекта
        delete_data = {
            "deleted": True,  # Флаг удаления проекта
        }
        # Отправка PUT запроса для удаления проекта
        response = projects_page.update_project(project_id, delete_data)
        # Проверка что проект успешно удален (статус 200)
        assert response.status_code == 200
        # Получение данных из ответа
        response_data = response.json()
        # Проверка что в ответе вернулся ID удаленного проекта
        assert response_data["id"] == project_id

    # Негативный тест: попытка создания проекта без обязательного поля title
    def test_create_project_missing_title_fails(self, projects_page,
                                                test_user_id):
        # Подготовка невалидных данных (отсутствует обязательное поле title)
        invalid_data = {
            "users": {test_user_id: "admin"}  # Без названия
        }
        # Отправка POST запроса с невалидными данными
        response = projects_page.create_project(invalid_data)
        # Проверка что API возвращает ошибку (статус 400)
        assert response.status_code == 400

    # Негативный тест: попытка получения несуществующего проекта
    def test_get_project_invalid_id_fails(self, projects_page):
        # Использование заведомо несуществующего ID проекта
        invalid_project_id = "00000000-0000-0000-0000-000000000000"
        # Отправка GET запроса для получения несуществующего проекта
        response = projects_page.get_project(invalid_project_id)
        # Проверка что API возвращает ошибку "не найдено" (статус 404)
        assert response.status_code == 404

    # Негативный тест: попытка удаления несуществующего проекта
    def test_delete_project_invalid_id_fails(self, projects_page,
                                             test_user_id):
        # Использование заведомо несуществующего ID проекта
        invalid_project_id = "00000000-0000-0000-0000-000000000000"
        # Подготовка данных для удаления
        delete_data = {
            "deleted": True,
            "title": "Test Project",
            "users": {test_user_id: "admin"}
        }
        # Отправка PUT запроса для удаления несуществующего проекта
        response = projects_page.update_project(invalid_project_id,
                                                delete_data)
        # Проверка что API возвращает ошибку "не найдено" (статус 404)
        assert response.status_code == 404
