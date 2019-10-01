class kardus:
    def __init__(self,panjang,lebar,tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        
    def VolumeKardus(self):
        return (self.panjang * self.lebar * self.tinggi)
    
    def LuasPermukaanKardus(self):
        return( 2 * ( (self.panjang * self.lebar) + (self.panjang * self.lebar) + (self.lebar * self.tinggi) ))
    
    def MassaJenis(self,massa):
        return( massa / self.VolumeKardus())

KotakBiru = kardus(10,8,4)
print('Kotak Biru       : p = 10, l = 8, t =4')
print('Volume           :',KotakBiru.VolumeKardus())
print('Luas Permukaan   :',KotakBiru.LuasPermukaanKardus())
print('Massa Jenis      :',KotakBiru.MassaJenis(1))

print()

KotakMerah = kardus(15,5,1)
print('Kotak Merah       : p = 15, l = 5, t =1')
print('Volume           :',KotakMerah.VolumeKardus())
print('Luas Permukaan   :',KotakMerah.LuasPermukaanKardus())
print('Massa Jenis      :',KotakMerah.MassaJenis(1))