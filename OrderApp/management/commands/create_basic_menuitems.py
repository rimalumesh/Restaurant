from django.core.management.base import BaseCommand

from OrderApp.models import Catagory, MenuItem, KitchenStation
from OrderApp.data.basic_menu_items import (
    RESTAURANT_MENU_ITEMS,
    KITCHEN_STATIONS,
)


class Command(BaseCommand):
    help = "Populate restaurant menu categories, kitchen stations and menu items"

    def handle(self, *args, **options):

        categories_created = 0
        stations_created = 0
        items_created = 0

        # -------------------------
        # Seed Kitchen Stations
        # -------------------------
        stations = {}

        for code, data in KITCHEN_STATIONS.items():
            station, created = KitchenStation.objects.update_or_create(
                code=code,
                defaults={
                    "name": data["name"],
                    "description": data["description"],
                },
            )

            stations[code] = station

            if created:
                stations_created += 1

        # -------------------------
        # Seed Categories & Menu
        # -------------------------
        for category_name, items in RESTAURANT_MENU_ITEMS.items():

            if isinstance(items, list):
                categories = {
                    category_name.title(): items
                }

            elif isinstance(items, dict):
                categories = {
                    f"{category_name.title()}-{subcategory.title()}": sub_items
                    for subcategory, sub_items in items.items()
                }

            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Skipping invalid category: {category_name}"
                    )
                )
                continue

            for category_label, menu_items in categories.items():

                category, created = Catagory.objects.get_or_create(
                    name=category_label
                )

                if created:
                    categories_created += 1

                for item in menu_items:

                    _, created = MenuItem.objects.update_or_create(
                        category=category,
                        name=item["name"],
                        defaults={
                            "price": item["price"],
                            "default_priority": item["priority"],
                            "description": item.get("description", ""),
                            "est_time": item["est_time"],
                            "station": stations[item["station"]],
                        },
                    )

                    if created:
                        items_created += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"""
Restaurant seeded successfully.

Kitchen stations created: {stations_created}
Categories created: {categories_created}
Menu items created: {items_created}
"""
            )
        )