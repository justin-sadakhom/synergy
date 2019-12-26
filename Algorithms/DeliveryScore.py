# calculates delivery score of supplier
def deliveryScore(supplier, client):
    score = 1.0
    # estimated delivery time in days
    supplierTime = supplier.delivery_time
    clientTime = client.delivery_time
    # if supplier delivery time is less than client preferred delivery time return perfect score
    if supplierTime <= clientTime:
        return score
    # else peanalise supplier's score by 0.2 times number of days over
    else:
        if (supplierTime - clientTime > 5):
            return 0
        else:
            return (score - 0.2(supplierTime - clientTime))
