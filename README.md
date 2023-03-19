# Тестовый проект по автоматизации API

___

## Запуск тестов

1. Для просмотра результатов в консоли:

   `pytest -s -v`

2. Для формирования отчета Allure и просмотра в виде веб-страницы
   (Доступно если в системе установлен Allure [Подробнее](https://docs.qameta.io/allure-report/#_installing_a_commandline)):

      `python -m pytest --alluredir=test_results/ tests/test_google_maps_api.py`

      `allure serve test_results`
