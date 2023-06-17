from inc_noesis import *

def registerNoesisTypes():
    handle = noesis.register("Diablo IV Texture", ".tex")
    noesis.setHandlerTypeCheck(handle, noepyCheckType)
    noesis.setHandlerLoadRGBA(handle, noepyLoadRGBA)   
    #noesis.logPopup()
    return 1

def noepyCheckType(data):
    return 1
    
def noepyLoadRGBA(data, texList):
    size = len(data)-6
    bs = NoeBitStream(data)
    
    bs.seek(0)
    fmeta = bs.readUShort()
    
    bs.seek(2)
    width = bs.readUShort()
    
    bs.seek(4)
    height = bs.readUShort()
    
    bs.seek(6)
    textureData = bs.readBytes(size) #read   

    if fmeta == 41:
        textureData = rapi.imageDecodeDXT(textureData, width, height, noesis.FOURCC_BC4)
        
    if fmeta == 42:
        textureData = rapi.imageDecodeDXT(textureData, width, height, noesis.FOURCC_BC5)
        
    if fmeta == 23:
        width = int(size / (height * 4))
        format = 'r8 g8 b8 a8'
        textureData = rapi.imageDecodeRaw(textureData, width, height, format)
        
    if fmeta == 46 or fmeta == 9:
        width = int(size / (height * 0.5))
        textureData = rapi.imageDecodeDXT(textureData, width, height, noesis.FOURCC_BC1)  

    if fmeta == 47 or fmeta == 48 or fmeta == 10:
        width = int(size / (height * 1))
        textureData = rapi.imageDecodeDXT(textureData, width, height, noesis.FOURCC_BC3)         
        
    if fmeta == 49:
        width = int(size / (height * 1))
        textureData = rapi.imageDecodeDXT(textureData, width, height, noesis.NOESISTEX_DXT5)
        
    texture = NoeTexture("tex", width, height, textureData, noesis.NOESISTEX_RGBA32)
    
    texList.append(texture)  
    return 1
