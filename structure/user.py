import mysql as sql
from datetime import datetime

# 資料輸入順序
User_order = ["email","username","password"]

# 註冊User
def Register(data:dict):
    if sql.countTable(f"User where Email = '{data['email']}'") != 0:
        return "User already exist"
    id = sql.getMaxId("User") + 1
    User_arg = [id]+[data[k] for k in User_order]+[0]+[id]*2
    store_arg = [id,"empty","empty",str(datetime.today().date())]
    shopping_cart_arg = [id]
    sql.command(sql.insert("Store",store_arg))
    sql.command(sql.insert("Shopping_Cart",shopping_cart_arg))
    sql.command(sql.insert("User",User_arg))
    return "register success"

# 登陸User
def Login(data:dict):
    if sql.countTable(f"User where Email = '{data['email']}'") == 0:
        return "this email isn't register yet"
    cmd = "Select Password from User where Email = "+ f"'{data['email']}'"
    acuratePassword = sql.command(cmd)[0][0]
    id = sql.command("Select ID from User where Email = "+ f"'{data['email']}'")[0][0]
    return id if data['password'] == acuratePassword else "login failed"

# get user name from id
def GetName(userId:int):
    if sql.countTable(f"User where ID = '{userId}'") == 0:
        return "User not found"
    cmd = f"Select User_Name from User where ID = {userId}"
    return sql.command(cmd)[0][0]