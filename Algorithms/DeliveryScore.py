# calculates delivery score of supplier


def delivery_score(supplier, client):
    score = 1.0
    # estimated delivery time in days
    supplier_time = supplier.delivery_time
    client_time = client.delivery_time
    # if supplier delivery time is less than client preferred delivery time return perfect score
    if supplier_time <= client_time:
        return score
    # else penalize supplier's score by 0.2 times number of days over
    else:
        if supplier_time - client_time > 5:
            return 0
        else:
            return score - 0.2(supplier_time - client_time)
