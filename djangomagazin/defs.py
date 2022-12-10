links_menu = [
        {'href': 'main', 'name': 'главная'},
        {'href': 'products:index', 'name': 'продукты'},
        {'href': 'contacts', 'name': 'контакты'},
]
group_permissions = ['Users', 'Stuff', 'Admins']
test_users = [
        ("Admin_viewer", 2),
        ("Searcher_viewer", 1),
        ("Random_viewer", 0)
]

admin_links = [
        (('Создать ', 'create'),
         (('users', 'нового пользователя'),
          ('categories', 'новую категорию'),
          ('products', 'новый товар'),
          ('basket', 'новую корзину'))),
        # (('Просмотр ', 'read'),
        #  (('users', 'пользователя'),
        #   ('categories', 'категории'),
        #   ('products', 'товара'),
        #   ('baskets', 'корзины'))),
        # (('Изменить ', 'update'),
        #  (('users', 'пользователя'),
        #   ('categories', 'категорию'),
        #   ('products', 'товар'),
        #   ('baskets', 'корзину'))),
        # (('Удалить ', 'delete'),
        #  (('users', 'пользователя'),
        #   ('categories', 'категорию'),
        #   ('products', 'товар'),
        #   ('baskets', 'корзину'))),
]

admin_links_common = [
        ('users', 'Просмотр всех пользователей'),
        ('categories', 'Просмотр всех категорий'),
        ('products', 'Просмотр всех товаров'),
        ('basket', 'Просмотр всех корзин'),
]
