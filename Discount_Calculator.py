class Discount_Calculator(object):

    def calculate(self, total, discount_amt, discount_type):
        if discount_type == 'percent':
            percentage_discount = float(discount_amt) / 100
            discount = float(total) * percentage_discount
            
        elif discount_type == 'absolute':
            discount = discount_amt

        else:
            raise ValueError("Invalid discount type")
        
        return discount
