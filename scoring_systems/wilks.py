"""
Wilks score calculator
"""

class wilks(object):
    """
    Wilks score.
    """

    def __init__(self, sex):
        if sex not in ["M", "F"]:
            raise Exception("'sex' must be M or F")
        PARS = {
            "M": [-216.0475144, 16.2606339, -0.002388645, -0.00113732, 7.01863E-06, -1.291E-08],
            "F": [594.31747775582, -27.23842536447, 0.82112226871, -0.00930733913, 0.00004731582, -0.00000009054]
        } #End parameters dictionary
        self._set_coefficients(*PARS[sex])

    def _set_coefficients(self, a, b, c, d, e, f):
        """
        Assign the coefficients to this object.
        """
        self.coefficients = [a, b, c, d, e, f]
        return

    def score(self, bodyweight, total, in_pounds=False):
        """
        Compute the Wilks score given the bodyweight and total
        of the lifter.

        Args:
            bodyweight (float): bodyweight of the lifter
            total (float): total of the lift(s)
            in_pounds (boolean): whether the inputs are in lbs or kgs (default: False)

        Returns:
            Wilks score
        """

        if in_pounds: #Convert lbs to kgs
            bodyweight = bodyweight / 2.205
            total = total / 2.205
        a, b, c, d, e, f = self.coefficients
        return total * 500. / (a + b*bodyweight + c*bodyweight**2 +
                               d*bodyweight**3 + e*bodyweight**4 +
                               f*bodyweight**5)

if __name__ == "__main__":
    M = wilks("M")
    print(M.score(200, 1000, in_pounds=True))
