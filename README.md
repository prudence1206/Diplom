# ZDV_Diploma_DRF_backend
# Дипломная работа к профессии Python-разработчик «API Сервис заказа товаров для розничных сетей».

## Описание

Приложение предназначено для автоматизации закупок в розничной сети. Пользователи сервиса — покупатель (менеджер торговой сети, который закупает товары для продажи в магазине) и поставщик товаров.

**Клиент (покупатель):**

- Менеджер закупок через API делает ежедневные закупки по каталогу, в котором
  представлены товары от нескольких поставщиков.
- В одном заказе можно указать товары от разных поставщиков — это
  повлияет на стоимость доставки.
- Пользователь может авторизироваться, регистрироваться и восстанавливать пароль через API.
    
**Поставщик:**

- Через API информирует сервис об обновлении прайса.
- Может включать и отключать прием заказов.
- Может получать список оформленных заказов (с товарами из его прайса).


### Задача

Необходимо разработать backend-часть (Django) сервиса заказа товаров для розничных сетей.

**Базовая часть:**
* Разработка сервиса под готовую спецификацию (API);
* Возможность добавления настраиваемых полей (характеристик) товаров;
* Импорт товаров;
* Отправка накладной на email администратора (для исполнения заказа);
* Отправка заказа на email клиента (подтверждение приема заказа).

**Продвинутая часть:**
* Экспорт товаров;
* Админка заказов (проставление статуса заказа и уведомление клиента);
* Выделение медленных методов в отдельные процессы (email, импорт, экспорт).

### Исходные данные
 
1. Общее описание сервиса
1. [Спецификация (API) - 1 шт.](./reference/screens.md)
1. [Файлы yaml для импорта товаров - 1 шт.](./data/shop1.yaml)
1. [Пример API Сервиса для магазина](./reference//netology_pd_diplom/) 

## Этапы разработки

Разработку Backend рекомендуется разделить на следующие этапы:

Базовая часть:
1. [Создание и настройка проекта](./reference/step-1.md)
2. [Проработка моделей данных](./reference/step-2.md)
3. [Реализация импорта товаров](./reference/step-3.md)
4. [Реализация API views](./reference/step-4.md)
5. [Полностью готовый backend](./reference/step-5.md)

Продвинутая часть (по желанию, если базовая часть полностью готова):

6. [Реализация forms и views админки склада](./reference/step-6-adv.md)
7. [Вынос медленных методов в задачи Celery](./reference/step-7-adv.md)
8. Создание docker-файла для приложения


Настоятельно рекомендуется вести разработку с использованием git (github/gitlab/bitbucket) с регулярными коммитами в репозиторий, доступный вашему дипломному руководителю. Старайтесь делать коммиты как можно чаще для того, чтобы иметь возможность оперативно получать обратную связь от руководителя проекта и избежать лишнего переписывания кода, если что-то потребует корректировки.

Разберём подробно каждый этап.

### Этап 1. Создание и настройка проекта

Критерии достижения:

1. Вы имеете актуальный код данного репозитория на рабочем компьютере;
2. У вас создан django-проект и он запускается без ошибок.

Для получения подробностей по данному этапу
[перейдите по ссылке](./reference/step-1.md).

### Этап 2. Проработка моделей данных

Критерии достижения:

1. Созданы модели и их дополнительные методы.

Для получения подробностей по данному этапу
[перейдите по ссылке](./reference/step-2.md).

### Этап 3. Реализация импорта товаров

Критерии достижения:

1. Созданы функции загрузки товаров из приложенных файлов в модели Django.
2. Загружены товары из всех файлов для импорта.

Для получения подробностей по данному этапу
[перейдите по ссылке](./reference/step-3.md).

### Этап 4. Реализация forms и views

Критерии достижения:

1. Реализованы API Views для основных [страниц](./reference/screens.md) сервиса (без админки):
   - Вход
   - Регистрация
   - Список товаров
   - Карточка товара
   - Корзина
   - Подтверждение заказа
   - Спасибо за заказ
   - Заказы
   - Заказ

Для получения подробностей по данному этапу
[перейдите по ссылке](./reference/step-4.md).

### Этап 5. Полностью готовый backend

Критерии достижения:

1. Полностью работающие API Endpoint
2. Корректно отрабатывает следующий сценарий:
   - пользователь может авторизироваться;
   - есть возможность отправки данных для регистрации и получения email с подтверждением регистрации;
   - пользователь может добавлять в корзину товары от разных магазинов;
   - пользователь может подтверждать заказ с вводом адреса доставки;
   - пользователь получает email с подтверждением после ввода адреса доставки;
   - Пользователь может переходить на страницу "Заказы" и открывать созданный заказ.

Для получения подробностей по данному этапу
[перейдите по ссылке](./reference/step-5.md).

## Полезные материалы

1. [Информация о сервисе](./reference/service.md)
2. [Спецификация API](./reference/api.md)
3. [Описание страниц сервиса](./reference/screens.md)


---

## Продвинутая часть (по желанию)

Обязательное условие: Базовая часть полностью готова.

### Этап 6. Реализация API views админки склада

Критерии достижения:

1. Реализованы API views для [страниц админки](./reference/screens.md) сервиса.


Для получения подробностей по данному этапу
[перейдите по ссылке](reference/step-6-adv.md).

### Этап 7. Вынос медленных методов в задачи Celery

Критерии достижения:

1. Создано Celery-приложение c методами:
   - send_email
   - do_import
2. Создан view для запуска Celery-задачи do_import из админки.

Для получения подробностей по данному этапу
[перейдите по ссылке](reference/step-7-adv.md).  


### Этап 8. Создание docker-файла для приложения
1. Создать docker-файл для сборки приложения.
2. Предоставить инструкцию для сборки docker-образа.
3. Создать docker-compose файл для развертывания приложения локально (с БД и необходимыми сервисами)
