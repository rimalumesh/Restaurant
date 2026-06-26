KITCHEN_STATIONS = {
    "hot_kitchen": {
        "name": "Hot Kitchen",
        "description": "Prepares curries, soups, dal bhat, thalis, and other cooked meals.",
    },
    "breakfast": {
        "name": "Breakfast Station",
        "description": "Prepares breakfast dishes such as sel roti and paratha.",
    },
    "momo": {
        "name": "Momo Station",
        "description": "Specialized station for steamed and fried momo.",
    },
    "grill": {
        "name": "Grill Station",
        "description": "Handles grilled and roasted dishes such as choila and sekuwa.",
    },
    "beverage_dessert": {
        "name": "Beverage & Dessert Station",
        "description": "Prepares beverages, desserts, and ready-to-serve cold items.",
    },
}


RESTAURANT_MENU_ITEMS = {
    "breakfast": [
        {
            "name": "Sel Roti",
            "price": 80,
            "priority": 3,
            "est_time": 12,
            "station": "breakfast",
        },
        {
            "name": "Aloo Tarkari",
            "price": 60,
            "priority": 2,
            "est_time": 10,
            "station": "breakfast",
        },
        {
            "name": "Chiura with Curd",
            "price": 120,
            "priority": 2,
            "est_time": 5,
            "station": "beverage_dessert",
        },
        {
            "name": "Anda Paratha",
            "price": 150,
            "priority": 3,
            "est_time": 15,
            "station": "breakfast",
        },
        {
            "name": "Gundruk Soup",
            "price": 100,
            "priority": 1,
            "est_time": 12,
            "station": "hot_kitchen",
        },
    ],

    "snacks": [
        {
            "name": "Buff Momo",
            "price": 180,
            "priority": 3,
            "est_time": 18,
            "station": "momo",
        },
        {
            "name": "Chicken Momo",
            "price": 220,
            "priority": 3,
            "est_time": 18,
            "station": "momo",
        },
        {
            "name": "Veg Momo",
            "price": 160,
            "priority": 2,
            "est_time": 15,
            "station": "momo",
        },
        {
            "name": "Chatamari",
            "price": 180,
            "priority": 2,
            "est_time": 12,
            "station": "hot_kitchen",
        },
        {
            "name": "Pakoda",
            "price": 120,
            "priority": 1,
            "est_time": 10,
            "station": "hot_kitchen",
        },
        {
            "name": "Choila",
            "price": 250,
            "priority": 3,
            "est_time": 15,
            "station": "grill",
        },
        {
            "name": "Sekuwa",
            "price": 300,
            "priority": 3,
            "est_time": 20,
            "station": "grill",
        },
        {
            "name": "Aloo Chop",
            "price": 100,
            "priority": 1,
            "est_time": 10,
            "station": "hot_kitchen",
        },
    ],

    "lunch": [
        {
            "name": "Veg Dal Bhat Tarkari",
            "price": 250,
            "priority": 2,
            "est_time": 18,
            "station": "hot_kitchen",
        },
        {
            "name": "Chicken Dal Bhat Tarkari",
            "price": 350,
            "priority": 3,
            "est_time": 20,
            "station": "hot_kitchen",
        },
        {
            "name": "Buff Dal Bhat Tarkari",
            "price": 330,
            "priority": 3,
            "est_time": 20,
            "station": "hot_kitchen",
        },
        {
            "name": "Mutton Dal Bhat Tarkari",
            "price": 450,
            "priority": 3,
            "est_time": 25,
            "station": "hot_kitchen",
        },
        {
            "name": "Thakali Khana Set",
            "price": 500,
            "priority": 3,
            "est_time": 25,
            "station": "hot_kitchen",
        },
    ],

    "dinner": [
        {
            "name": "Veg Thali Set",
            "price": 280,
            "priority": 2,
            "est_time": 18,
            "station": "hot_kitchen",
        },
        {
            "name": "Chicken Thali Set",
            "price": 380,
            "priority": 3,
            "est_time": 20,
            "station": "hot_kitchen",
        },
        {
            "name": "Buff Thali Set",
            "price": 360,
            "priority": 3,
            "est_time": 20,
            "station": "hot_kitchen",
        },
        {
            "name": "Mutton Thali Set",
            "price": 480,
            "priority": 3,
            "est_time": 25,
            "station": "hot_kitchen",
        },
        {
            "name": "Dhido Set",
            "price": 350,
            "priority": 2,
            "est_time": 20,
            "station": "hot_kitchen",
        },
    ],

    "drinks": {
        "hot": [
            {
                "name": "Milk Tea",
                "price": 40,
                "priority": 3,
                "est_time": 5,
                "station": "beverage_dessert",
            },
            {
                "name": "Black Tea",
                "price": 30,
                "priority": 1,
                "est_time": 3,
                "station": "beverage_dessert",
            },
            {
                "name": "Masala Tea",
                "price": 50,
                "priority": 3,
                "est_time": 6,
                "station": "beverage_dessert",
            },
            {
                "name": "Coffee",
                "price": 80,
                "priority": 2,
                "est_time": 5,
                "station": "beverage_dessert",
            },
        ],
        "cold": [
            {
                "name": "Lassi",
                "price": 120,
                "priority": 3,
                "est_time": 4,
                "station": "beverage_dessert",
            },
            {
                "name": "Fresh Lemon Soda",
                "price": 100,
                "priority": 2,
                "est_time": 3,
                "station": "beverage_dessert",
            },
            {
                "name": "Mineral Water",
                "price": 30,
                "priority": 1,
                "est_time": 1,
                "station": "beverage_dessert",
            },
            {
                "name": "Soft Drink",
                "price": 50,
                "priority": 1,
                "est_time": 1,
                "station": "beverage_dessert",
            },
        ],
    },

    "desserts": [
        {
            "name": "Juju Dhau",
            "price": 120,
            "priority": 3,
            "est_time": 2,
            "station": "beverage_dessert",
        },
        {
            "name": "Kheer",
            "price": 100,
            "priority": 2,
            "est_time": 3,
            "station": "beverage_dessert",
        },
        {
            "name": "Rasbari",
            "price": 80,
            "priority": 2,
            "est_time": 2,
            "station": "beverage_dessert",
        },
        {
            "name": "Lalmohan",
            "price": 80,
            "priority": 1,
            "est_time": 2,
            "station": "beverage_dessert",
        },
    ],
}