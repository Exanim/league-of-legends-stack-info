def hs(initial_hp, number_of_procs, additional_hp_per_proc):
    for i in range(number_of_procs):
        initial_hp += initial_hp*0.006 + additional_hp_per_proc
        
    return initial_hp


# az elso hs proc elott meg van veve a wardstone
def hs_with_wardstone(initial_hp, number_of_procs, additional_hp_per_proc):
    initial_hp = initial_hp*1.2
    for i in range(number_of_procs):
        if (i == 0):
            initial_hp += initial_hp*0.006 + additional_hp_per_proc
        else:
            initial_hp += (initial_hp*0.006 + additional_hp_per_proc)*1.2
    return initial_hp


def h(hp, p):
    return hp*(1+0.006)**p



p = hs(3000, 1000, 12.5)
print("periodic deposit:", p)

ws = hs_with_wardstone(3000, 2000, 19.5)
print("ws:", ws)

print("ratio:", ws/p)
