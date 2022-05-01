import math
import matplotlib.pyplot as plt

class Fibonacci():
    # exact ratio 
    exact_next = (math.sqrt(5) + 1) / 2
    exact_prev = (math.sqrt(5) - 1) / 2
    
    def fibonacci(self,n, cache={}):
        if n in cache:
            ans = cache[n]
        elif n <= 2:
            ans = 1
            cache[n] = ans
        else:
            ans = self.fibonacci(self,n - 2) + self.fibonacci(self,n - 1)
            cache[n] = ans

        return ans


    # get next and previous value
    def next_num(self,n):
        return n * self.exact_next

    def previous_num(self,n):
        return n * self.exact_prev

    # get value between two postions
    def between_val(prev, after):
        try:
            return math.sqrt(prev * after)
        except:
            pass

    # get certain amount of either previous or following values in the sequence
    # direction = 1 -> get next vals, direction = 0 -> get prev vals
    def get_neighbor_vals(self, n, amount, direction):
        vals = []
        for i in range(1, amount + 1):
            if direction == 1:
                n = n * self.exact_next
            elif direction == 0:
                n = n * self.exact_prev
            vals.append(n)
        else:
            return vals

    # visualize in graph
    def visualize(self, amount):
        vals = []
        for i in range(1, amount + 1):
            n = self.fibonacci(self, i)
            vals.append(n)
        else:
            plt.plot(vals, 'bo', vals, 'k')
            plt.show()

