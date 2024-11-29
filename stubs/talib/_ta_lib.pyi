from __future__ import annotations
import builtins as __builtins__
from collections import OrderedDict
import math as math
import numpy as numpy
import pandas as pandas
from pandas.core.frame import DataFrame as __PANDAS_DATAFRAME
from pandas.core.series import Series as __PANDAS_SERIES
import sys as sys
import threading as threading
__all__: list = ['ACOS', 'AD', 'ADD', 'ADOSC', 'ADX', 'ADXR', 'APO', 'AROON', 'AROONOSC', 'ASIN', 'ATAN', 'ATR', 'AVGPRICE', 'BBANDS', 'BETA', 'BOP', 'CCI', 'CDL2CROWS', 'CDL3BLACKCROWS', 'CDL3INSIDE', 'CDL3LINESTRIKE', 'CDL3OUTSIDE', 'CDL3STARSINSOUTH', 'CDL3WHITESOLDIERS', 'CDLABANDONEDBABY', 'CDLADVANCEBLOCK', 'CDLBELTHOLD', 'CDLBREAKAWAY', 'CDLCLOSINGMARUBOZU', 'CDLCONCEALBABYSWALL', 'CDLCOUNTERATTACK', 'CDLDARKCLOUDCOVER', 'CDLDOJI', 'CDLDOJISTAR', 'CDLDRAGONFLYDOJI', 'CDLENGULFING', 'CDLEVENINGDOJISTAR', 'CDLEVENINGSTAR', 'CDLGAPSIDESIDEWHITE', 'CDLGRAVESTONEDOJI', 'CDLHAMMER', 'CDLHANGINGMAN', 'CDLHARAMI', 'CDLHARAMICROSS', 'CDLHIGHWAVE', 'CDLHIKKAKE', 'CDLHIKKAKEMOD', 'CDLHOMINGPIGEON', 'CDLIDENTICAL3CROWS', 'CDLINNECK', 'CDLINVERTEDHAMMER', 'CDLKICKING', 'CDLKICKINGBYLENGTH', 'CDLLADDERBOTTOM', 'CDLLONGLEGGEDDOJI', 'CDLLONGLINE', 'CDLMARUBOZU', 'CDLMATCHINGLOW', 'CDLMATHOLD', 'CDLMORNINGDOJISTAR', 'CDLMORNINGSTAR', 'CDLONNECK', 'CDLPIERCING', 'CDLRICKSHAWMAN', 'CDLRISEFALL3METHODS', 'CDLSEPARATINGLINES', 'CDLSHOOTINGSTAR', 'CDLSHORTLINE', 'CDLSPINNINGTOP', 'CDLSTALLEDPATTERN', 'CDLSTICKSANDWICH', 'CDLTAKURI', 'CDLTASUKIGAP', 'CDLTHRUSTING', 'CDLTRISTAR', 'CDLUNIQUE3RIVER', 'CDLUPSIDEGAP2CROWS', 'CDLXSIDEGAP3METHODS', 'CEIL', 'CMO', 'CORREL', 'COS', 'COSH', 'DEMA', 'DIV', 'DX', 'EMA', 'EXP', 'FLOOR', 'HT_DCPERIOD', 'HT_DCPHASE', 'HT_PHASOR', 'HT_SINE', 'HT_TRENDLINE', 'HT_TRENDMODE', 'KAMA', 'LINEARREG', 'LINEARREG_ANGLE', 'LINEARREG_INTERCEPT', 'LINEARREG_SLOPE', 'LN', 'LOG10', 'MA', 'MACD', 'MACDEXT', 'MACDFIX', 'MAMA', 'MAVP', 'MAX', 'MAXINDEX', 'MEDPRICE', 'MFI', 'MIDPOINT', 'MIDPRICE', 'MIN', 'MININDEX', 'MINMAX', 'MINMAXINDEX', 'MINUS_DI', 'MINUS_DM', 'MOM', 'MULT', 'NATR', 'OBV', 'PLUS_DI', 'PLUS_DM', 'PPO', 'ROC', 'ROCP', 'ROCR', 'ROCR100', 'RSI', 'SAR', 'SAREXT', 'SIN', 'SINH', 'SMA', 'SQRT', 'STDDEV', 'STOCH', 'STOCHF', 'STOCHRSI', 'SUB', 'SUM', 'T3', 'TAN', 'TANH', 'TEMA', 'TRANGE', 'TRIMA', 'TRIX', 'TSF', 'TYPPRICE', 'ULTOSC', 'VAR', 'WCLPRICE', 'WILLR', 'WMA', 'stream_ACOS', 'stream_AD', 'stream_ADD', 'stream_ADOSC', 'stream_ADX', 'stream_ADXR', 'stream_APO', 'stream_AROON', 'stream_AROONOSC', 'stream_ASIN', 'stream_ATAN', 'stream_ATR', 'stream_AVGPRICE', 'stream_BBANDS', 'stream_BETA', 'stream_BOP', 'stream_CCI', 'stream_CDL2CROWS', 'stream_CDL3BLACKCROWS', 'stream_CDL3INSIDE', 'stream_CDL3LINESTRIKE', 'stream_CDL3OUTSIDE', 'stream_CDL3STARSINSOUTH', 'stream_CDL3WHITESOLDIERS', 'stream_CDLABANDONEDBABY', 'stream_CDLADVANCEBLOCK', 'stream_CDLBELTHOLD', 'stream_CDLBREAKAWAY', 'stream_CDLCLOSINGMARUBOZU', 'stream_CDLCONCEALBABYSWALL', 'stream_CDLCOUNTERATTACK', 'stream_CDLDARKCLOUDCOVER', 'stream_CDLDOJI', 'stream_CDLDOJISTAR', 'stream_CDLDRAGONFLYDOJI', 'stream_CDLENGULFING', 'stream_CDLEVENINGDOJISTAR', 'stream_CDLEVENINGSTAR', 'stream_CDLGAPSIDESIDEWHITE', 'stream_CDLGRAVESTONEDOJI', 'stream_CDLHAMMER', 'stream_CDLHANGINGMAN', 'stream_CDLHARAMI', 'stream_CDLHARAMICROSS', 'stream_CDLHIGHWAVE', 'stream_CDLHIKKAKE', 'stream_CDLHIKKAKEMOD', 'stream_CDLHOMINGPIGEON', 'stream_CDLIDENTICAL3CROWS', 'stream_CDLINNECK', 'stream_CDLINVERTEDHAMMER', 'stream_CDLKICKING', 'stream_CDLKICKINGBYLENGTH', 'stream_CDLLADDERBOTTOM', 'stream_CDLLONGLEGGEDDOJI', 'stream_CDLLONGLINE', 'stream_CDLMARUBOZU', 'stream_CDLMATCHINGLOW', 'stream_CDLMATHOLD', 'stream_CDLMORNINGDOJISTAR', 'stream_CDLMORNINGSTAR', 'stream_CDLONNECK', 'stream_CDLPIERCING', 'stream_CDLRICKSHAWMAN', 'stream_CDLRISEFALL3METHODS', 'stream_CDLSEPARATINGLINES', 'stream_CDLSHOOTINGSTAR', 'stream_CDLSHORTLINE', 'stream_CDLSPINNINGTOP', 'stream_CDLSTALLEDPATTERN', 'stream_CDLSTICKSANDWICH', 'stream_CDLTAKURI', 'stream_CDLTASUKIGAP', 'stream_CDLTHRUSTING', 'stream_CDLTRISTAR', 'stream_CDLUNIQUE3RIVER', 'stream_CDLUPSIDEGAP2CROWS', 'stream_CDLXSIDEGAP3METHODS', 'stream_CEIL', 'stream_CMO', 'stream_CORREL', 'stream_COS', 'stream_COSH', 'stream_DEMA', 'stream_DIV', 'stream_DX', 'stream_EMA', 'stream_EXP', 'stream_FLOOR', 'stream_HT_DCPERIOD', 'stream_HT_DCPHASE', 'stream_HT_PHASOR', 'stream_HT_SINE', 'stream_HT_TRENDLINE', 'stream_HT_TRENDMODE', 'stream_KAMA', 'stream_LINEARREG', 'stream_LINEARREG_ANGLE', 'stream_LINEARREG_INTERCEPT', 'stream_LINEARREG_SLOPE', 'stream_LN', 'stream_LOG10', 'stream_MA', 'stream_MACD', 'stream_MACDEXT', 'stream_MACDFIX', 'stream_MAMA', 'stream_MAVP', 'stream_MAX', 'stream_MAXINDEX', 'stream_MEDPRICE', 'stream_MFI', 'stream_MIDPOINT', 'stream_MIDPRICE', 'stream_MIN', 'stream_MININDEX', 'stream_MINMAX', 'stream_MINMAXINDEX', 'stream_MINUS_DI', 'stream_MINUS_DM', 'stream_MOM', 'stream_MULT', 'stream_NATR', 'stream_OBV', 'stream_PLUS_DI', 'stream_PLUS_DM', 'stream_PPO', 'stream_ROC', 'stream_ROCP', 'stream_ROCR', 'stream_ROCR100', 'stream_RSI', 'stream_SAR', 'stream_SAREXT', 'stream_SIN', 'stream_SINH', 'stream_SMA', 'stream_SQRT', 'stream_STDDEV', 'stream_STOCH', 'stream_STOCHF', 'stream_STOCHRSI', 'stream_SUB', 'stream_SUM', 'stream_T3', 'stream_TAN', 'stream_TANH', 'stream_TEMA', 'stream_TRANGE', 'stream_TRIMA', 'stream_TRIX', 'stream_TSF', 'stream_TYPPRICE', 'stream_ULTOSC', 'stream_VAR', 'stream_WCLPRICE', 'stream_WILLR', 'stream_WMA']
class Function:
    """
    
        This is a pythonic wrapper around TALIB's abstract interface. It is
        intended to simplify using individual TALIB functions by providing a
        unified interface for setting/controlling input data, setting function
        parameters and retrieving results. Input data consists of a ``dict`` of
        ``numpy`` arrays (or a ``pandas.DataFrame`` or ``polars.DataFrame``), one
        array for each of open, high, low, close and volume. This can be set with
        the set_input_arrays() method. Which keyed array(s) are used as inputs when
        calling the function is controlled using the input_names property.
    
        This class gets initialized with a TALIB function name and optionally an
        input_arrays object. It provides the following primary functions for
        setting inputs and retrieving results:
    
        ---- input_array/TA-function-parameter set-only functions -----
        - set_input_arrays(input_arrays)
        - set_function_args([input_arrays,] [param_args_andor_kwargs])
    
        Documentation for param_args_andor_kwargs can be seen by printing the
        Function instance or programatically via the info, input_names and
        parameters properties.
    
        ----- result-returning functions -----
        - the outputs property wraps a method which ensures results are always valid
        - run([input_arrays]) # calls set_input_arrays and returns self.outputs
        - FunctionInstance([input_arrays,] [param_args_andor_kwargs]) # calls set_function_args and returns self.outputs
        
    """
    def _Function__call_function(self):
        ...
    def _Function__check_opt_input_value(self, input_name, value):
        ...
    def _Function__get_opt_input_value(self, input_name):
        """
        
                Returns the user-set value if there is one, otherwise the default.
                
        """
    def _Function__input_price_series_names(self):
        ...
    def __call__(self, *args, **kwargs):
        """
        
                func_instance([input_arrays,] [parameter_args,] [input_price_series_kwargs,] [parameter_kwargs])
        
                This is a shortcut to the outputs property that also allows setting
                the input_arrays dict and function parameters.
                
        """
    def __init__(self, function_name, func_object, *args, **kwargs):
        ...
    def __repr__(self):
        ...
    def __str__(self):
        ...
    def __unicode__(self):
        ...
    def get_input_arrays(self):
        """
        
                Returns a copy of the dict of input arrays in use.
                
        """
    def get_input_names(self):
        """
        
                Returns the dict of input price series names that specifies which
                of the ndarrays in input_arrays will be used to calculate the function.
                
        """
    def get_parameters(self):
        """
        
                Returns the function's optional parameters and their default values.
                
        """
    def run(self, input_arrays = None):
        """
        
                run([input_arrays=None])
        
                This is a shortcut to the outputs property that also allows setting
                the input_arrays dict.
                
        """
    def set_function_args(self, *args, **kwargs):
        """
        
                optional args:[input_arrays,] [parameter_args,] [input_price_series_kwargs,] [parameter_kwargs]
                
        """
    def set_input_arrays(self, input_arrays):
        """
        
                Sets the dict of input_arrays to use. Returns True/False for
                subclasses:
        
                If input_arrays is a dict with the keys open, high, low, close and
                volume, it is assigned as the input_array to use and this function
                returns True, returning False otherwise. If you implement your own
                data type and wish to subclass Function, you should wrap this function
                with an if-statement:
        
                class CustomFunction(Function):
                    def __init__(self, function_name):
                        Function.__init__(self, function_name)
        
                    def set_input_arrays(self, input_data):
                        if Function.set_input_arrays(self, input_data):
                            return True
                        elif isinstance(input_data, some_module.CustomDataType):
                            input_arrays = Function.get_input_arrays(self)
                            # convert input_data to input_arrays and then call the super
                            Function.set_input_arrays(self, input_arrays)
                            return True
                        return False
                
        """
    def set_input_names(self, input_names):
        """
        
                Sets the input price series names to use.
                
        """
    def set_parameters(self, parameters = None, **kwargs):
        """
        
                Sets the function parameter values.
                
        """
    @property
    def _Function__local(self):
        ...
    @property
    def function_flags(self):
        """
        
                Returns any function flags defined for this indicator function.
                
        """
    @property
    def info(self):
        """
        
                Returns a copy of the function's info dict.
                
        """
    @property
    def input_arrays(self):
        """
        
                Returns a copy of the dict of input arrays in use.
                
        """
    @input_arrays.setter
    def input_arrays(self, input_arrays):
        """
        
                Sets the dict of input_arrays to use. Returns True/False for
                subclasses:
        
                If input_arrays is a dict with the keys open, high, low, close and
                volume, it is assigned as the input_array to use and this function
                returns True, returning False otherwise. If you implement your own
                data type and wish to subclass Function, you should wrap this function
                with an if-statement:
        
                class CustomFunction(Function):
                    def __init__(self, function_name):
                        Function.__init__(self, function_name)
        
                    def set_input_arrays(self, input_data):
                        if Function.set_input_arrays(self, input_data):
                            return True
                        elif isinstance(input_data, some_module.CustomDataType):
                            input_arrays = Function.get_input_arrays(self)
                            # convert input_data to input_arrays and then call the super
                            Function.set_input_arrays(self, input_arrays)
                            return True
                        return False
                
        """
    @property
    def input_names(self):
        """
        
                Returns the dict of input price series names that specifies which
                of the ndarrays in input_arrays will be used to calculate the function.
                
        """
    @input_names.setter
    def input_names(self, input_names):
        """
        
                Sets the input price series names to use.
                
        """
    @property
    def lookback(self):
        """
        
                Returns the lookback window size for the function with the parameter
                values that are currently set.
                
        """
    @property
    def output_flags(self):
        """
        
                Returns the flags for each output for this indicator function.
                
        """
    @property
    def output_names(self):
        """
        
                Returns a list of the output names returned by this function.
                
        """
    @property
    def outputs(self):
        """
        
                Returns the TA function values for the currently set input_arrays and
                parameters. Returned values are a ndarray if there is only one output
                or a list of ndarrays for more than one output.
                
        """
    @property
    def parameters(self):
        """
        
                Returns the function's optional parameters and their default values.
                
        """
    @parameters.setter
    def parameters(self, parameters = None, **kwargs):
        """
        
                Sets the function parameter values.
                
        """
def ACOS(*args, **kwds):
    """
     ACOS(real)
    
        Vector Trigonometric ACos (Math Transform)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            real
        
    """
def AD(*args, **kwds):
    """
     AD(high, low, close, volume)
    
        Chaikin A/D Line (Volume Indicators)
    
        Inputs:
            prices: ['high', 'low', 'close', 'volume']
        Outputs:
            real
        
    """
def ADD(*args, **kwds):
    """
     ADD(real0, real1)
    
        Vector Arithmetic Add (Math Operators)
    
        Inputs:
            real0: (any ndarray)
            real1: (any ndarray)
        Outputs:
            real
        
    """
def ADOSC(*args, **kwds):
    """
     ADOSC(high, low, close, volume[, fastperiod=?, slowperiod=?])
    
        Chaikin A/D Oscillator (Volume Indicators)
    
        Inputs:
            prices: ['high', 'low', 'close', 'volume']
        Parameters:
            fastperiod: 3
            slowperiod: 10
        Outputs:
            real
        
    """
def ADX(*args, **kwds):
    """
     ADX(high, low, close[, timeperiod=?])
    
        Average Directional Movement Index (Momentum Indicators)
    
        Inputs:
            prices: ['high', 'low', 'close']
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def ADXR(*args, **kwds):
    """
     ADXR(high, low, close[, timeperiod=?])
    
        Average Directional Movement Index Rating (Momentum Indicators)
    
        Inputs:
            prices: ['high', 'low', 'close']
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def APO(*args, **kwds):
    """
     APO(real[, fastperiod=?, slowperiod=?, matype=?])
    
        Absolute Price Oscillator (Momentum Indicators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            fastperiod: 12
            slowperiod: 26
            matype: 0 (Simple Moving Average)
        Outputs:
            real
        
    """
def AROON(*args, **kwds):
    """
     AROON(high, low[, timeperiod=?])
    
        Aroon (Momentum Indicators)
    
        Inputs:
            prices: ['high', 'low']
        Parameters:
            timeperiod: 14
        Outputs:
            aroondown
            aroonup
        
    """
def AROONOSC(*args, **kwds):
    """
     AROONOSC(high, low[, timeperiod=?])
    
        Aroon Oscillator (Momentum Indicators)
    
        Inputs:
            prices: ['high', 'low']
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def ASIN(*args, **kwds):
    """
     ASIN(real)
    
        Vector Trigonometric ASin (Math Transform)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            real
        
    """
def ATAN(*args, **kwds):
    """
     ATAN(real)
    
        Vector Trigonometric ATan (Math Transform)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            real
        
    """
def ATR(*args, **kwds):
    """
     ATR(high, low, close[, timeperiod=?])
    
        Average True Range (Volatility Indicators)
    
        Inputs:
            prices: ['high', 'low', 'close']
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def AVGPRICE(*args, **kwds):
    """
     AVGPRICE(open, high, low, close)
    
        Average Price (Price Transform)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            real
        
    """
def BBANDS(*args, **kwds):
    """
     BBANDS(real[, timeperiod=?, nbdevup=?, nbdevdn=?, matype=?])
    
        Bollinger Bands (Overlap Studies)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 5
            nbdevup: 2.0
            nbdevdn: 2.0
            matype: 0 (Simple Moving Average)
        Outputs:
            upperband
            middleband
            lowerband
        
    """
def BETA(*args, **kwds):
    """
     BETA(real0, real1[, timeperiod=?])
    
        Beta (Statistic Functions)
    
        Inputs:
            real0: (any ndarray)
            real1: (any ndarray)
        Parameters:
            timeperiod: 5
        Outputs:
            real
        
    """
def BOP(*args, **kwds):
    """
     BOP(open, high, low, close)
    
        Balance Of Power (Momentum Indicators)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            real
        
    """
def CCI(*args, **kwds):
    """
     CCI(high, low, close[, timeperiod=?])
    
        Commodity Channel Index (Momentum Indicators)
    
        Inputs:
            prices: ['high', 'low', 'close']
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def CDL2CROWS(*args, **kwds):
    """
     CDL2CROWS(open, high, low, close)
    
        Two Crows (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDL3BLACKCROWS(*args, **kwds):
    """
     CDL3BLACKCROWS(open, high, low, close)
    
        Three Black Crows (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDL3INSIDE(*args, **kwds):
    """
     CDL3INSIDE(open, high, low, close)
    
        Three Inside Up/Down (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDL3LINESTRIKE(*args, **kwds):
    """
     CDL3LINESTRIKE(open, high, low, close)
    
        Three-Line Strike  (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDL3OUTSIDE(*args, **kwds):
    """
     CDL3OUTSIDE(open, high, low, close)
    
        Three Outside Up/Down (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDL3STARSINSOUTH(*args, **kwds):
    """
     CDL3STARSINSOUTH(open, high, low, close)
    
        Three Stars In The South (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDL3WHITESOLDIERS(*args, **kwds):
    """
     CDL3WHITESOLDIERS(open, high, low, close)
    
        Three Advancing White Soldiers (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLABANDONEDBABY(*args, **kwds):
    """
     CDLABANDONEDBABY(open, high, low, close[, penetration=?])
    
        Abandoned Baby (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Parameters:
            penetration: 0.3
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLADVANCEBLOCK(*args, **kwds):
    """
     CDLADVANCEBLOCK(open, high, low, close)
    
        Advance Block (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLBELTHOLD(*args, **kwds):
    """
     CDLBELTHOLD(open, high, low, close)
    
        Belt-hold (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLBREAKAWAY(*args, **kwds):
    """
     CDLBREAKAWAY(open, high, low, close)
    
        Breakaway (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLCLOSINGMARUBOZU(*args, **kwds):
    """
     CDLCLOSINGMARUBOZU(open, high, low, close)
    
        Closing Marubozu (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLCONCEALBABYSWALL(*args, **kwds):
    """
     CDLCONCEALBABYSWALL(open, high, low, close)
    
        Concealing Baby Swallow (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLCOUNTERATTACK(*args, **kwds):
    """
     CDLCOUNTERATTACK(open, high, low, close)
    
        Counterattack (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLDARKCLOUDCOVER(*args, **kwds):
    """
     CDLDARKCLOUDCOVER(open, high, low, close[, penetration=?])
    
        Dark Cloud Cover (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Parameters:
            penetration: 0.5
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLDOJI(*args, **kwds):
    """
     CDLDOJI(open, high, low, close)
    
        Doji (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLDOJISTAR(*args, **kwds):
    """
     CDLDOJISTAR(open, high, low, close)
    
        Doji Star (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLDRAGONFLYDOJI(*args, **kwds):
    """
     CDLDRAGONFLYDOJI(open, high, low, close)
    
        Dragonfly Doji (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLENGULFING(*args, **kwds):
    """
     CDLENGULFING(open, high, low, close)
    
        Engulfing Pattern (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLEVENINGDOJISTAR(*args, **kwds):
    """
     CDLEVENINGDOJISTAR(open, high, low, close[, penetration=?])
    
        Evening Doji Star (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Parameters:
            penetration: 0.3
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLEVENINGSTAR(*args, **kwds):
    """
     CDLEVENINGSTAR(open, high, low, close[, penetration=?])
    
        Evening Star (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Parameters:
            penetration: 0.3
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLGAPSIDESIDEWHITE(*args, **kwds):
    """
     CDLGAPSIDESIDEWHITE(open, high, low, close)
    
        Up/Down-gap side-by-side white lines (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLGRAVESTONEDOJI(*args, **kwds):
    """
     CDLGRAVESTONEDOJI(open, high, low, close)
    
        Gravestone Doji (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLHAMMER(*args, **kwds):
    """
     CDLHAMMER(open, high, low, close)
    
        Hammer (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLHANGINGMAN(*args, **kwds):
    """
     CDLHANGINGMAN(open, high, low, close)
    
        Hanging Man (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLHARAMI(*args, **kwds):
    """
     CDLHARAMI(open, high, low, close)
    
        Harami Pattern (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLHARAMICROSS(*args, **kwds):
    """
     CDLHARAMICROSS(open, high, low, close)
    
        Harami Cross Pattern (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLHIGHWAVE(*args, **kwds):
    """
     CDLHIGHWAVE(open, high, low, close)
    
        High-Wave Candle (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLHIKKAKE(*args, **kwds):
    """
     CDLHIKKAKE(open, high, low, close)
    
        Hikkake Pattern (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLHIKKAKEMOD(*args, **kwds):
    """
     CDLHIKKAKEMOD(open, high, low, close)
    
        Modified Hikkake Pattern (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLHOMINGPIGEON(*args, **kwds):
    """
     CDLHOMINGPIGEON(open, high, low, close)
    
        Homing Pigeon (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLIDENTICAL3CROWS(*args, **kwds):
    """
     CDLIDENTICAL3CROWS(open, high, low, close)
    
        Identical Three Crows (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLINNECK(*args, **kwds):
    """
     CDLINNECK(open, high, low, close)
    
        In-Neck Pattern (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLINVERTEDHAMMER(*args, **kwds):
    """
     CDLINVERTEDHAMMER(open, high, low, close)
    
        Inverted Hammer (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLKICKING(*args, **kwds):
    """
     CDLKICKING(open, high, low, close)
    
        Kicking (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLKICKINGBYLENGTH(*args, **kwds):
    """
     CDLKICKINGBYLENGTH(open, high, low, close)
    
        Kicking - bull/bear determined by the longer marubozu (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLLADDERBOTTOM(*args, **kwds):
    """
     CDLLADDERBOTTOM(open, high, low, close)
    
        Ladder Bottom (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLLONGLEGGEDDOJI(*args, **kwds):
    """
     CDLLONGLEGGEDDOJI(open, high, low, close)
    
        Long Legged Doji (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLLONGLINE(*args, **kwds):
    """
     CDLLONGLINE(open, high, low, close)
    
        Long Line Candle (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLMARUBOZU(*args, **kwds):
    """
     CDLMARUBOZU(open, high, low, close)
    
        Marubozu (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLMATCHINGLOW(*args, **kwds):
    """
     CDLMATCHINGLOW(open, high, low, close)
    
        Matching Low (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLMATHOLD(*args, **kwds):
    """
     CDLMATHOLD(open, high, low, close[, penetration=?])
    
        Mat Hold (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Parameters:
            penetration: 0.5
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLMORNINGDOJISTAR(*args, **kwds):
    """
     CDLMORNINGDOJISTAR(open, high, low, close[, penetration=?])
    
        Morning Doji Star (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Parameters:
            penetration: 0.3
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLMORNINGSTAR(*args, **kwds):
    """
     CDLMORNINGSTAR(open, high, low, close[, penetration=?])
    
        Morning Star (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Parameters:
            penetration: 0.3
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLONNECK(*args, **kwds):
    """
     CDLONNECK(open, high, low, close)
    
        On-Neck Pattern (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLPIERCING(*args, **kwds):
    """
     CDLPIERCING(open, high, low, close)
    
        Piercing Pattern (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLRICKSHAWMAN(*args, **kwds):
    """
     CDLRICKSHAWMAN(open, high, low, close)
    
        Rickshaw Man (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLRISEFALL3METHODS(*args, **kwds):
    """
     CDLRISEFALL3METHODS(open, high, low, close)
    
        Rising/Falling Three Methods (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLSEPARATINGLINES(*args, **kwds):
    """
     CDLSEPARATINGLINES(open, high, low, close)
    
        Separating Lines (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLSHOOTINGSTAR(*args, **kwds):
    """
     CDLSHOOTINGSTAR(open, high, low, close)
    
        Shooting Star (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLSHORTLINE(*args, **kwds):
    """
     CDLSHORTLINE(open, high, low, close)
    
        Short Line Candle (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLSPINNINGTOP(*args, **kwds):
    """
     CDLSPINNINGTOP(open, high, low, close)
    
        Spinning Top (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLSTALLEDPATTERN(*args, **kwds):
    """
     CDLSTALLEDPATTERN(open, high, low, close)
    
        Stalled Pattern (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLSTICKSANDWICH(*args, **kwds):
    """
     CDLSTICKSANDWICH(open, high, low, close)
    
        Stick Sandwich (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLTAKURI(*args, **kwds):
    """
     CDLTAKURI(open, high, low, close)
    
        Takuri (Dragonfly Doji with very long lower shadow) (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLTASUKIGAP(*args, **kwds):
    """
     CDLTASUKIGAP(open, high, low, close)
    
        Tasuki Gap (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLTHRUSTING(*args, **kwds):
    """
     CDLTHRUSTING(open, high, low, close)
    
        Thrusting Pattern (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLTRISTAR(*args, **kwds):
    """
     CDLTRISTAR(open, high, low, close)
    
        Tristar Pattern (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLUNIQUE3RIVER(*args, **kwds):
    """
     CDLUNIQUE3RIVER(open, high, low, close)
    
        Unique 3 River (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLUPSIDEGAP2CROWS(*args, **kwds):
    """
     CDLUPSIDEGAP2CROWS(open, high, low, close)
    
        Upside Gap Two Crows (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CDLXSIDEGAP3METHODS(*args, **kwds):
    """
     CDLXSIDEGAP3METHODS(open, high, low, close)
    
        Upside/Downside Gap Three Methods (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def CEIL(*args, **kwds):
    """
     CEIL(real)
    
        Vector Ceil (Math Transform)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            real
        
    """
def CMO(*args, **kwds):
    """
     CMO(real[, timeperiod=?])
    
        Chande Momentum Oscillator (Momentum Indicators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def CORREL(*args, **kwds):
    """
     CORREL(real0, real1[, timeperiod=?])
    
        Pearson's Correlation Coefficient (r) (Statistic Functions)
    
        Inputs:
            real0: (any ndarray)
            real1: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            real
        
    """
def COS(*args, **kwds):
    """
     COS(real)
    
        Vector Trigonometric Cos (Math Transform)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            real
        
    """
def COSH(*args, **kwds):
    """
     COSH(real)
    
        Vector Trigonometric Cosh (Math Transform)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            real
        
    """
def DEMA(*args, **kwds):
    """
     DEMA(real[, timeperiod=?])
    
        Double Exponential Moving Average (Overlap Studies)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            real
        
    """
def DIV(*args, **kwds):
    """
     DIV(real0, real1)
    
        Vector Arithmetic Div (Math Operators)
    
        Inputs:
            real0: (any ndarray)
            real1: (any ndarray)
        Outputs:
            real
        
    """
def DX(*args, **kwds):
    """
     DX(high, low, close[, timeperiod=?])
    
        Directional Movement Index (Momentum Indicators)
    
        Inputs:
            prices: ['high', 'low', 'close']
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def EMA(*args, **kwds):
    """
     EMA(real[, timeperiod=?])
    
        Exponential Moving Average (Overlap Studies)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            real
        
    """
def EXP(*args, **kwds):
    """
     EXP(real)
    
        Vector Arithmetic Exp (Math Transform)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            real
        
    """
def FLOOR(*args, **kwds):
    """
     FLOOR(real)
    
        Vector Floor (Math Transform)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            real
        
    """
def HT_DCPERIOD(*args, **kwds):
    """
     HT_DCPERIOD(real)
    
        Hilbert Transform - Dominant Cycle Period (Cycle Indicators)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            real
        
    """
def HT_DCPHASE(*args, **kwds):
    """
     HT_DCPHASE(real)
    
        Hilbert Transform - Dominant Cycle Phase (Cycle Indicators)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            real
        
    """
def HT_PHASOR(*args, **kwds):
    """
     HT_PHASOR(real)
    
        Hilbert Transform - Phasor Components (Cycle Indicators)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            inphase
            quadrature
        
    """
def HT_SINE(*args, **kwds):
    """
     HT_SINE(real)
    
        Hilbert Transform - SineWave (Cycle Indicators)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            sine
            leadsine
        
    """
def HT_TRENDLINE(*args, **kwds):
    """
     HT_TRENDLINE(real)
    
        Hilbert Transform - Instantaneous Trendline (Overlap Studies)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            real
        
    """
def HT_TRENDMODE(*args, **kwds):
    """
     HT_TRENDMODE(real)
    
        Hilbert Transform - Trend vs Cycle Mode (Cycle Indicators)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def KAMA(*args, **kwds):
    """
     KAMA(real[, timeperiod=?])
    
        Kaufman Adaptive Moving Average (Overlap Studies)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            real
        
    """
def LINEARREG(*args, **kwds):
    """
     LINEARREG(real[, timeperiod=?])
    
        Linear Regression (Statistic Functions)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def LINEARREG_ANGLE(*args, **kwds):
    """
     LINEARREG_ANGLE(real[, timeperiod=?])
    
        Linear Regression Angle (Statistic Functions)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def LINEARREG_INTERCEPT(*args, **kwds):
    """
     LINEARREG_INTERCEPT(real[, timeperiod=?])
    
        Linear Regression Intercept (Statistic Functions)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def LINEARREG_SLOPE(*args, **kwds):
    """
     LINEARREG_SLOPE(real[, timeperiod=?])
    
        Linear Regression Slope (Statistic Functions)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def LN(*args, **kwds):
    """
     LN(real)
    
        Vector Log Natural (Math Transform)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            real
        
    """
def LOG10(*args, **kwds):
    """
     LOG10(real)
    
        Vector Log10 (Math Transform)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            real
        
    """
def MA(*args, **kwds):
    """
     MA(real[, timeperiod=?, matype=?])
    
        Moving average (Overlap Studies)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
            matype: 0 (Simple Moving Average)
        Outputs:
            real
        
    """
def MACD(*args, **kwds):
    """
     MACD(real[, fastperiod=?, slowperiod=?, signalperiod=?])
    
        Moving Average Convergence/Divergence (Momentum Indicators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            fastperiod: 12
            slowperiod: 26
            signalperiod: 9
        Outputs:
            macd
            macdsignal
            macdhist
        
    """
def MACDEXT(*args, **kwds):
    """
     MACDEXT(real[, fastperiod=?, fastmatype=?, slowperiod=?, slowmatype=?, signalperiod=?, signalmatype=?])
    
        MACD with controllable MA type (Momentum Indicators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            fastperiod: 12
            fastmatype: 0
            slowperiod: 26
            slowmatype: 0
            signalperiod: 9
            signalmatype: 0
        Outputs:
            macd
            macdsignal
            macdhist
        
    """
def MACDFIX(*args, **kwds):
    """
     MACDFIX(real[, signalperiod=?])
    
        Moving Average Convergence/Divergence Fix 12/26 (Momentum Indicators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            signalperiod: 9
        Outputs:
            macd
            macdsignal
            macdhist
        
    """
def MAMA(*args, **kwds):
    """
     MAMA(real[, fastlimit=?, slowlimit=?])
    
        MESA Adaptive Moving Average (Overlap Studies)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            fastlimit: 0.5
            slowlimit: 0.05
        Outputs:
            mama
            fama
        
    """
def MAVP(*args, **kwds):
    """
     MAVP(real, periods[, minperiod=?, maxperiod=?, matype=?])
    
        Moving average with variable period (Overlap Studies)
    
        Inputs:
            real: (any ndarray)
            periods: (any ndarray)
        Parameters:
            minperiod: 2
            maxperiod: 30
            matype: 0 (Simple Moving Average)
        Outputs:
            real
        
    """
def MAX(*args, **kwds):
    """
     MAX(real[, timeperiod=?])
    
        Highest value over a specified period (Math Operators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            real
        
    """
def MAXINDEX(*args, **kwds):
    """
     MAXINDEX(real[, timeperiod=?])
    
        Index of highest value over a specified period (Math Operators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def MEDPRICE(*args, **kwds):
    """
     MEDPRICE(high, low)
    
        Median Price (Price Transform)
    
        Inputs:
            prices: ['high', 'low']
        Outputs:
            real
        
    """
def MFI(*args, **kwds):
    """
     MFI(high, low, close, volume[, timeperiod=?])
    
        Money Flow Index (Momentum Indicators)
    
        Inputs:
            prices: ['high', 'low', 'close', 'volume']
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def MIDPOINT(*args, **kwds):
    """
     MIDPOINT(real[, timeperiod=?])
    
        MidPoint over period (Overlap Studies)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def MIDPRICE(*args, **kwds):
    """
     MIDPRICE(high, low[, timeperiod=?])
    
        Midpoint Price over period (Overlap Studies)
    
        Inputs:
            prices: ['high', 'low']
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def MIN(*args, **kwds):
    """
     MIN(real[, timeperiod=?])
    
        Lowest value over a specified period (Math Operators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            real
        
    """
def MININDEX(*args, **kwds):
    """
     MININDEX(real[, timeperiod=?])
    
        Index of lowest value over a specified period (Math Operators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def MINMAX(*args, **kwds):
    """
     MINMAX(real[, timeperiod=?])
    
        Lowest and highest values over a specified period (Math Operators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            min
            max
        
    """
def MINMAXINDEX(*args, **kwds):
    """
     MINMAXINDEX(real[, timeperiod=?])
    
        Indexes of lowest and highest values over a specified period (Math Operators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            minidx
            maxidx
        
    """
def MINUS_DI(*args, **kwds):
    """
     MINUS_DI(high, low, close[, timeperiod=?])
    
        Minus Directional Indicator (Momentum Indicators)
    
        Inputs:
            prices: ['high', 'low', 'close']
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def MINUS_DM(*args, **kwds):
    """
     MINUS_DM(high, low[, timeperiod=?])
    
        Minus Directional Movement (Momentum Indicators)
    
        Inputs:
            prices: ['high', 'low']
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def MOM(*args, **kwds):
    """
     MOM(real[, timeperiod=?])
    
        Momentum (Momentum Indicators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 10
        Outputs:
            real
        
    """
def MULT(*args, **kwds):
    """
     MULT(real0, real1)
    
        Vector Arithmetic Mult (Math Operators)
    
        Inputs:
            real0: (any ndarray)
            real1: (any ndarray)
        Outputs:
            real
        
    """
def NATR(*args, **kwds):
    """
     NATR(high, low, close[, timeperiod=?])
    
        Normalized Average True Range (Volatility Indicators)
    
        Inputs:
            prices: ['high', 'low', 'close']
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def OBV(*args, **kwds):
    """
     OBV(real, volume)
    
        On Balance Volume (Volume Indicators)
    
        Inputs:
            real: (any ndarray)
            prices: ['volume']
        Outputs:
            real
        
    """
def PLUS_DI(*args, **kwds):
    """
     PLUS_DI(high, low, close[, timeperiod=?])
    
        Plus Directional Indicator (Momentum Indicators)
    
        Inputs:
            prices: ['high', 'low', 'close']
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def PLUS_DM(*args, **kwds):
    """
     PLUS_DM(high, low[, timeperiod=?])
    
        Plus Directional Movement (Momentum Indicators)
    
        Inputs:
            prices: ['high', 'low']
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def PPO(*args, **kwds):
    """
     PPO(real[, fastperiod=?, slowperiod=?, matype=?])
    
        Percentage Price Oscillator (Momentum Indicators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            fastperiod: 12
            slowperiod: 26
            matype: 0 (Simple Moving Average)
        Outputs:
            real
        
    """
def ROC(*args, **kwds):
    """
     ROC(real[, timeperiod=?])
    
        Rate of change : ((real/prevPrice)-1)*100 (Momentum Indicators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 10
        Outputs:
            real
        
    """
def ROCP(*args, **kwds):
    """
     ROCP(real[, timeperiod=?])
    
        Rate of change Percentage: (real-prevPrice)/prevPrice (Momentum Indicators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 10
        Outputs:
            real
        
    """
def ROCR(*args, **kwds):
    """
     ROCR(real[, timeperiod=?])
    
        Rate of change ratio: (real/prevPrice) (Momentum Indicators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 10
        Outputs:
            real
        
    """
def ROCR100(*args, **kwds):
    """
     ROCR100(real[, timeperiod=?])
    
        Rate of change ratio 100 scale: (real/prevPrice)*100 (Momentum Indicators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 10
        Outputs:
            real
        
    """
def RSI(*args, **kwds):
    """
     RSI(real[, timeperiod=?])
    
        Relative Strength Index (Momentum Indicators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def SAR(*args, **kwds):
    """
     SAR(high, low[, acceleration=?, maximum=?])
    
        Parabolic SAR (Overlap Studies)
    
        Inputs:
            prices: ['high', 'low']
        Parameters:
            acceleration: 0.02
            maximum: 0.2
        Outputs:
            real
        
    """
def SAREXT(*args, **kwds):
    """
     SAREXT(high, low[, startvalue=?, offsetonreverse=?, accelerationinitlong=?, accelerationlong=?, accelerationmaxlong=?, accelerationinitshort=?, accelerationshort=?, accelerationmaxshort=?])
    
        Parabolic SAR - Extended (Overlap Studies)
    
        Inputs:
            prices: ['high', 'low']
        Parameters:
            startvalue: 0.0
            offsetonreverse: 0.0
            accelerationinitlong: 0.02
            accelerationlong: 0.02
            accelerationmaxlong: 0.2
            accelerationinitshort: 0.02
            accelerationshort: 0.02
            accelerationmaxshort: 0.2
        Outputs:
            real
        
    """
def SIN(*args, **kwds):
    """
     SIN(real)
    
        Vector Trigonometric Sin (Math Transform)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            real
        
    """
def SINH(*args, **kwds):
    """
     SINH(real)
    
        Vector Trigonometric Sinh (Math Transform)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            real
        
    """
def SMA(*args, **kwds):
    """
     SMA(real[, timeperiod=?])
    
        Simple Moving Average (Overlap Studies)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            real
        
    """
def SQRT(*args, **kwds):
    """
     SQRT(real)
    
        Vector Square Root (Math Transform)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            real
        
    """
def STDDEV(*args, **kwds):
    """
     STDDEV(real[, timeperiod=?, nbdev=?])
    
        Standard Deviation (Statistic Functions)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 5
            nbdev: 1.0
        Outputs:
            real
        
    """
def STOCH(*args, **kwds):
    """
     STOCH(high, low, close[, fastk_period=?, slowk_period=?, slowk_matype=?, slowd_period=?, slowd_matype=?])
    
        Stochastic (Momentum Indicators)
    
        Inputs:
            prices: ['high', 'low', 'close']
        Parameters:
            fastk_period: 5
            slowk_period: 3
            slowk_matype: 0
            slowd_period: 3
            slowd_matype: 0
        Outputs:
            slowk
            slowd
        
    """
def STOCHF(*args, **kwds):
    """
     STOCHF(high, low, close[, fastk_period=?, fastd_period=?, fastd_matype=?])
    
        Stochastic Fast (Momentum Indicators)
    
        Inputs:
            prices: ['high', 'low', 'close']
        Parameters:
            fastk_period: 5
            fastd_period: 3
            fastd_matype: 0
        Outputs:
            fastk
            fastd
        
    """
def STOCHRSI(*args, **kwds):
    """
     STOCHRSI(real[, timeperiod=?, fastk_period=?, fastd_period=?, fastd_matype=?])
    
        Stochastic Relative Strength Index (Momentum Indicators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 14
            fastk_period: 5
            fastd_period: 3
            fastd_matype: 0
        Outputs:
            fastk
            fastd
        
    """
def SUB(*args, **kwds):
    """
     SUB(real0, real1)
    
        Vector Arithmetic Subtraction (Math Operators)
    
        Inputs:
            real0: (any ndarray)
            real1: (any ndarray)
        Outputs:
            real
        
    """
def SUM(*args, **kwds):
    """
     SUM(real[, timeperiod=?])
    
        Summation (Math Operators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            real
        
    """
def T3(*args, **kwds):
    """
     T3(real[, timeperiod=?, vfactor=?])
    
        Triple Exponential Moving Average (T3) (Overlap Studies)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 5
            vfactor: 0.7
        Outputs:
            real
        
    """
def TAN(*args, **kwds):
    """
     TAN(real)
    
        Vector Trigonometric Tan (Math Transform)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            real
        
    """
def TANH(*args, **kwds):
    """
     TANH(real)
    
        Vector Trigonometric Tanh (Math Transform)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            real
        
    """
def TEMA(*args, **kwds):
    """
     TEMA(real[, timeperiod=?])
    
        Triple Exponential Moving Average (Overlap Studies)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            real
        
    """
def TRANGE(*args, **kwds):
    """
     TRANGE(high, low, close)
    
        True Range (Volatility Indicators)
    
        Inputs:
            prices: ['high', 'low', 'close']
        Outputs:
            real
        
    """
def TRIMA(*args, **kwds):
    """
     TRIMA(real[, timeperiod=?])
    
        Triangular Moving Average (Overlap Studies)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            real
        
    """
def TRIX(*args, **kwds):
    """
     TRIX(real[, timeperiod=?])
    
        1-day Rate-Of-Change (ROC) of a Triple Smooth EMA (Momentum Indicators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            real
        
    """
def TSF(*args, **kwds):
    """
     TSF(real[, timeperiod=?])
    
        Time Series Forecast (Statistic Functions)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def TYPPRICE(*args, **kwds):
    """
     TYPPRICE(high, low, close)
    
        Typical Price (Price Transform)
    
        Inputs:
            prices: ['high', 'low', 'close']
        Outputs:
            real
        
    """
def ULTOSC(*args, **kwds):
    """
     ULTOSC(high, low, close[, timeperiod1=?, timeperiod2=?, timeperiod3=?])
    
        Ultimate Oscillator (Momentum Indicators)
    
        Inputs:
            prices: ['high', 'low', 'close']
        Parameters:
            timeperiod1: 7
            timeperiod2: 14
            timeperiod3: 28
        Outputs:
            real
        
    """
def VAR(*args, **kwds):
    """
     VAR(real[, timeperiod=?, nbdev=?])
    
        Variance (Statistic Functions)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 5
            nbdev: 1.0
        Outputs:
            real
        
    """
def WCLPRICE(*args, **kwds):
    """
     WCLPRICE(high, low, close)
    
        Weighted Close Price (Price Transform)
    
        Inputs:
            prices: ['high', 'low', 'close']
        Outputs:
            real
        
    """
def WILLR(*args, **kwds):
    """
     WILLR(high, low, close[, timeperiod=?])
    
        Williams' %R (Momentum Indicators)
    
        Inputs:
            prices: ['high', 'low', 'close']
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def WMA(*args, **kwds):
    """
     WMA(real[, timeperiod=?])
    
        Weighted Moving Average (Overlap Studies)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            real
        
    """
def __get_flags(flag, flags_lookup_dict):
    """
    
        TA-LIB provides hints for multiple flags as a bitwise-ORed int.
        This function returns the flags from flag found in the provided
        flags_lookup_dict.
        
    """
def _get_defaults_and_docs(func_info):
    """
    
        Returns a tuple with two outputs: defaults, a dict of parameter defaults,
        and documentation, a formatted docstring for the function.
        .. Note: func_info should come from Function.info, *not* _ta_getFuncInfo.
        
    """
def _ta_check_success(function_name, ret_code):
    ...
def _ta_getFuncInfo(function_name):
    """
    
        Returns the info dict for the function. It has the following keys: name,
        group, help, flags, num_inputs, num_opt_inputs and num_outputs.
        
    """
def _ta_getFuncTable(group):
    """
    
        Returns a list of the functions for the specified group name. *slow*
        
    """
def _ta_getGroupTable():
    """
    
        Returns the list of available TALIB function group names. *slow*
        
    """
def _ta_getInputParameterInfo(function_name, idx):
    """
    
        Returns the function's input info dict for the given index. It has two
        keys: name and flags.
        
    """
def _ta_getOptInputParameterInfo(function_name, idx):
    """
    
        Returns the function's opt_input info dict for the given index. It has the
        following keys: name, display_name, type, help, default_value and value.
        
    """
def _ta_getOutputParameterInfo(function_name, idx):
    """
    
        Returns the function's output info dict for the given index. It has two
        keys: name and flags.
        
    """
def _ta_get_compatibility():
    ...
def _ta_get_unstable_period(name):
    ...
def _ta_initialize():
    ...
def _ta_restore_candle_default_settings(settingtype):
    ...
def _ta_set_candle_settings(settingtype, rangetype, avgperiod, factor):
    ...
def _ta_set_compatibility(value):
    ...
def _ta_set_unstable_period(name, period):
    ...
def _ta_shutdown():
    ...
def bytes2str(b):
    ...
def str2bytes(s):
    ...
def stream_ACOS(real):
    """
     ACOS(real)
    
        Vector Trigonometric ACos (Math Transform)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            real
        
    """
def stream_AD(high, low, close, volume):
    """
     AD(high, low, close, volume)
    
        Chaikin A/D Line (Volume Indicators)
    
        Inputs:
            prices: ['high', 'low', 'close', 'volume']
        Outputs:
            real
        
    """
def stream_ADD(real0, real1):
    """
     ADD(real0, real1)
    
        Vector Arithmetic Add (Math Operators)
    
        Inputs:
            real0: (any ndarray)
            real1: (any ndarray)
        Outputs:
            real
        
    """
def stream_ADOSC(high, low, close, volume, fastperiod = -2147483648, slowperiod = -2147483648):
    """
     ADOSC(high, low, close, volume[, fastperiod=?, slowperiod=?])
    
        Chaikin A/D Oscillator (Volume Indicators)
    
        Inputs:
            prices: ['high', 'low', 'close', 'volume']
        Parameters:
            fastperiod: 3
            slowperiod: 10
        Outputs:
            real
        
    """
def stream_ADX(high, low, close, timeperiod = -2147483648):
    """
     ADX(high, low, close[, timeperiod=?])
    
        Average Directional Movement Index (Momentum Indicators)
    
        Inputs:
            prices: ['high', 'low', 'close']
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def stream_ADXR(high, low, close, timeperiod = -2147483648):
    """
     ADXR(high, low, close[, timeperiod=?])
    
        Average Directional Movement Index Rating (Momentum Indicators)
    
        Inputs:
            prices: ['high', 'low', 'close']
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def stream_APO(real, fastperiod = -2147483648, slowperiod = -2147483648, matype = 0):
    """
     APO(real[, fastperiod=?, slowperiod=?, matype=?])
    
        Absolute Price Oscillator (Momentum Indicators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            fastperiod: 12
            slowperiod: 26
            matype: 0 (Simple Moving Average)
        Outputs:
            real
        
    """
def stream_AROON(high, low, timeperiod = -2147483648):
    """
     AROON(high, low[, timeperiod=?])
    
        Aroon (Momentum Indicators)
    
        Inputs:
            prices: ['high', 'low']
        Parameters:
            timeperiod: 14
        Outputs:
            aroondown
            aroonup
        
    """
def stream_AROONOSC(high, low, timeperiod = -2147483648):
    """
     AROONOSC(high, low[, timeperiod=?])
    
        Aroon Oscillator (Momentum Indicators)
    
        Inputs:
            prices: ['high', 'low']
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def stream_ASIN(real):
    """
     ASIN(real)
    
        Vector Trigonometric ASin (Math Transform)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            real
        
    """
def stream_ATAN(real):
    """
     ATAN(real)
    
        Vector Trigonometric ATan (Math Transform)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            real
        
    """
def stream_ATR(high, low, close, timeperiod = -2147483648):
    """
     ATR(high, low, close[, timeperiod=?])
    
        Average True Range (Volatility Indicators)
    
        Inputs:
            prices: ['high', 'low', 'close']
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def stream_AVGPRICE(open, high, low, close):
    """
     AVGPRICE(open, high, low, close)
    
        Average Price (Price Transform)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            real
        
    """
def stream_BBANDS(real, timeperiod = -2147483648, nbdevup = -4e+37, nbdevdn = -4e+37, matype = 0):
    """
     BBANDS(real[, timeperiod=?, nbdevup=?, nbdevdn=?, matype=?])
    
        Bollinger Bands (Overlap Studies)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 5
            nbdevup: 2.0
            nbdevdn: 2.0
            matype: 0 (Simple Moving Average)
        Outputs:
            upperband
            middleband
            lowerband
        
    """
def stream_BETA(real0, real1, timeperiod = -2147483648):
    """
     BETA(real0, real1[, timeperiod=?])
    
        Beta (Statistic Functions)
    
        Inputs:
            real0: (any ndarray)
            real1: (any ndarray)
        Parameters:
            timeperiod: 5
        Outputs:
            real
        
    """
def stream_BOP(open, high, low, close):
    """
     BOP(open, high, low, close)
    
        Balance Of Power (Momentum Indicators)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            real
        
    """
def stream_CCI(high, low, close, timeperiod = -2147483648):
    """
     CCI(high, low, close[, timeperiod=?])
    
        Commodity Channel Index (Momentum Indicators)
    
        Inputs:
            prices: ['high', 'low', 'close']
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def stream_CDL2CROWS(open, high, low, close):
    """
     CDL2CROWS(open, high, low, close)
    
        Two Crows (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDL3BLACKCROWS(open, high, low, close):
    """
     CDL3BLACKCROWS(open, high, low, close)
    
        Three Black Crows (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDL3INSIDE(open, high, low, close):
    """
     CDL3INSIDE(open, high, low, close)
    
        Three Inside Up/Down (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDL3LINESTRIKE(open, high, low, close):
    """
     CDL3LINESTRIKE(open, high, low, close)
    
        Three-Line Strike  (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDL3OUTSIDE(open, high, low, close):
    """
     CDL3OUTSIDE(open, high, low, close)
    
        Three Outside Up/Down (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDL3STARSINSOUTH(open, high, low, close):
    """
     CDL3STARSINSOUTH(open, high, low, close)
    
        Three Stars In The South (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDL3WHITESOLDIERS(open, high, low, close):
    """
     CDL3WHITESOLDIERS(open, high, low, close)
    
        Three Advancing White Soldiers (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLABANDONEDBABY(open, high, low, close, penetration = 0.3):
    """
     CDLABANDONEDBABY(open, high, low, close[, penetration=?])
    
        Abandoned Baby (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Parameters:
            penetration: 0.3
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLADVANCEBLOCK(open, high, low, close):
    """
     CDLADVANCEBLOCK(open, high, low, close)
    
        Advance Block (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLBELTHOLD(open, high, low, close):
    """
     CDLBELTHOLD(open, high, low, close)
    
        Belt-hold (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLBREAKAWAY(open, high, low, close):
    """
     CDLBREAKAWAY(open, high, low, close)
    
        Breakaway (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLCLOSINGMARUBOZU(open, high, low, close):
    """
     CDLCLOSINGMARUBOZU(open, high, low, close)
    
        Closing Marubozu (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLCONCEALBABYSWALL(open, high, low, close):
    """
     CDLCONCEALBABYSWALL(open, high, low, close)
    
        Concealing Baby Swallow (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLCOUNTERATTACK(open, high, low, close):
    """
     CDLCOUNTERATTACK(open, high, low, close)
    
        Counterattack (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLDARKCLOUDCOVER(open, high, low, close, penetration = 0.5):
    """
     CDLDARKCLOUDCOVER(open, high, low, close[, penetration=?])
    
        Dark Cloud Cover (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Parameters:
            penetration: 0.5
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLDOJI(open, high, low, close):
    """
     CDLDOJI(open, high, low, close)
    
        Doji (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLDOJISTAR(open, high, low, close):
    """
     CDLDOJISTAR(open, high, low, close)
    
        Doji Star (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLDRAGONFLYDOJI(open, high, low, close):
    """
     CDLDRAGONFLYDOJI(open, high, low, close)
    
        Dragonfly Doji (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLENGULFING(open, high, low, close):
    """
     CDLENGULFING(open, high, low, close)
    
        Engulfing Pattern (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLEVENINGDOJISTAR(open, high, low, close, penetration = 0.3):
    """
     CDLEVENINGDOJISTAR(open, high, low, close[, penetration=?])
    
        Evening Doji Star (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Parameters:
            penetration: 0.3
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLEVENINGSTAR(open, high, low, close, penetration = 0.3):
    """
     CDLEVENINGSTAR(open, high, low, close[, penetration=?])
    
        Evening Star (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Parameters:
            penetration: 0.3
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLGAPSIDESIDEWHITE(open, high, low, close):
    """
     CDLGAPSIDESIDEWHITE(open, high, low, close)
    
        Up/Down-gap side-by-side white lines (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLGRAVESTONEDOJI(open, high, low, close):
    """
     CDLGRAVESTONEDOJI(open, high, low, close)
    
        Gravestone Doji (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLHAMMER(open, high, low, close):
    """
     CDLHAMMER(open, high, low, close)
    
        Hammer (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLHANGINGMAN(open, high, low, close):
    """
     CDLHANGINGMAN(open, high, low, close)
    
        Hanging Man (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLHARAMI(open, high, low, close):
    """
     CDLHARAMI(open, high, low, close)
    
        Harami Pattern (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLHARAMICROSS(open, high, low, close):
    """
     CDLHARAMICROSS(open, high, low, close)
    
        Harami Cross Pattern (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLHIGHWAVE(open, high, low, close):
    """
     CDLHIGHWAVE(open, high, low, close)
    
        High-Wave Candle (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLHIKKAKE(open, high, low, close):
    """
     CDLHIKKAKE(open, high, low, close)
    
        Hikkake Pattern (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLHIKKAKEMOD(open, high, low, close):
    """
     CDLHIKKAKEMOD(open, high, low, close)
    
        Modified Hikkake Pattern (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLHOMINGPIGEON(open, high, low, close):
    """
     CDLHOMINGPIGEON(open, high, low, close)
    
        Homing Pigeon (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLIDENTICAL3CROWS(open, high, low, close):
    """
     CDLIDENTICAL3CROWS(open, high, low, close)
    
        Identical Three Crows (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLINNECK(open, high, low, close):
    """
     CDLINNECK(open, high, low, close)
    
        In-Neck Pattern (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLINVERTEDHAMMER(open, high, low, close):
    """
     CDLINVERTEDHAMMER(open, high, low, close)
    
        Inverted Hammer (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLKICKING(open, high, low, close):
    """
     CDLKICKING(open, high, low, close)
    
        Kicking (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLKICKINGBYLENGTH(open, high, low, close):
    """
     CDLKICKINGBYLENGTH(open, high, low, close)
    
        Kicking - bull/bear determined by the longer marubozu (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLLADDERBOTTOM(open, high, low, close):
    """
     CDLLADDERBOTTOM(open, high, low, close)
    
        Ladder Bottom (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLLONGLEGGEDDOJI(open, high, low, close):
    """
     CDLLONGLEGGEDDOJI(open, high, low, close)
    
        Long Legged Doji (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLLONGLINE(open, high, low, close):
    """
     CDLLONGLINE(open, high, low, close)
    
        Long Line Candle (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLMARUBOZU(open, high, low, close):
    """
     CDLMARUBOZU(open, high, low, close)
    
        Marubozu (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLMATCHINGLOW(open, high, low, close):
    """
     CDLMATCHINGLOW(open, high, low, close)
    
        Matching Low (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLMATHOLD(open, high, low, close, penetration = 0.5):
    """
     CDLMATHOLD(open, high, low, close[, penetration=?])
    
        Mat Hold (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Parameters:
            penetration: 0.5
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLMORNINGDOJISTAR(open, high, low, close, penetration = 0.3):
    """
     CDLMORNINGDOJISTAR(open, high, low, close[, penetration=?])
    
        Morning Doji Star (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Parameters:
            penetration: 0.3
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLMORNINGSTAR(open, high, low, close, penetration = 0.3):
    """
     CDLMORNINGSTAR(open, high, low, close[, penetration=?])
    
        Morning Star (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Parameters:
            penetration: 0.3
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLONNECK(open, high, low, close):
    """
     CDLONNECK(open, high, low, close)
    
        On-Neck Pattern (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLPIERCING(open, high, low, close):
    """
     CDLPIERCING(open, high, low, close)
    
        Piercing Pattern (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLRICKSHAWMAN(open, high, low, close):
    """
     CDLRICKSHAWMAN(open, high, low, close)
    
        Rickshaw Man (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLRISEFALL3METHODS(open, high, low, close):
    """
     CDLRISEFALL3METHODS(open, high, low, close)
    
        Rising/Falling Three Methods (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLSEPARATINGLINES(open, high, low, close):
    """
     CDLSEPARATINGLINES(open, high, low, close)
    
        Separating Lines (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLSHOOTINGSTAR(open, high, low, close):
    """
     CDLSHOOTINGSTAR(open, high, low, close)
    
        Shooting Star (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLSHORTLINE(open, high, low, close):
    """
     CDLSHORTLINE(open, high, low, close)
    
        Short Line Candle (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLSPINNINGTOP(open, high, low, close):
    """
     CDLSPINNINGTOP(open, high, low, close)
    
        Spinning Top (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLSTALLEDPATTERN(open, high, low, close):
    """
     CDLSTALLEDPATTERN(open, high, low, close)
    
        Stalled Pattern (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLSTICKSANDWICH(open, high, low, close):
    """
     CDLSTICKSANDWICH(open, high, low, close)
    
        Stick Sandwich (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLTAKURI(open, high, low, close):
    """
     CDLTAKURI(open, high, low, close)
    
        Takuri (Dragonfly Doji with very long lower shadow) (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLTASUKIGAP(open, high, low, close):
    """
     CDLTASUKIGAP(open, high, low, close)
    
        Tasuki Gap (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLTHRUSTING(open, high, low, close):
    """
     CDLTHRUSTING(open, high, low, close)
    
        Thrusting Pattern (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLTRISTAR(open, high, low, close):
    """
     CDLTRISTAR(open, high, low, close)
    
        Tristar Pattern (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLUNIQUE3RIVER(open, high, low, close):
    """
     CDLUNIQUE3RIVER(open, high, low, close)
    
        Unique 3 River (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLUPSIDEGAP2CROWS(open, high, low, close):
    """
     CDLUPSIDEGAP2CROWS(open, high, low, close)
    
        Upside Gap Two Crows (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CDLXSIDEGAP3METHODS(open, high, low, close):
    """
     CDLXSIDEGAP3METHODS(open, high, low, close)
    
        Upside/Downside Gap Three Methods (Pattern Recognition)
    
        Inputs:
            prices: ['open', 'high', 'low', 'close']
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_CEIL(real):
    """
     CEIL(real)
    
        Vector Ceil (Math Transform)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            real
        
    """
def stream_CMO(real, timeperiod = -2147483648):
    """
     CMO(real[, timeperiod=?])
    
        Chande Momentum Oscillator (Momentum Indicators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def stream_CORREL(real0, real1, timeperiod = -2147483648):
    """
     CORREL(real0, real1[, timeperiod=?])
    
        Pearson's Correlation Coefficient (r) (Statistic Functions)
    
        Inputs:
            real0: (any ndarray)
            real1: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            real
        
    """
def stream_COS(real):
    """
     COS(real)
    
        Vector Trigonometric Cos (Math Transform)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            real
        
    """
def stream_COSH(real):
    """
     COSH(real)
    
        Vector Trigonometric Cosh (Math Transform)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            real
        
    """
def stream_DEMA(real, timeperiod = -2147483648):
    """
     DEMA(real[, timeperiod=?])
    
        Double Exponential Moving Average (Overlap Studies)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            real
        
    """
def stream_DIV(real0, real1):
    """
     DIV(real0, real1)
    
        Vector Arithmetic Div (Math Operators)
    
        Inputs:
            real0: (any ndarray)
            real1: (any ndarray)
        Outputs:
            real
        
    """
def stream_DX(high, low, close, timeperiod = -2147483648):
    """
     DX(high, low, close[, timeperiod=?])
    
        Directional Movement Index (Momentum Indicators)
    
        Inputs:
            prices: ['high', 'low', 'close']
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def stream_EMA(real, timeperiod = -2147483648):
    """
     EMA(real[, timeperiod=?])
    
        Exponential Moving Average (Overlap Studies)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            real
        
    """
def stream_EXP(real):
    """
     EXP(real)
    
        Vector Arithmetic Exp (Math Transform)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            real
        
    """
def stream_FLOOR(real):
    """
     FLOOR(real)
    
        Vector Floor (Math Transform)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            real
        
    """
def stream_HT_DCPERIOD(real):
    """
     HT_DCPERIOD(real)
    
        Hilbert Transform - Dominant Cycle Period (Cycle Indicators)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            real
        
    """
def stream_HT_DCPHASE(real):
    """
     HT_DCPHASE(real)
    
        Hilbert Transform - Dominant Cycle Phase (Cycle Indicators)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            real
        
    """
def stream_HT_PHASOR(real):
    """
     HT_PHASOR(real)
    
        Hilbert Transform - Phasor Components (Cycle Indicators)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            inphase
            quadrature
        
    """
def stream_HT_SINE(real):
    """
     HT_SINE(real)
    
        Hilbert Transform - SineWave (Cycle Indicators)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            sine
            leadsine
        
    """
def stream_HT_TRENDLINE(real):
    """
     HT_TRENDLINE(real)
    
        Hilbert Transform - Instantaneous Trendline (Overlap Studies)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            real
        
    """
def stream_HT_TRENDMODE(real):
    """
     HT_TRENDMODE(real)
    
        Hilbert Transform - Trend vs Cycle Mode (Cycle Indicators)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_KAMA(real, timeperiod = -2147483648):
    """
     KAMA(real[, timeperiod=?])
    
        Kaufman Adaptive Moving Average (Overlap Studies)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            real
        
    """
def stream_LINEARREG(real, timeperiod = -2147483648):
    """
     LINEARREG(real[, timeperiod=?])
    
        Linear Regression (Statistic Functions)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def stream_LINEARREG_ANGLE(real, timeperiod = -2147483648):
    """
     LINEARREG_ANGLE(real[, timeperiod=?])
    
        Linear Regression Angle (Statistic Functions)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def stream_LINEARREG_INTERCEPT(real, timeperiod = -2147483648):
    """
     LINEARREG_INTERCEPT(real[, timeperiod=?])
    
        Linear Regression Intercept (Statistic Functions)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def stream_LINEARREG_SLOPE(real, timeperiod = -2147483648):
    """
     LINEARREG_SLOPE(real[, timeperiod=?])
    
        Linear Regression Slope (Statistic Functions)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def stream_LN(real):
    """
     LN(real)
    
        Vector Log Natural (Math Transform)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            real
        
    """
def stream_LOG10(real):
    """
     LOG10(real)
    
        Vector Log10 (Math Transform)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            real
        
    """
def stream_MA(real, timeperiod = -2147483648, matype = 0):
    """
     MA(real[, timeperiod=?, matype=?])
    
        Moving average (Overlap Studies)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
            matype: 0 (Simple Moving Average)
        Outputs:
            real
        
    """
def stream_MACD(real, fastperiod = -2147483648, slowperiod = -2147483648, signalperiod = -2147483648):
    """
     MACD(real[, fastperiod=?, slowperiod=?, signalperiod=?])
    
        Moving Average Convergence/Divergence (Momentum Indicators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            fastperiod: 12
            slowperiod: 26
            signalperiod: 9
        Outputs:
            macd
            macdsignal
            macdhist
        
    """
def stream_MACDEXT(real, fastperiod = -2147483648, fastmatype = 0, slowperiod = -2147483648, slowmatype = 0, signalperiod = -2147483648, signalmatype = 0):
    """
     MACDEXT(real[, fastperiod=?, fastmatype=?, slowperiod=?, slowmatype=?, signalperiod=?, signalmatype=?])
    
        MACD with controllable MA type (Momentum Indicators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            fastperiod: 12
            fastmatype: 0
            slowperiod: 26
            slowmatype: 0
            signalperiod: 9
            signalmatype: 0
        Outputs:
            macd
            macdsignal
            macdhist
        
    """
def stream_MACDFIX(real, signalperiod = -2147483648):
    """
     MACDFIX(real[, signalperiod=?])
    
        Moving Average Convergence/Divergence Fix 12/26 (Momentum Indicators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            signalperiod: 9
        Outputs:
            macd
            macdsignal
            macdhist
        
    """
def stream_MAMA(real, fastlimit = -4e+37, slowlimit = -4e+37):
    """
     MAMA(real[, fastlimit=?, slowlimit=?])
    
        MESA Adaptive Moving Average (Overlap Studies)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            fastlimit: 0.5
            slowlimit: 0.05
        Outputs:
            mama
            fama
        
    """
def stream_MAVP(real, periods, minperiod = -2147483648, maxperiod = -2147483648, matype = 0):
    """
     MAVP(real, periods[, minperiod=?, maxperiod=?, matype=?])
    
        Moving average with variable period (Overlap Studies)
    
        Inputs:
            real: (any ndarray)
            periods: (any ndarray)
        Parameters:
            minperiod: 2
            maxperiod: 30
            matype: 0 (Simple Moving Average)
        Outputs:
            real
        
    """
def stream_MAX(real, timeperiod = -2147483648):
    """
     MAX(real[, timeperiod=?])
    
        Highest value over a specified period (Math Operators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            real
        
    """
def stream_MAXINDEX(real, timeperiod = -2147483648):
    """
     MAXINDEX(real[, timeperiod=?])
    
        Index of highest value over a specified period (Math Operators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_MEDPRICE(high, low):
    """
     MEDPRICE(high, low)
    
        Median Price (Price Transform)
    
        Inputs:
            prices: ['high', 'low']
        Outputs:
            real
        
    """
def stream_MFI(high, low, close, volume, timeperiod = -2147483648):
    """
     MFI(high, low, close, volume[, timeperiod=?])
    
        Money Flow Index (Momentum Indicators)
    
        Inputs:
            prices: ['high', 'low', 'close', 'volume']
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def stream_MIDPOINT(real, timeperiod = -2147483648):
    """
     MIDPOINT(real[, timeperiod=?])
    
        MidPoint over period (Overlap Studies)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def stream_MIDPRICE(high, low, timeperiod = -2147483648):
    """
     MIDPRICE(high, low[, timeperiod=?])
    
        Midpoint Price over period (Overlap Studies)
    
        Inputs:
            prices: ['high', 'low']
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def stream_MIN(real, timeperiod = -2147483648):
    """
     MIN(real[, timeperiod=?])
    
        Lowest value over a specified period (Math Operators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            real
        
    """
def stream_MININDEX(real, timeperiod = -2147483648):
    """
     MININDEX(real[, timeperiod=?])
    
        Index of lowest value over a specified period (Math Operators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            integer (values are -100, 0 or 100)
        
    """
def stream_MINMAX(real, timeperiod = -2147483648):
    """
     MINMAX(real[, timeperiod=?])
    
        Lowest and highest values over a specified period (Math Operators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            min
            max
        
    """
def stream_MINMAXINDEX(real, timeperiod = -2147483648):
    """
     MINMAXINDEX(real[, timeperiod=?])
    
        Indexes of lowest and highest values over a specified period (Math Operators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            minidx
            maxidx
        
    """
def stream_MINUS_DI(high, low, close, timeperiod = -2147483648):
    """
     MINUS_DI(high, low, close[, timeperiod=?])
    
        Minus Directional Indicator (Momentum Indicators)
    
        Inputs:
            prices: ['high', 'low', 'close']
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def stream_MINUS_DM(high, low, timeperiod = -2147483648):
    """
     MINUS_DM(high, low[, timeperiod=?])
    
        Minus Directional Movement (Momentum Indicators)
    
        Inputs:
            prices: ['high', 'low']
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def stream_MOM(real, timeperiod = -2147483648):
    """
     MOM(real[, timeperiod=?])
    
        Momentum (Momentum Indicators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 10
        Outputs:
            real
        
    """
def stream_MULT(real0, real1):
    """
     MULT(real0, real1)
    
        Vector Arithmetic Mult (Math Operators)
    
        Inputs:
            real0: (any ndarray)
            real1: (any ndarray)
        Outputs:
            real
        
    """
def stream_NATR(high, low, close, timeperiod = -2147483648):
    """
     NATR(high, low, close[, timeperiod=?])
    
        Normalized Average True Range (Volatility Indicators)
    
        Inputs:
            prices: ['high', 'low', 'close']
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def stream_OBV(real, volume):
    """
     OBV(real, volume)
    
        On Balance Volume (Volume Indicators)
    
        Inputs:
            real: (any ndarray)
            prices: ['volume']
        Outputs:
            real
        
    """
def stream_PLUS_DI(high, low, close, timeperiod = -2147483648):
    """
     PLUS_DI(high, low, close[, timeperiod=?])
    
        Plus Directional Indicator (Momentum Indicators)
    
        Inputs:
            prices: ['high', 'low', 'close']
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def stream_PLUS_DM(high, low, timeperiod = -2147483648):
    """
     PLUS_DM(high, low[, timeperiod=?])
    
        Plus Directional Movement (Momentum Indicators)
    
        Inputs:
            prices: ['high', 'low']
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def stream_PPO(real, fastperiod = -2147483648, slowperiod = -2147483648, matype = 0):
    """
     PPO(real[, fastperiod=?, slowperiod=?, matype=?])
    
        Percentage Price Oscillator (Momentum Indicators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            fastperiod: 12
            slowperiod: 26
            matype: 0 (Simple Moving Average)
        Outputs:
            real
        
    """
def stream_ROC(real, timeperiod = -2147483648):
    """
     ROC(real[, timeperiod=?])
    
        Rate of change : ((real/prevPrice)-1)*100 (Momentum Indicators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 10
        Outputs:
            real
        
    """
def stream_ROCP(real, timeperiod = -2147483648):
    """
     ROCP(real[, timeperiod=?])
    
        Rate of change Percentage: (real-prevPrice)/prevPrice (Momentum Indicators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 10
        Outputs:
            real
        
    """
def stream_ROCR(real, timeperiod = -2147483648):
    """
     ROCR(real[, timeperiod=?])
    
        Rate of change ratio: (real/prevPrice) (Momentum Indicators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 10
        Outputs:
            real
        
    """
def stream_ROCR100(real, timeperiod = -2147483648):
    """
     ROCR100(real[, timeperiod=?])
    
        Rate of change ratio 100 scale: (real/prevPrice)*100 (Momentum Indicators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 10
        Outputs:
            real
        
    """
def stream_RSI(real, timeperiod = -2147483648):
    """
     RSI(real[, timeperiod=?])
    
        Relative Strength Index (Momentum Indicators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def stream_SAR(high, low, acceleration = 0.02, maximum = 0.2):
    """
     SAR(high, low[, acceleration=?, maximum=?])
    
        Parabolic SAR (Overlap Studies)
    
        Inputs:
            prices: ['high', 'low']
        Parameters:
            acceleration: 0.02
            maximum: 0.2
        Outputs:
            real
        
    """
def stream_SAREXT(high, low, startvalue = -4e+37, offsetonreverse = -4e+37, accelerationinitlong = -4e+37, accelerationlong = -4e+37, accelerationmaxlong = -4e+37, accelerationinitshort = -4e+37, accelerationshort = -4e+37, accelerationmaxshort = -4e+37):
    """
     SAREXT(high, low[, startvalue=?, offsetonreverse=?, accelerationinitlong=?, accelerationlong=?, accelerationmaxlong=?, accelerationinitshort=?, accelerationshort=?, accelerationmaxshort=?])
    
        Parabolic SAR - Extended (Overlap Studies)
    
        Inputs:
            prices: ['high', 'low']
        Parameters:
            startvalue: 0.0
            offsetonreverse: 0.0
            accelerationinitlong: 0.02
            accelerationlong: 0.02
            accelerationmaxlong: 0.2
            accelerationinitshort: 0.02
            accelerationshort: 0.02
            accelerationmaxshort: 0.2
        Outputs:
            real
        
    """
def stream_SIN(real):
    """
     SIN(real)
    
        Vector Trigonometric Sin (Math Transform)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            real
        
    """
def stream_SINH(real):
    """
     SINH(real)
    
        Vector Trigonometric Sinh (Math Transform)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            real
        
    """
def stream_SMA(real, timeperiod = -2147483648):
    """
     SMA(real[, timeperiod=?])
    
        Simple Moving Average (Overlap Studies)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            real
        
    """
def stream_SQRT(real):
    """
     SQRT(real)
    
        Vector Square Root (Math Transform)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            real
        
    """
def stream_STDDEV(real, timeperiod = -2147483648, nbdev = -4e+37):
    """
     STDDEV(real[, timeperiod=?, nbdev=?])
    
        Standard Deviation (Statistic Functions)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 5
            nbdev: 1.0
        Outputs:
            real
        
    """
def stream_STOCH(high, low, close, fastk_period = -2147483648, slowk_period = -2147483648, slowk_matype = 0, slowd_period = -2147483648, slowd_matype = 0):
    """
     STOCH(high, low, close[, fastk_period=?, slowk_period=?, slowk_matype=?, slowd_period=?, slowd_matype=?])
    
        Stochastic (Momentum Indicators)
    
        Inputs:
            prices: ['high', 'low', 'close']
        Parameters:
            fastk_period: 5
            slowk_period: 3
            slowk_matype: 0
            slowd_period: 3
            slowd_matype: 0
        Outputs:
            slowk
            slowd
        
    """
def stream_STOCHF(high, low, close, fastk_period = -2147483648, fastd_period = -2147483648, fastd_matype = 0):
    """
     STOCHF(high, low, close[, fastk_period=?, fastd_period=?, fastd_matype=?])
    
        Stochastic Fast (Momentum Indicators)
    
        Inputs:
            prices: ['high', 'low', 'close']
        Parameters:
            fastk_period: 5
            fastd_period: 3
            fastd_matype: 0
        Outputs:
            fastk
            fastd
        
    """
def stream_STOCHRSI(real, timeperiod = -2147483648, fastk_period = -2147483648, fastd_period = -2147483648, fastd_matype = 0):
    """
     STOCHRSI(real[, timeperiod=?, fastk_period=?, fastd_period=?, fastd_matype=?])
    
        Stochastic Relative Strength Index (Momentum Indicators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 14
            fastk_period: 5
            fastd_period: 3
            fastd_matype: 0
        Outputs:
            fastk
            fastd
        
    """
def stream_SUB(real0, real1):
    """
     SUB(real0, real1)
    
        Vector Arithmetic Subtraction (Math Operators)
    
        Inputs:
            real0: (any ndarray)
            real1: (any ndarray)
        Outputs:
            real
        
    """
def stream_SUM(real, timeperiod = -2147483648):
    """
     SUM(real[, timeperiod=?])
    
        Summation (Math Operators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            real
        
    """
def stream_T3(real, timeperiod = -2147483648, vfactor = -4e+37):
    """
     T3(real[, timeperiod=?, vfactor=?])
    
        Triple Exponential Moving Average (T3) (Overlap Studies)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 5
            vfactor: 0.7
        Outputs:
            real
        
    """
def stream_TAN(real):
    """
     TAN(real)
    
        Vector Trigonometric Tan (Math Transform)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            real
        
    """
def stream_TANH(real):
    """
     TANH(real)
    
        Vector Trigonometric Tanh (Math Transform)
    
        Inputs:
            real: (any ndarray)
        Outputs:
            real
        
    """
def stream_TEMA(real, timeperiod = -2147483648):
    """
     TEMA(real[, timeperiod=?])
    
        Triple Exponential Moving Average (Overlap Studies)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            real
        
    """
def stream_TRANGE(high, low, close):
    """
     TRANGE(high, low, close)
    
        True Range (Volatility Indicators)
    
        Inputs:
            prices: ['high', 'low', 'close']
        Outputs:
            real
        
    """
def stream_TRIMA(real, timeperiod = -2147483648):
    """
     TRIMA(real[, timeperiod=?])
    
        Triangular Moving Average (Overlap Studies)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            real
        
    """
def stream_TRIX(real, timeperiod = -2147483648):
    """
     TRIX(real[, timeperiod=?])
    
        1-day Rate-Of-Change (ROC) of a Triple Smooth EMA (Momentum Indicators)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            real
        
    """
def stream_TSF(real, timeperiod = -2147483648):
    """
     TSF(real[, timeperiod=?])
    
        Time Series Forecast (Statistic Functions)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def stream_TYPPRICE(high, low, close):
    """
     TYPPRICE(high, low, close)
    
        Typical Price (Price Transform)
    
        Inputs:
            prices: ['high', 'low', 'close']
        Outputs:
            real
        
    """
def stream_ULTOSC(high, low, close, timeperiod1 = -2147483648, timeperiod2 = -2147483648, timeperiod3 = -2147483648):
    """
     ULTOSC(high, low, close[, timeperiod1=?, timeperiod2=?, timeperiod3=?])
    
        Ultimate Oscillator (Momentum Indicators)
    
        Inputs:
            prices: ['high', 'low', 'close']
        Parameters:
            timeperiod1: 7
            timeperiod2: 14
            timeperiod3: 28
        Outputs:
            real
        
    """
def stream_VAR(real, timeperiod = -2147483648, nbdev = -4e+37):
    """
     VAR(real[, timeperiod=?, nbdev=?])
    
        Variance (Statistic Functions)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 5
            nbdev: 1.0
        Outputs:
            real
        
    """
def stream_WCLPRICE(high, low, close):
    """
     WCLPRICE(high, low, close)
    
        Weighted Close Price (Price Transform)
    
        Inputs:
            prices: ['high', 'low', 'close']
        Outputs:
            real
        
    """
def stream_WILLR(high, low, close, timeperiod = -2147483648):
    """
     WILLR(high, low, close[, timeperiod=?])
    
        Williams' %R (Momentum Indicators)
    
        Inputs:
            prices: ['high', 'low', 'close']
        Parameters:
            timeperiod: 14
        Outputs:
            real
        
    """
def stream_WMA(real, timeperiod = -2147483648):
    """
     WMA(real[, timeperiod=?])
    
        Weighted Moving Average (Overlap Studies)
    
        Inputs:
            real: (any ndarray)
        Parameters:
            timeperiod: 30
        Outputs:
            real
        
    """
CandleSettingType: CandleSettingType  # value = <talib._ta_lib.CandleSettingType object>
MA_Type: MA_Type  # value = <talib._ta_lib.MA_Type object>
RangeType: RangeType  # value = <talib._ta_lib.RangeType object>
TA_FUNC_FLAGS: dict = {16777216: 'Output scale same as input', 67108864: 'Output is over volume', 134217728: 'Function has an unstable period', 268435456: 'Output is a candlestick'}
TA_INPUT_FLAGS: dict = {1: 'open', 2: 'high', 4: 'low', 8: 'close', 16: 'volume', 32: 'openInterest', 64: 'timeStamp'}
TA_OUTPUT_FLAGS: dict = {1: 'Line', 2: 'Dotted Line', 4: 'Dashed Line', 8: 'Dot', 16: 'Histogram', 32: 'Pattern (Bool)', 64: 'Bull/Bear Pattern (Bearish < 0, Neutral = 0, Bullish > 0)', 128: 'Strength Pattern ([-200..-100] = Bearish, [-100..0] = Getting Bearish, 0 = Neutral, [0..100] = Getting Bullish, [100-200] = Bullish)', 256: 'Output can be positive', 512: 'Output can be negative', 1024: 'Output can be zero', 2048: 'Values represent an upper limit', 4096: 'Values represent a lower limit'}
__ARRAY_TYPES: tuple = (numpy.ndarray, pandas.core.series.Series)
__INPUT_ARRAYS_TYPES: tuple = (dict, pandas.core.frame.DataFrame)
__INPUT_PRICE_SERIES_DEFAULTS: dict = {'price': 'close', 'price0': 'high', 'price1': 'low', 'periods': 'periods'}
__POLARS_DATAFRAME = None
__POLARS_SERIES = None
__TA_FUNCTION_NAMES__: list = ['ACOS', 'AD', 'ADD', 'ADOSC', 'ADX', 'ADXR', 'APO', 'AROON', 'AROONOSC', 'ASIN', 'ATAN', 'ATR', 'AVGPRICE', 'BBANDS', 'BETA', 'BOP', 'CCI', 'CDL2CROWS', 'CDL3BLACKCROWS', 'CDL3INSIDE', 'CDL3LINESTRIKE', 'CDL3OUTSIDE', 'CDL3STARSINSOUTH', 'CDL3WHITESOLDIERS', 'CDLABANDONEDBABY', 'CDLADVANCEBLOCK', 'CDLBELTHOLD', 'CDLBREAKAWAY', 'CDLCLOSINGMARUBOZU', 'CDLCONCEALBABYSWALL', 'CDLCOUNTERATTACK', 'CDLDARKCLOUDCOVER', 'CDLDOJI', 'CDLDOJISTAR', 'CDLDRAGONFLYDOJI', 'CDLENGULFING', 'CDLEVENINGDOJISTAR', 'CDLEVENINGSTAR', 'CDLGAPSIDESIDEWHITE', 'CDLGRAVESTONEDOJI', 'CDLHAMMER', 'CDLHANGINGMAN', 'CDLHARAMI', 'CDLHARAMICROSS', 'CDLHIGHWAVE', 'CDLHIKKAKE', 'CDLHIKKAKEMOD', 'CDLHOMINGPIGEON', 'CDLIDENTICAL3CROWS', 'CDLINNECK', 'CDLINVERTEDHAMMER', 'CDLKICKING', 'CDLKICKINGBYLENGTH', 'CDLLADDERBOTTOM', 'CDLLONGLEGGEDDOJI', 'CDLLONGLINE', 'CDLMARUBOZU', 'CDLMATCHINGLOW', 'CDLMATHOLD', 'CDLMORNINGDOJISTAR', 'CDLMORNINGSTAR', 'CDLONNECK', 'CDLPIERCING', 'CDLRICKSHAWMAN', 'CDLRISEFALL3METHODS', 'CDLSEPARATINGLINES', 'CDLSHOOTINGSTAR', 'CDLSHORTLINE', 'CDLSPINNINGTOP', 'CDLSTALLEDPATTERN', 'CDLSTICKSANDWICH', 'CDLTAKURI', 'CDLTASUKIGAP', 'CDLTHRUSTING', 'CDLTRISTAR', 'CDLUNIQUE3RIVER', 'CDLUPSIDEGAP2CROWS', 'CDLXSIDEGAP3METHODS', 'CEIL', 'CMO', 'CORREL', 'COS', 'COSH', 'DEMA', 'DIV', 'DX', 'EMA', 'EXP', 'FLOOR', 'HT_DCPERIOD', 'HT_DCPHASE', 'HT_PHASOR', 'HT_SINE', 'HT_TRENDLINE', 'HT_TRENDMODE', 'KAMA', 'LINEARREG', 'LINEARREG_ANGLE', 'LINEARREG_INTERCEPT', 'LINEARREG_SLOPE', 'LN', 'LOG10', 'MA', 'MACD', 'MACDEXT', 'MACDFIX', 'MAMA', 'MAVP', 'MAX', 'MAXINDEX', 'MEDPRICE', 'MFI', 'MIDPOINT', 'MIDPRICE', 'MIN', 'MININDEX', 'MINMAX', 'MINMAXINDEX', 'MINUS_DI', 'MINUS_DM', 'MOM', 'MULT', 'NATR', 'OBV', 'PLUS_DI', 'PLUS_DM', 'PPO', 'ROC', 'ROCP', 'ROCR', 'ROCR100', 'RSI', 'SAR', 'SAREXT', 'SIN', 'SINH', 'SMA', 'SQRT', 'STDDEV', 'STOCH', 'STOCHF', 'STOCHRSI', 'SUB', 'SUM', 'T3', 'TAN', 'TANH', 'TEMA', 'TRANGE', 'TRIMA', 'TRIX', 'TSF', 'TYPPRICE', 'ULTOSC', 'VAR', 'WCLPRICE', 'WILLR', 'WMA']
__ta_version__: bytes  # value = b'0.4.0 (Nov 18 2023 16:34:42)'
__test__: dict = {}
_ta_func_unst_ids: dict = {'NONE': -1, 'ADX': 0, 'ADXR': 1, 'ATR': 2, 'CMO': 3, 'DX': 4, 'EMA': 5, 'HT_DCPERIOD': 6, 'HT_DCPHASE': 7, 'HT_PHASOR': 8, 'HT_SINE': 9, 'HT_TRENDLINE': 10, 'HT_TRENDMODE': 11, 'KAMA': 12, 'MAMA': 13, 'MFI': 14, 'MINUS_DI': 15, 'MINUS_DM': 16, 'NATR': 17, 'PLUS_DI': 18, 'PLUS_DM': 19, 'RSI': 20, 'STOCHRSI': 21, 'T3': 22, 'ALL': 23}
i: int = 23
name: str = 'WMA'
nan: float  # value = nan
