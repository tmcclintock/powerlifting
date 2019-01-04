"""
Implementations of the scoring system released by the IPF in 2019.
"""

from numpy import log

class ipf(object):
    """
    IPF points released in 2019.
    """
    
    def __init__(self, sex, equipment, event):
        if sex not in ["M", "F"]:
            raise Exception("'sex' must be M or F")
        if equipment not in ["Raw", "SP"]:
            raise Exception("'equipment' must be Raw or SP")
        if event not in ["SBD", "B"]:
            raise Exception("'equipment' must be SBD or B")

        PARS = {
            "M": {
                "Raw": {
                    "SBD": [310.67, 857.785, 53.216, 147.0835],
                    "B": [86.4745, 259.155, 17.57845, 53.122],
                },
                "SP": {
                    "SBD": [387.265, 1121.28, 80.6324, 222.4896],
                    "B": [133.94, 441.465, 35.3938, 113.0057],
                }
            },
            "F": {
                "Raw": {
                    "SBD": [125.1435, 228.03, 34.5246, 86.8301],
                    "B": [25.0485, 43.848, 6.7172, 13.952],
                },
                "SP": {
                    "SBD": [176.58, 373.315, 48.4534, 110.0103],
                    "B": [49.106, 124.209, 23.199, 67.4926],
                }
            }
        } #End parameters dictionary
        parameters = PARS[sex][equipment][event]
        self._set_coefficients(*parameters)

    def _set_coefficients(self, C1, C2, C3, C4):
        """
        Assign the coefficients to this object.
        """
        self.coefficients = [C1, C2, C3, C4]
        return

    def score(self, bodyweight, total, in_pounds=False):
        """
        Compute the IPF score given the bodyweight and total
        of the lifter.

        Args:
            bodyweight (float): bodyweight of the lifter
            total (float): total of the lift(s)
            in_pounds (boolean): whether the inputs are in lbs or kgs (default: False)

        Returns:
            IPF score
        """
        if in_pounds: #Convert lbs to kgs
            bodyweight = bodyweight / 2.205
            total = total / 2.205
        C1, C2, C3, C4 = self.coefficients
        return 500 + 100*(total-C1*log(bodyweight)+C2)/(C3*log(bodyweight)-C4)

if __name__ == "__main__":
    MRSBD = ipf("M", "Raw", "SBD")
    print(MRSBD.score(200, 1000, in_pounds=True))

