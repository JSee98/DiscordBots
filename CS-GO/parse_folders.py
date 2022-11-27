import os
import itertools
from discord_components import DiscordComponents, ComponentsBot, Button, Select, SelectOption


def chunked_iterable(iterable, size):
    it = iter(iterable)
    while True:
        chunk = list(itertools.islice(it, size))
        if not chunk:
            break
        yield chunk


def get_chunks(iter, placeholder):
    li = list()
    iter.sort()
    for x in chunked_iterable(iter, 25):
        li.append(Select(placeholder=placeholder, options=[
                  SelectOption(label=y, value=y) for y in x]))
    return li


buildings = ['Apartment', 'ATC', 'Base Cooler', 'Boathouse', 'Bus Station Bench', 'Carnival', 'Castle', 'Civilian Barracks', 'Construction Crane', 'Construction Site', 'Containers', 'Factory', 'Farm', 'Firefighter', 'Garage', 'Gaurdhouse', 'Hangar', 'Headquarters', 'Hospital', 'Hotel', 'House',
             'Hunting', 'Kiosk', 'L-Shaped Barracks', 'Large Bus Stop', 'Lighthouse', 'Market', 'Medical', 'Mess Hall', 'Military Nests', 'Military Tents', 'Municipal', 'Narrow Barracks', 'New folder', 'Officers Barracks', 'Outhouse', 'Pier Crane', 'Police', 'Power Station', 'Prison', 'Pubs', 'Radar Building', 'Radio', 'Regimental Barracks', 'Repair center', 'Sawmill', 'Scaffolding', 'School', 'Shipwreck', 'Single-Room Barracks', 'Small Boat', 'Tower', 'Train Station', 'Two-Storey Barracks', 'Village', 'Warehouse', 'Water Station', 'Well', 'Workshop', 'Wrecks']
clothes = ['Bags', 'Boots', 'Ghille', 'Glasses', 'Gloves', 'Hats', 'Helmets',
           'Jackets', 'Masks', 'Military Cloths', 'Pants', 'Shirts', 'Shoes', 'Vests']
loot = ['Armbands', 'Bags', 'Base Supplies', 'Belts', 'Boots', 'Canned Goods', 'Communication', 'Fauna', 'Food _ Drink', 'Fuits _ Veggies', 'Ghille', 'Glasses', 'Gloves', 'Hats', 'Helmets',
        'Jackets', 'Lights', 'Masks', 'Medical', 'Navigation', 'Pants', 'Pelts', 'Repairs', 'Seeds', 'Shirts', 'Shoes', 'Snacks', 'Steaks', 'Storage', 'Tools', 'Vehicle Parts', 'Vests', 'Water']

tools = ['Barbed Wire', 'Crowbar', 'Fange', 'Hacksaw', 'Hammer', 'Hand Saw', 'Hatchet', 'Lock Pick', 'Metal Wire', 'Pickaxe',
         'Pipe Wrench', 'Pliers', 'Rope', 'Screwdriver', 'Shovel', 'Sledgehammer', 'Splitting Axe', 'Tire Iron', 'Wrench']

vehicles = ['Bikes', 'Bus', 'Cars', 'Trucks']

ammunition = ['.22 LR', '.308 WIN', '.357 Magnum', '.380 ACP', '.45 ACP', '12ga Buckshot', '12ga Rifled Slugs',
              '12ga Rubber Bullets', '5.45x39mm', '5.56x45mm', '762x39mm', '762x54mm', '9x19mm', '9x39mm', '9x39mm AP']

attachments = ['1PN51 Scope', 'ATOG 4x32 Scope', 'ATOG 6x48 Scope', 'Backup Iron Sights', 'Binoculars', 'Combat Sights', 'Handgun Scope', 'Hunting Scope', 'KA Lightweight Buttstock', 'KA Polymer Buttstock', 'KA Polymer Handguard', 'KA Rail Handguard', 'KA Wooden Buttstock', 'KA Wooden Handguard',
               'KAS-74U Lightweight Buttstock', 'Kobra Sights', 'M4-A1 Carry Handle Sights', 'M4-A1 CQB Buttstock', 'M4-A1 MP Buttstock', 'M4-A1 MP Handguard', 'M4-A1 Polymer Handguard', 'M4-A1 Rail Handguard', 'M4-A1 Telescopic Buttstock', 'Mini Sights', 'Normalized Suppressor', 'NV-PVS4 Scope', 'P1-87-L Scope', 'Pistol Suppressor', 'PSO-1 Scope', 'PU Scope', 'Rangefinder', 'RVN Sights', 'SG5-K Compensator', 'SG5-K Lightweight Buttstock', 'SG5-K Polymer Handguard', 'SG5-K Rail Handguard', 'Standardized Suppressor']

magazines = ['AKM Mags', 'CR-527 Mag', 'CR-61 Mag', 'CR-75 Mag', 'Deagle Mag', 'Famas Mag', 'FX-45 Mag', 'Glock19 Mag', 'IJ-70 Mag', 'KA-101 Mag', 'KA74 Mag',
             'Kolt1911 Mag', 'LAR Mag', 'M4A1 Mags', 'MKII Mag', 'Pioneer Mag', 'PP19 Mag', 'SG5-K Mag', 'Sporter Mag', 'SVAL Mag', 'USG-45 Mag', 'Vaiga Mags', 'VSD Mag', 'VSS Mag']

weapons = ['1. To do - Explosives', '2. To do - Automatic Rifles', '3. To do - Pistols', '4. To do - Shotguns', '5. To do - SubMachine Guns', '6. To do- Melee', '7. To do - Rifles', 'B95', 'BK-133', 'BK-18', 'BK-43', 'CR-527', 'CR-61', 'CR-75', 'Deagle', 'Famas', 'FX-45', 'Glock19', 'IJ-70',
           'KA-101', 'KA-74', 'KA-74u', 'KA-M', 'Kolt 1911', 'Kolt 1911 (engraved)', 'LAR', 'M16-A2', 'M4A1', 'M70 Tundra', 'MK II', 'Mosin 91-30', 'Pioneer', 'PP19', 'Repeater', 'Revolver', 'SG5-K', 'SKS', 'Sporter22', 'SVAL', 'SVD', 'USG-45', 'Vaiga', 'VSS']
