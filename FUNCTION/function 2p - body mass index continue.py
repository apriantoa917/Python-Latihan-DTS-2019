# 4.1.5.2 Creating functions | two-parameter functions

# added with metric units converter (convert lbs to kg & ft to m)

# 1 lb = 0.45359237 kg

def lbs_to_kg(lb):
    return lb * 0.45359237

# 1 ft = 0.3048 m, and 1 in = 2.54 cm = 0.0254 m

# inch = 0.0 -> default value for not assigned parameter

def ft_to_m(ft, inch = 0.0):
    return (ft * 0.3048) + (inch * 0.0254)

def bmi(weight, height):
    if weight < 20 or weight > 200 or \
        height < 1.0 or height > 2.5 :
            return None
    return weight / height ** 2

#testing

print(bmi(weight = lbs_to_kg(176), height = ft_to_m(5, 7)))
