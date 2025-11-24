inventory = {"яблоко", "ключ", "карта"}

if 'ключ' in inventory:
    print('ключ в инвентаре')

if 'факел' not in inventory:
    inventory.add('факел')

inventory.remove('яблоко')

print(inventory)
