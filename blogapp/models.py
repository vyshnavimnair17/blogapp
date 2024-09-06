from django.db import models

# Create your models here.

'''class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)'''


class Category(models.Model):  # main table
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    synopsis = models.TextField(default="synopsis")
    image = models.ImageField(upload_to='', default=1)
    description = models.TextField(default="description")
    genre = models.CharField(max_length=255, default="genre")


class Current(models.Model):  # Currently Reading table under Category table
    cur_id = models.AutoField(primary_key=True)
    curr_read = models.ForeignKey(Category, on_delete=models.CASCADE)


class Review(models.Model):  # Book review table
    rev_id = models.AutoField(primary_key=True)
    review = models.ForeignKey(Category, on_delete=models.CASCADE)


class Wrapup(models.Model):  # Monthly wrapup table
    mon_id = models.AutoField(primary_key=True)
    month = models.ForeignKey(Category, on_delete=models.CASCADE)


class January(models.Model):  # january table under Monthly wrapup
    jan_id = models.AutoField(primary_key=True)
    january = models.ForeignKey(Wrapup, on_delete=models.CASCADE)


class February(models.Model):  # february table under Monthly wrapup
    feb_id = models.AutoField(primary_key=True)
    february = models.ForeignKey(Wrapup, on_delete=models.CASCADE)


class March(models.Model):  # march table under Monthly wrapup
    mar_id = models.AutoField(primary_key=True)
    march = models.ForeignKey(Wrapup, on_delete=models.CASCADE)


class April(models.Model):  # april table under Monthly wrapup
    apr_id = models.AutoField(primary_key=True)
    april = models.ForeignKey(Wrapup, on_delete=models.CASCADE)


class May(models.Model):  # may table under Monthly wrapup
    may_id = models.AutoField(primary_key=True)
    may_rev = models.ForeignKey(Wrapup, on_delete=models.CASCADE)


class June(models.Model):  # june table under Monthly wrapup
    jun_id = models.AutoField(primary_key=True)
    june = models.ForeignKey(Wrapup, on_delete=models.CASCADE)


class July(models.Model):  # july table under Monthly wrapup
    jul_id = models.AutoField(primary_key=True)
    july = models.ForeignKey(Wrapup, on_delete=models.CASCADE)


class August(models.Model):  # august table under Monthly wrapup
    aug_id = models.AutoField(primary_key=True)
    august = models.ForeignKey(Wrapup, on_delete=models.CASCADE)


class September(models.Model):  # september table under Monthly wrapup
    sept_id = models.AutoField(primary_key=True)
    september = models.ForeignKey(Wrapup, on_delete=models.CASCADE)


class October(models.Model):  # october table under Monthly wrapup
    octo_id = models.AutoField(primary_key=True)
    october = models.ForeignKey(Wrapup, on_delete=models.CASCADE)


class November(models.Model):  # november table under Monthly wrapup
    nov_id = models.AutoField(primary_key=True)
    november = models.ForeignKey(Wrapup, on_delete=models.CASCADE)


class December(models.Model):  # december table under Monthly wrapup
    dec_id = models.AutoField(primary_key=True)
    december = models.ForeignKey(Wrapup, on_delete=models.CASCADE)


class Favourite(models.Model):  # 2023 favourites table
    fav_id = models.AutoField(primary_key=True)
    favourite = models.ForeignKey(Category, on_delete=models.CASCADE)


class Recommendation(models.Model):  # recommendations table
    rec_id = models.AutoField(primary_key=True)
    recommend = models.ForeignKey(Category, on_delete=models.CASCADE)


class Tbr(models.Model):  # TBR list table
    tbr_id = models.AutoField(primary_key=True)
    toread = models.ForeignKey(Category, on_delete=models.CASCADE)


class Meta:
    db_table = "blogtable"
