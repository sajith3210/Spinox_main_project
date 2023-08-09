from django.db import models

# Create your models here.
class AdminTable(models.Model):
    username=models.CharField(max_length=20)
    password=models.IntegerField()

class category_details(models.Model):
    category_ID=models.AutoField(primary_key=True)
    category_name=models.CharField(max_length=20)
    category_description=models.CharField(max_length=30)

    def __str__(self):
        return self.category_name



class user(models.Model):
    user_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    username=models.CharField(max_length=10)
    date_of_birth=models.DateTimeField()
    adress=models.CharField(max_length=30)
    email=models.CharField(max_length=20)
    phone_number=models.IntegerField()
    password=models.CharField(max_length=10)
    

    
class SellerTable(models.Model):
    Seller_ID=models.AutoField(primary_key=True)
    sellername=models.CharField(max_length=20,db_column="sname")
    adress=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    phone_number=models.IntegerField()

    def __str__(self):
        return self.sellername
    class Meta:
        db_table="tb_seler"
   


class ProductTable(models.Model):
    Product_ID=models.AutoField(primary_key=True)
    quantity=models.IntegerField(default=0,null=True) 
    Product_name=models.CharField(max_length=20)
    product_image= models.ImageField(upload_to='product_image/',null=True,blank=True)
    price=models.IntegerField()
    category_ID=models.ForeignKey(category_details, on_delete=models.CASCADE)
    Seller_ID=models.ForeignKey(SellerTable,on_delete=models.CASCADE)
    
    @property
    def imageURL(self):
		    try:
			    url = self.product_image.url
		    except:
			    url = ''
		    return url



class cart(models.Model):
    Product_ID=models.ForeignKey(ProductTable,on_delete=models.CASCADE)        
    user_id=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    Quantity=models.IntegerField(default=0)
class orders(models.Model):
    user_ID=models.ForeignKey(user,on_delete=models.CASCADE)
    Product_ID=models.ForeignKey(ProductTable,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    TotalPrice=models.IntegerField()
    Order_date=models.DateTimeField()
    Expected_Delivery=models.DateTimeField()
    
   