import peewee
from config import db_name, user, host, password_db

database = peewee.PostgresqlDatabase(db_name, user=user, host=host, password=password_db)


class User(peewee.Model):
    class Meta:
        database = database

    user_id = peewee.IntegerField(unique=True)
    time = peewee.IntegerField(default=10800)
    sort = peewee.CharField(default="Время", max_length=20)
    display = peewee.CharField(default="Фото", max_length=20)
    scens = peewee.CharField(default="kontroler", max_length=20)


User.create_table(True)
