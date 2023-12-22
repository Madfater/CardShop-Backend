import mysql as sql
# 查購物車
def GetCart(data:dict):
    cmd = f'''select sc.ID,Price,sc.Status,sc.Quantity,sc.ACCard_ID,sc.Store_ID
    from StoreCard sc
    inner join Cart_to_Card_Table cctable ON cctable.Card_ID = sc.ID
    inner join Shopping_Cart scart ON scart.ID = cctable.Cart_ID
    where scart.ID = {data['User_ID']}'''
    cmd += f" Limit {(data['page']-1)*data['pageLimit']},{data['pageLimit']}"
    return sql.command(cmd)

# 加入Store card到 shopping cart
def AddCardToCart(data:dict):
    id = sql.getMaxId("Cart_to_Card_Table") + 1
    cart_to_card_arg = [id, data['Cart_ID'],data['Card_id']]
    sql.command(sql.insert("Cart_to_Card_Table",cart_to_card_arg))
    return "added"