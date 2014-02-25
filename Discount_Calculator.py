class Discount_Calculator(object):

    def calculate(self, total, discount_amt, discount_type):
        if discount_type == 'percent':
            print "Total discount is: ", (total * (discount_amt/100))
            return 10
        elif discount_type == 'absolute':
            print "Total discount is: ", discount_amt
            return total - discount_amt
        
