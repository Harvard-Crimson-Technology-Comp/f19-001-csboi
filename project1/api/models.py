from django.db import models

# TODO: you'll need to fill in the models that you create here!

# a class containing what happened in a purchase (who made it, when it was made, what it traded)
class PurchaseModel(models.Model):
    class Meta:
        app_label = 'api'
        timestamp = models.DateTimeField()
        user = models.ForeignKey(
            'UserModel',
            on_delete=modles.CASCADE
        )
        symbol = models.CharField()
        price = models.FlaotField()
        quantity = models.IntegerField()


# the class containing your user information (including their api token and password, etc)
class UserModel(models.Model):
    class Meta:
        app_label = 'api'
        first_name = models.CharField()
        last_name = models.CharField()
        api_id = models.UUIDField()
        password = models.CharField() # Assuming it has already been hashed
        username = modesl.PrimaryKey()
        portfolio = models.OnetoOnefield(
            PortfolioModel,
            on_delete=modles.CASCADE

        )
# the class containing a portfolio of stocks
class PortfolioModel(models.Model):
    class Meta:
        app_label = 'api'
        cash = models.FloatField()
        portfolio = models.ForeignKey(
            'UserModel',
            on_delete=modles.CASCADE
        )

# a class containing a simple set of data on a stock within a portfolio
class StockModel(models.Model):
    class Meta:
        portfolio = models.ForeignKey(
            'Portfiolio',
            on_delete=modles.CASCADE
        )
        app_label = 'api'
        symbol = models.CharField()
        quantity = models.IntegerField()
