from datetime import datetime

from peewee import CharField, DateTimeField, ForeignKeyField, IntegerField, BooleanField

from app import db


class User(db.Model):
    username = CharField()
    password = CharField()
    is_admin = BooleanField()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __unicode__(self):
        return self.username


class Supplier(db.Model):
    name = CharField()
    address = CharField(null=True)
    contact = CharField(null=True)

    def __unicode__(self):
        return self.name


class Customer(db.Model):
    name = CharField()
    address = CharField(null=True)
    contact = CharField(null=True)

    def __unicode__(self):
        return self.name


class Item(db.Model):
    # TODO make it positive integer
    barcode = CharField(unique=True)
    name = CharField()
    stock = IntegerField(default=0)
    price_buy = IntegerField(default=0)
    price_sell = IntegerField(default=0)
    supplier = ForeignKeyField(Supplier, null=True)

    def __unicode__(self):
        return '%s (Stok: %s)' % (self.name, self.stock)


class PurchaseInvoice(db.Model):
    code = CharField(primary_key=True)
    created_at = DateTimeField(default=datetime.now)

    def __unicode__(self):
        return self.created_at


class PurchaseInvoiceDetail(db.Model):
    purchase_invoice = ForeignKeyField(PurchaseInvoice, related_name='related_to', null=True)
    item = ForeignKeyField(Item, related_name='items', null=True)


class SalesInvoice(db.Model):
    code = CharField(primary_key=True)
    created_at = DateTimeField(default=datetime.now)
    discount = IntegerField(default=0)

    def __unicode__(self):
        return self.created_at


class SalesInvoiceDetail(db.Model):
    sales_invoice = ForeignKeyField(SalesInvoice, related_name='related_to', null=True)
    item = ForeignKeyField(Item, related_name='items', null=True)


def seed_table():
    User.create_table(True)
    Item.create_table(True)
    Supplier.create_table(True)
    Customer.create_table(True)
    PurchaseInvoice.create_table(True)
    PurchaseInvoiceDetail.create_table(True)
    SalesInvoice.create_table(True)
    SalesInvoiceDetail.create_table(True)