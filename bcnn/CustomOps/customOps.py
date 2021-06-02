import tensorflow.keras.backend as K

import CustomOps.tensorflowOps as tensorflowOps

def passthroughSign(x):
    return tensorflowOps.passthroughSignTF(x)

def passthroughTanh(x):
    return tensorflowOps.passthroughTanhTF(x)

def SetSession():
    tensorflowOps.SetSession()
