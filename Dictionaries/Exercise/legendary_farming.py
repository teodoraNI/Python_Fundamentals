materials = {"shards": 0, "fragments": 0, "motes": 0}
current_materials = input().split()
obtained = False
while not obtained:
    for i in range(0, len(current_materials), 2):
        value = int(current_materials[i])
        key = current_materials[i+1].lower()
        if key not in materials.keys():
            materials[key] = 0
        materials[key] += value
        if materials["shards"] >= 250:
            materials[key] -= 250
            print("Shadowmourne obtained!")
            obtained = True
        elif materials["fragments"] >= 250:
            materials[key] -= 250
            print("Valanyr obtained!")
            obtained = True
        elif  materials["motes"] >= 250:
            materials[key] -= 250
            print("Dragonwrath obtained!")
            obtained = True
        if obtained:
            break
    if obtained:
        break
    current_materials = input().split()
for material, quantity in materials.items():
    print(f"{material}: {quantity}")




