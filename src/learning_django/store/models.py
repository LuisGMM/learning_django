from django.db import models

# Create your models here.


class Promotion(models.Model):

    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Collection(models.Model):

    featured_product = models.ForeignKey('Product', related_name='+', on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


    class Meta:
        ordering = ['title']


class Product(models.Model):

    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)

    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)

    def __str__(self) -> str:
        return self.title


    class Meta:
        ordering = ['title']


class Customer(models.Model):

    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = (
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)


    # class Meta:
    #     db_table = 'store_customers'
    #     indexes = [
    #         models.Index(fields=['last_name', 'first_name'])
    #     ]


class Address(models.Model):

    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Order(models.Model):

    PENDING = 'P'
    COMPLETE = 'C'
    FAILED = 'F'

    PAYMENT_STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (COMPLETE, 'Complete'),
        (FAILED, 'Failed')
    )

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PENDING)


class OrderItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Cart(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.PositiveSmallIntegerField()
