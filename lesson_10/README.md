# Проект автотестов Lesson 10

## Описание
Проект содержит два автотеста с использованием Selenium WebDriver и Allure для отчетности:

1. **Calculator** - тестирование медленного калькулятора
2. **Online_store** - тестирование полного цикла покупки в интернет-магазине

## Установка зависимостей

```bash
pip install -r requirements.txt
```


## Запуск всех тестов:
Из корня lesson_10
```bash
pytest lesson_10 --alluredir=allure-results
```

## Генерация и просмотр отчета:
```bash
allure serve allure-results
```