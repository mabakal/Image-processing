import numpy as np
import math as mt


class MomentC:

    def __init__(self):
        pass

    def momentpq(self, ib, p, q):
        """
        This function return de central moment of a binary image
        :param ib: This is binary image input
        :param p:order of x
        :param q:order of y
        :return: return a moment of order p and q
        """
        s = 0
        h, l = ib.shape
        for x in range(h):
            for y in range(l):
                s = s + (x ** p) * (y ** q) * ib[x, y]
        return s

    def momentpqC(self, ib, p, q):
        """
        This return a centralised momemnt
        :param ib: This is binary image input
        :param p: order of x
        :param q: order of y
        :return: return a centralised moment  of order p and q
        """
        mu = 0
        l, h = ib.shape
        x_ = self.momemtpq(ib, 1, 0) / self.momemtpq(ib, 0, 0)
        y_ = self.momemtpq(ib, 0, 1) / self.momemtpq(ib, 0, 0)
        for x in range(l):
            for y in range(h):
                mu = mu + (((x - x_) ** p) * ((y - y_) ** q)) * ib[x, y]
        return mu

    def alpha_pq(self, ib, p, q):
        """
        This function return a normalized central moment
        :param ib: This is binary image input
        :param p:order of x
        :param q:order of y
        :return: return a normalized moment  of order p and q
        """
        lambda_ = ((p + q + 1) / 2) + 1
        alpha = self.momentpqC(ib, p, q) / (self.momentpqC(ib, 0, 0) ** lambda_)
        return alpha

    def momenthu(self, ib):
        """

        :param ib:the binary image
        :return: return hu moment
        """
        phi = []
        a_0_2 = self.alpha_pq(ib, 0, 2)
        a_0_3 = self.alpha_pq(ib, 0, 3)
        a_1_1 = self.alpha_pq(ib, 1, 1)
        a_1_2 = self.alpha_pq(ib, 1, 2)
        a_2_0 = self.alpha_pq(ib, 2, 0)
        a_2_1 = self.alpha_pq(ib, 2, 1)
        a_3_0 = self.alpha_pq(ib, 3, 0)

        phi.append(a_2_0 - a_0_2)
        phi.append((a_2_0 - a_0_2) ** 2 + (4 * a_1_1) ** 2)
        phi.append((a_3_0 - a_1_2) ** 2 + (3 * a_1_2 - a_0_3) ** 2)
        phi.append((a_3_0 + a_1_2) ** 2 + (a_2_1 + a_0_3) ** 2)

        phi.append((a_3_0 - 3 * a_1_2) * (a_3_0 + a_1_2) * ((a_3_0 + a_1_2) ** 2 - 3 * (a_2_1 + a_0_3) ** 2) + (
                    3 * a_2_1 - a_0_3) * (a_2_1 + a_0_3) * (3 * (a_3_0 + a_1_2) ** 2 - ((a_2_1 + a_0_3) ** 2)))

        phi.append((a_2_0 - a_0_2) * ((a_3_0 + a_1_2) ** 2 - (a_2_1 + a_0_3) ** 2) + 4 * a_1_1 * (a_3_0 + a_1_2) * (
                    a_2_1 + a_0_3))

        phi.append((3 * a_2_1 - a_3_0) * (a_3_0 + a_1_2) * ((a_3_0 + a_1_2) ** 2 - 3 * ((a_2_1 + a_0_3) ** 2)) + (
                    3 * a_1_2 - a_0_3) * (a_2_1 + a_0_3) * ((3 * (a_3_0 + a_1_2) ** 2) - ((a_2_1 + a_0_3) ** 2)))
        return phi


class MomentT:
    I = np.random.normal(size=(20, 30), scale=1 / 5)
    M, N = I.shape

    def __init__(self):
        pass

    def rho(self, n, N):
        return mt.factorial((n + N)) / ((2 * n + 1) * mt.factorial(N - n - 1))

    def ak(self, a, k):
        answer = 1
        if k < 1:
            answer = 1
        else:
            for i in range(1, k):
                answer = answer * (answer + i - 1)
        return answer

    def t(self, n, x):
        answer = 0
        coef = self.ak(1 - self.M, n) / mt.sqrt(self.rho(n, self.M))
        for k in range(n + 1):
            answer = answer + coef * (
                        (self.ak(-n, k) * self.ak(-x, k) * self.ak(1 + n, k)) / ((mt.factorial(k) ** 2) * (self.ak(1 - self.M, k))))
        return answer

    def tchibichef_nm(self, n, m, I):
        answer = 0
        for x in range(self.M):
            for y in range(self.N):
                answer = answer + self.t(n, x) * self.t(m, y) * I[x, y]
        return answer

    def tchbichef_ordre_n(self, n):
        
        tchibi_n = []
        for i in range(n + 1):
            for j in range(n + 1):
                if i + j <= n:
                    tchibi_n.append(self.tchibichef_nm(i, j, I))
        return tchibi_n

