from django.db.models import Sum, Count
from .models import Category

def get_top_categories():
    """
    Retrieve the top 5 categories with highest total product price.
    
    Returns:
    List[Dict]: A list of dictionaries containing:
        - category_name: str
        - total_price: Decimal
        - product_count: int
    """
    return (
        Category.objects
        .annotate(
            total_price=Sum('product__price'),
            product_count=Count('product')
        )
        .filter(product_count__gt=0)  # Exclude categories without products
        .values(
            'name',
            'total_price',
            'product_count'
        )
        .order_by('-total_price')  # Sort by total price descending
        .all()[:5]  # Limit to top 5
    ).values(
        category_name=F('name'),
        total_price=F('total_price'),
        product_count=F('product_count')
    )

# Example usage
top_categories = get_top_categories()

# Print results
for category in top_categories:
    print({
        'category_name': category['category_name'],
        'total_price': float(category['total_price']),  # Convert Decimal to float for display
        'product_count': category['product_count']
    })

# Create test data
electronics = Category.objects.create(name='Electronics')
books = Category.objects.create(name='Books')

# Create some products
Product.objects.create(title='Laptop', price=1000.00, category=electronics)
Product.objects.create(title='Phone', price=500.50, category=electronics)
Product.objects.create(title='Book 1', price=20.00, category=books)
Product.objects.create(title='Book 2', price=30.00, category=books)

# Run the query
results = get_top_categories()