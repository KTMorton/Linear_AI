from point_line_creator import create_points_from_line

data_set = create_points_from_line(1.2, 3.3, 150, 2)

class Linear_Classificatoin():
    
    def __init__(self, data_set):
        self.data_set = data_set
        

    def find_cost_func(self, m, b):
        total = 0
        for data in self.data_set:
            x = data[0]
            y = data[1]
            total += self.cost_func(x, y, m, b)
        average = total / len(self.data_set)
        print(average)
        return average

    def cost_func(self, x, y, m, b):
        result = (y - (x * m + b))**2
        # print(result)
        return result

    def update_weights_step(self, learning_rate, m_current, b_current):
        m_gradient = 0
        b_gradient = 0
        for data in self.data_set:
            x = data[0]
            y = data[1]
            m_gradient += -(2/len(self.data_set)) * x * (y - ((m_current*x) + b_current))
            b_gradient += -(2/len(self.data_set)) * (y - ((m_current*x) + b_current))
        new_m = m_current - (m_gradient * learning_rate)
        new_b = b_current - (b_gradient * learning_rate)
        return (new_m, new_b)
    
    def run(self, learning_rate, epochs, starting_m, starting_b):
        m = starting_m
        b = starting_b
        for i in range(epochs):
            if (i % (epochs / 10)) == 0:
                print(str((i/epochs)*100) + "%")
                print("M: %s || B: %s" % (m, b))
            # print(self.find_cost_func(m, b))
            new_bm = self.update_weights_step(learning_rate, m, b)
            m = new_bm[0]
            b = new_bm[1]
        print("M: %s || B: %s" % (m, b))
        
ln = Linear_Classificatoin(data_set)
ln.run(0.0001, 50000, 0, 0)


