class py_solver:
    """simple solver utility to find the values for R1 (Ohms) and C (Farads) such that
    at R2 values of 0 Ohms and 10000 Ohms, the output freq (Hz) of an LM555 timer chip
    are 60 Hz and 0 Hz respectively. Will output the highest possible value of R1 (Ohms) and the
    associated cap. value (F) for the above relationship to be satisified.
    """

    def __init__(self):
        self.sixtyFreq = 0
        self.oneFreq = 0

    def freq_Hz(self,cVal,R1val,R2val):
        # on_time = 0.693*cVal*(R1val+R2val)
        # off_time = 0.693*cVal*(R2val)
        freqHz = 1/(0.693*cVal*(R1val+2*R2val))
        return(freqHz)

    def find_sixty_freq(self):
        # from sympy.solvers import solve
        # from sympy import Symbol
        import numpy as np
        # R2val = Symbol('R2val')
        cval = np.arange((1*10**-12),2,0.0001)
        R1array = np.arange(1,1000,1)

        for i in R1array:
            for i2 in cval:
                freq = self.freq_Hz(i,i2,0)
                if freq > 60 -1 and freq < 60 + 1:
                    retRsixty = i
                    retCsixty = i2
        return(retRsixty,retCsixty)

    def find_one_freq(self,retR,retC):
        import numpy as np
        cval = np.arange((1*10**-12),2,0.0001)
        R1array = np.arange(1,1000,1)

        for i in R1array:
            for i2 in cval:
                freq = self.freq_Hz(i,i2,10000)
                if freq > 1-1 and freq < 1 + 1 and i == retR and i2==retC:
                    retRboth = i
                    retCboth = i2
        print(retRboth,retCboth)

py1 = py_solver()
retR, retC = py1.find_sixty_freq()
py1.find_one_freq(retR,retC)
