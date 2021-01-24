from django.shortcuts import render


def index(request):
    context = {'title': 'Soul Shop'}
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'Soul Products',
        'products': [
            {'name': 'Черный худи с монограммами adidas Originals', 'price': '6 090',
             'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни', 'pic': 'vendor/img/products/Adidas-hoodie.png'},
            {'name': 'Синяя куртка The North Face', 'price': '23 750',
             'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель',
             'pic': 'vendor/img/products/Blue-jacket-The-North-Face.png'},
            {'name': 'Кoричневый спортивный oversized-топ ASOS DESIGN', 'price': '3 390',
             'description': 'Материал с плюшевой текстурой. Удобный и мягкий',
             'pic': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png'},
            {'name': 'Черный рюкзак Nike Heritage', 'price': '2 340',
             'description': 'Плотная ткань. Легкий материал', 'pic': 'vendor/img/products/Black-Nike-Heritage-backpack.png'},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': '13 590',
             'description': 'Гладкий кожаный верх. Натуральный материал', 'pic': 'vendor/img/products/Black-Dr-Martens-shoes.png'},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': '2 890',
             'description': 'Легкая эластичная ткань сирсакер Фактурная ткань',
             'pic': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'}
        ]
    }
    return render(request, 'mainapp/products.html', context)

