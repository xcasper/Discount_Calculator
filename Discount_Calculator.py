class Discount_Calculator(object):

    def calculate(self, total, discount_amt, discount_type):
        if discount_type == 'percent':
            if discount_amt > 100:
                raise ValueError("Percentage Discount Cannot Exceed 100%")
            percentage_discount = float(discount_amt) / 100
            discount = float(total) * percentage_discount
            
        elif discount_type == 'absolute':
            if discount_amt > total:
                raise ValueError("Aboslute Discount Cannot Exceed Order Total.")
            discount = discount_amt

        else:
            raise ValueError("Invalid discount type")
        
        return discount
