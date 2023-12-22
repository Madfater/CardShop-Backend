import mysql as sql
# 取得order
def GetOrder(data:dict):
    cmd = f'''select sc.ID,Price,sc.Status,sc.Quantity,sc.ACCard_ID,sc.Store_ID
    from StoreCard sc
    inner join Order_to_Card_Table oc ON oc.Card_ID = sc.ID
    inner join Order_List o ON o.ID = oc.Order_ID
    where o.ID = {data['Order_id']}
    '''
    cmd += f" Limit {(data['page']-1)*data['pageLimit']},{data['pageLimit']}" #按照頁數、資料筆數取得資料
    return sql.command(cmd)

# 加入Store card到 order
def AddOrder(data:dict):
    Order_ID = sql.getMaxId("Order_List") + 1
    Total_Price = 0
    for i in data['Card_id_list']:
        id = sql.getMaxId("Order_to_Card_Table") + 1
        order_to_card_arg = [id, Order_ID,i[0],i[1]] # table_id,order_id,card_id,quantity
        sql.command(sql.insert("Order_to_Cart_Table",order_to_card_arg)) #新增 卡片對應 order 資料
        Total_Price += sql.command(f"select Price from StoreCard where ID = {i[0]}")[0][0] * i[1] #計算總價 price * quantity
    order_List_arg = [Order_ID,data['Address'],Total_Price,data['User_ID']]
    sql.command(sql.insert("Order_List",order_List_arg)) #新增 order 資料
    return "added"
