from .locators.order_locators import Order

class UserData:
    RENTAL_PERIOD_DAY = Order.RENTAL_PERIOD_DAY
    RENTAL_PERIOD_TWO_DAYS = Order.RENTAL_PERIOD_TWO_DAYS
    RENTAL_PERIOD_THREE_DAYS = Order.RENTAL_PERIOD_THREE_DAYS
    RENTAL_PERIOD_FOUR_DAYS = Order.RENTAL_PERIOD_FOUR_DAYS
    RENTAL_PERIOD_FIVE_DAYS = Order.RENTAL_PERIOD_FIVE_DAYS
    RENTAL_PERIOD_SIX_DAYS = Order.RENTAL_PERIOD_SIX_DAYS
    RENTAL_PERIOD_SEVEN_DAYS = Order.RENTAL_PERIOD_SEVEN_DAYS
    COLOR_BLACK = Order.COLOR_BLACK
    COLOR_GREY = Order.COLOR_GREY

class UserData:
    USER1 = {
        "order1": {
            "name": "Евгения",
            "surname": "Козлова",
            "address": "Братьев Захаровых",
            "metro": "Белорусская",
            "telephon": "89991234567"
        },
        "order2": {
            "delivery": "24.06.2026",
            "period": Order.RENTAL_PERIOD_TWO_DAYS,    
            "color": Order.COLOR_GREY,
            "comment": "Тестовый комментарий"
        }
    }

    USER2 = {
        "order1": {
            "name": "Владимир",
            "surname": "Сергеевич",
            "address": "Улица Тестовская",
            "metro": "Тверская",
            "telephon": "89997654321"
        },
"order2": {
            "delivery": "29.07.2026",
            "period": Order.RENTAL_PERIOD_THREE_DAYS, 
            "color": Order.COLOR_BLACK,
            "comment": "Позвоните за 10 минут"
        }
    }


 
