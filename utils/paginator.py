# coding=utf-8
from abc import ABC

from discord.ext import menus


class PaginatorSource(menus.ListPageSource, ABC):
    def __init__(self, data, *args, **kwargs):
        super().__init__(data, *args, per_page=1, **kwargs)

    async def format_page(self, menu: menus.Menu, entries):
        offset = menu.current_page * self.per_page
        return '\n'.join(f'{i}. {v}' for i, v in enumerate(entries, start=offset))


async def create_menu(data):
    """
    Constructs a menu that can be started with .start(ctx)
    :param data: Data for the menu to contain.
    :return: Menu
    """
    pages = menus.MenuPages(source=PaginatorSource(data), timeout=300,
                            clear_reactions_after=True, check_embeds=True)
    return pages
