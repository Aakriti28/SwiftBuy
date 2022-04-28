# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import ( BaseUserManager, AbstractBaseUser)
from django.contrib.auth.models import PermissionsMixin

class Addmoney(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    payment = models.ForeignKey('Paymentgateway', models.DO_NOTHING, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'addmoney'


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)

#     class Meta:
        
#         db_table = 'auth_group'


# class AuthGroupPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

#     class Meta:
        
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)


# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)

#     class Meta:
        
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.BooleanField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.BooleanField()
#     is_active = models.BooleanField()
#     date_joined = models.DateTimeField()

#     class Meta:
        
#         db_table = 'auth_user'


# class AuthUserGroups(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

#     class Meta:
        
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)


# class AuthUserUserPermissions(models.Model):
    # id = models.BigAutoField(primary_key=True)
    # user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    # permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    # class Meta:
        
    #     db_table = 'auth_user_user_permissions'
    #     unique_together = (('user', 'permission'),)


class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    brand_desc = models.TextField(blank=True, null=True)

    class Meta:
        
        db_table = 'brand'


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    category_desc = models.TextField(blank=True, null=True)

    class Meta:
        
        db_table = 'category'


# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.SmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)

#     class Meta:
        
#         db_table = 'django_admin_log'


# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)

#     class Meta:
        
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)


# class DjangoMigrations(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
        
#         db_table = 'django_migrations'


# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()

#     class Meta:
        
#         db_table = 'django_session'


class Incart(models.Model):
    buyer = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'incart'
        unique_together = (('buyer', 'product'),)


class Notification(models.Model):
    notif_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    seen = models.IntegerField(blank=True, null=True)
    notif_text = models.TextField(blank=True, null=True)
    notif_timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        
        db_table = 'notification'


class Orders(models.Model):
    order_id = models.TextField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    payment = models.ForeignKey('Paymentgateway', models.DO_NOTHING, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    trasaction_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        
        db_table = 'orders'


class Paymentgateway(models.Model):
    payment_id = models.IntegerField(primary_key=True)
    method_name = models.TextField(blank=True, null=True)

    class Meta:
        
        db_table = 'paymentgateway'


class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)
    brand = models.ForeignKey(Brand, models.DO_NOTHING, blank=True, null=True)
    seller = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    advertised = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    product_desc = models.TextField(blank=True, null=True)
    quantity_available = models.IntegerField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    images = models.TextField(blank=True, null=True)

    class Meta:
        
        db_table = 'product'


class Referral(models.Model):
    giver = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    taker = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True, related_name='+')

    class Meta:
        
        db_table = 'referral'


class Review(models.Model):
    product = models.ForeignKey(Product, models.DO_NOTHING)
    buyer = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True)
    rating = models.IntegerField(blank=True, null=True)
    review_text = models.TextField(blank=True, null=True)

    class Meta:
        
        db_table = 'review'
        unique_together = (('buyer', 'product'),)


class Transaction(models.Model):
    seller = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True)
    buyer = models.ForeignKey('Users', models.DO_NOTHING, related_name='+')
    product = models.ForeignKey(Product, models.DO_NOTHING)
    order = models.ForeignKey(Orders, models.DO_NOTHING)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'transaction'
        unique_together = (('seller', 'buyer', 'product', 'order'),)

class UserManager(BaseUserManager):
    def create_user(self, params, password='admin'):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not params['email']:
            raise ValueError('Users must have an email address')

        user = self.model(
            email = UserManager.normalize_email(params['email']),
            name = params['name'],
            phone = params['phone'],
            address = params['address'],
            shipping_address = params['shipping_address'],
            referral_token = params['referral_token'],
            wallet_amount = params['wallet_amount'],
        )

        user.set_password(params['password'])
        # user.set_password(password)
        user.save(using=self._db)
        return user

class Users(AbstractBaseUser):
    uid = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    shipping_address = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True, unique=True)
    password = models.TextField(blank=True, null=True)
    wallet_amount = models.IntegerField(blank=True, null=True)
    referral_token = models.TextField(blank=True, null=True)
    role = models.TextField(blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        
        db_table = 'users'

    @property
    def is_anonymous(self):
        """
        Always return False. This is a way of comparing User objects to
        anonymous users.
        """
        return False

    @property
    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True



class Wishlist(models.Model):
    buyer = models.OneToOneField(Users, models.DO_NOTHING, primary_key=True)
    product = models.ForeignKey(Product, models.DO_NOTHING)

    class Meta:
        
        db_table = 'wishlist'
        unique_together = (('buyer', 'product'),)






