class Discount_Calculator(object):

    def calculate(self, total, discount_amt, discount_type):
        if discount_type == 'percent':
            percentage_discount = float(discount_amt) / 100
            discount = float(total) * percentage_discount
            return discount
        elif discount_type == 'absolute':
            print "Total discount is: ", discount_amt
            return total - discount_amt
