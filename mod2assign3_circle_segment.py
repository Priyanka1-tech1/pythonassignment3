import math 
pi = 3.14159
def area_of_seg(r, ang): 
       area_of_sec= pi *(r * r) * (ang/360)       
       area_of_tri= 1 / 2 * (r * r) *math.sin((ang* pi) / 180) 
       return area_of_sec- area_of_tri; 
r=10.0
ang = 90.0
print("Area of min seg=",area_of_seg(r, ang)) 
print("Area of maj seg=", area_of_seg(r,(360 - ang))) 
