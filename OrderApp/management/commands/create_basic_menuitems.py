from django.core.management.base import BaseCommand

from OrderApp.models import Catagory, MenuItem
from OrderApp.data.basic_menu_items import RESTAURANT_MENU_ITEMS


class Command(BaseCommand):
    help = "Populate restaurant menu categories and items"

    def handle(self, *args, **options):

        categories_created = 0
        items_created = 0

        for category_name, items in RESTAURANT_MENU_ITEMS.items():

            # Handles:
            # breakfast, snacks, lunch, dinner, desserts
            if isinstance(items, list):

                categories = {
                    category_name.title(): items
                }

            # Handles:
            # drinks -> hot, cold
            elif isinstance(items, dict):

                categories = {
                    f"{category_name.title()}-{subcategory_name.title()}": sub_items
                    for subcategory_name, sub_items in items.items()
                }

            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Skipping invalid category: {category_name}"
                    )
                )
                continue

            for category_label, menu_items in categories.items():

                category, category_created = Catagory.objects.get_or_create(
                    name=category_label
                )

                if category_created:
                    categories_created += 1

                for item in menu_items:

                    _, item_created = MenuItem.objects.update_or_create(
                        category=category,
                        name=item["name"],
                        defaults={
                            "price": item["price"],
                            "description": item.get("description", "")
                        }
                    )

                    if item_created:
                        items_created += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"""
Menu seeded successfully.

Categories created: {categories_created}
Menu items created: {items_created}
                """
            )
        )