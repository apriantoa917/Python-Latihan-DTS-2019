# 4.1.5.5 Creating functions | right-angle triangles

def isItATriangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

# untuk rumus lengkap : 
#     https://edube.org/uploads/media/default/0001/01/1ba2517baae100429f0217f536819939b481cdb7.png -> rumus dasar heron
#     https://edube.org/uploads/media/default/0001/01/06d4ed184333e2f6def5b2ffcac9435c18fc325d.png
#     https://edube.org/uploads/media/default/0001/01/aac88ace1ce483bdbc5543fc19a29655e470b4f1.png


def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def fieldOfTriangle(a, b, c):
    if not isItATriangle(a, b, c):
        return None
    return heron(a, b, c)

print(fieldOfTriangle(1., 1., 2. ** .5))