def save_transaction(price,credit_card,desc):
    file=open("transactions.txt","a")
    file.write("%07d%16s%16s\n"%(price * 100,credit_card,desc))
    file.close()
