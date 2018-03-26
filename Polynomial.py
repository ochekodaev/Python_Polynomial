class Polynomial(object):
    def __init__(self, coeffs):
        if not isinstance(coeffs, list):
            raise TypeError("coeffs has a wrong type!")
        elif len(coeffs) == 0:
            raise TypeError("Empty coefficients list!")
        else:
            for i in range(len(coeffs)):
                if not (isinstance(coeffs[i], int) or isinstance(coeffs[i], float)):
                    raise TypeError("One or more coefficients has a wrong type!")

            coeffs_copy = coeffs[:]
            for i in range(len(coeffs)):
                if coeffs[i] == 0:
                    if i != len(coeffs) - 1:
                        del coeffs_copy[0]
                else:
                    break
            self.coeffs = coeffs_copy[:]


    @property
    def degree(self):
        return len(self.coeffs) - 1


    def __eq__(self, other):
        if isinstance(other, Polynomial):
            return self.coeffs == other.coeffs
        elif not (isinstance(other, int) or isinstance(other, float)):
            raise TypeError("Wrong type!")
        else:
            return len(self.coeffs) == 1 and self.coeffs[0] == other


    def __add__(self, other):
        if isinstance(other, Polynomial):
            if self.degree > other.degree:
                sum = self.coeffs[:]
                for i in range(len(other.coeffs)):
                    sum[i + (self.degree - other.degree)] += other.coeffs[i]
            else:
                sum = other.coeffs[:]
                for i in range(len(self.coeffs)):
                    sum[i + (other.degree - self.degree)] += self.coeffs[i]
        elif isinstance(other, int) or isinstance(other, float):
            sum = self.coeffs[:]
            sum[-1] += other
        else:
            raise TypeError("Wrong type!")

        return Polynomial(sum)


    def __radd__(self, other):
        return self + other


    def __mul__(self, other):
        if isinstance(other, Polynomial):
            mult = [0] * (self.degree + other.degree + 1)
            for i, self_coef in enumerate(self.coeffs):
                for j, other_coef in enumerate(other.coeffs):
                    mult[i + j] += self_coef * other_coef
        elif isinstance(other, int) or isinstance(other, float):
            mult = [coef * other for coef in self.coeffs]
        else:
            raise TypeError("Wrong type!")

        return Polynomial(mult)



    def __rmul__(self, other):
        return self * other



    def __str__(self):
        res = ""
        if self.degree == 0:
            res = str(self.coeffs[0])
        else:
            for i, coef in enumerate(self.coeffs):
                if coef != 0:
                    if coef < 0:
                        res += "-"
                    else:
                        if i != 0:
                            res += "+"							

                    if abs(coef) != 1:
                        res += str(abs(coef))
                    else:
                        if i == self.degree:
                            res += str(abs(coef))

                    if i != self.degree:
                        res += "x"
                        if i != self.degree - 1:					
                            res += str(self.degree - i)

        return res