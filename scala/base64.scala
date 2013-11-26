import org.apache.commons.codec.binary.Base64

def decode(data: Array[Byte]) = Base64.decodeBase64(data.getBytes("utf-8"))
