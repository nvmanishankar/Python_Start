def compound(gorwth_rate):
    growth_factor=[1+ rate for rate in growth_rates]

    product=1
    for factor in growth_factor:
        product*=factor
    n=len(growth_factor)
    geomentric_mean= product **(1/n)
    cagr=(geomentric_mean -1)*100
    return round(cagr,2)

    n=len(growth_factor)

growth_rates=[0.20,0.18,0.11,0.02,0.28]
print("Cagr:",compound(growth_rates),"%")