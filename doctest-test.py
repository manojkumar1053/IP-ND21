class Simulator:
    def run(self) -> int:
        """ run the simulation
        >>> sim.run()
        533342848544
        :return:
        """
        return self.a ** 2 + self.b / 16 - self.c


if __name__ == "__main__":
    import doctest

    doctest.testmod(extraglobs={sim: Simulator(43, 935, 3)})
