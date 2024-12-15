from enum import Enum
from typing import Dict, List, Set, Tuple
from BaseClasses import Location

class AgainstTheStormLocation(Location):
    game: str = "Against the Storm"

class ATSLocationClassification(Enum):
    basic = 1
    biome_rep = 2
    extra_trade = 3
    dlc = 4
    dlc_biome_rep = 5
    dlc_grove_expedition = 6
    species_rep = 7
    slurry_rep = 8
    derivative_rep = 9
    
# How to interpret these logic definitions:
# To reach a location, you need at least one item from each string. For example:
# ["A,B,C", "D,E"] means (A or B or C) and (D or E)
location_dict: Dict[str, Tuple[ATSLocationClassification, str]] = {
    "First Reputation through Resolve - Humans": (ATSLocationClassification.basic, ["Porridge,Biscuits,Pie,Coats", "Planks", "Bricks"], "First Resolve Reputation"),
    "First Reputation through Resolve - Beavers": (ATSLocationClassification.basic, ["Ale,Scrolls,Wine", "Planks", "Bricks", "Fabric"], "First Resolve Reputation"),
    "First Reputation through Resolve - Lizards": (ATSLocationClassification.basic, [], "First Resolve Reputation"),
    "First Reputation through Resolve - Harpies": (ATSLocationClassification.basic, [], "First Resolve Reputation"),
    "First Reputation through Resolve - Foxes": (ATSLocationClassification.basic, [], "First Resolve Reputation"),
    "First Reputation through Resolve - Frogs": (ATSLocationClassification.dlc, ["Bricks"], "First Resolve Reputation"),
    "50 Resolve - Humans": (ATSLocationClassification.basic, ["Porridge,Biscuits,Pie", "Coats", "Ale", "Incense", "Planks", "Fabric", "Bricks", "Purging Fire"], "50 Resolve"),
    "50 Resolve - Beavers": (ATSLocationClassification.basic, ["Biscuits,Pickled Goods", "Coats", "Ale", "Scrolls", "Wine", "Planks", "Fabric", "Bricks", "Purging Fire"], "50 Resolve"),
    "50 Resolve - Lizards": (ATSLocationClassification.basic, ["Jerky,Skewers,Pie", "Pickled Goods", "Boots", "Training Gear", "Planks", "Fabric", "Bricks", "Purging Fire"], "50 Resolve"),
    "50 Resolve - Harpies": (ATSLocationClassification.basic, ["Jerky", "Paste", "Coats", "Boots", "Scrolls", "Tea", "Planks", "Fabric", "Bricks", "Purging Fire"], "50 Resolve"),
    "50 Resolve - Foxes": (ATSLocationClassification.basic, ["Porridge,Skewers,Pickled Goods", "Boots", "Incense", "Tea", "Crystallized Dew", "Planks", "Fabric", "Bricks", "Purging Fire"], "50 Resolve"),
    "50 Resolve - Frogs": (ATSLocationClassification.dlc, ["Paste,Biscuits,Pie", "Boots", "Incense", "Wine", "Training Gear", "Planks", "Fabric", "Bricks", "Purging Fire"], "50 Resolve"),
    
    "1st Reputation - Royal Woodlands": (ATSLocationClassification.basic, [], "Royal Woodlands"),
    "2nd Reputation - Royal Woodlands": (ATSLocationClassification.biome_rep, ["Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "Royal Woodlands"),
    "3rd Reputation - Royal Woodlands": (ATSLocationClassification.biome_rep, ["Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "Royal Woodlands"),
    "4th Reputation - Royal Woodlands": (ATSLocationClassification.biome_rep, ["Planks,Bricks,Fabric", "Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "Royal Woodlands"),
    "5th Reputation - Royal Woodlands": (ATSLocationClassification.biome_rep, ["Planks,Bricks,Fabric", "Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish", "Purging Fire"], "Royal Woodlands"),
    "6th Reputation - Royal Woodlands": (ATSLocationClassification.biome_rep, ["Planks,Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Royal Woodlands"),
    "7th Reputation - Royal Woodlands": (ATSLocationClassification.biome_rep, ["Planks,Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Royal Woodlands"),
    "8th Reputation - Royal Woodlands": (ATSLocationClassification.biome_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Royal Woodlands"),
    "9th Reputation - Royal Woodlands": (ATSLocationClassification.biome_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Royal Woodlands"),
    "10th Reputation - Royal Woodlands": (ATSLocationClassification.biome_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Royal Woodlands"),
    "11th Reputation - Royal Woodlands": (ATSLocationClassification.biome_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Royal Woodlands"),
    "12th Reputation - Royal Woodlands": (ATSLocationClassification.biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Royal Woodlands"),
    "13th Reputation - Royal Woodlands": (ATSLocationClassification.biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Royal Woodlands"),
    "14th Reputation - Royal Woodlands": (ATSLocationClassification.biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Royal Woodlands"),
    "15th Reputation - Royal Woodlands": (ATSLocationClassification.biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Royal Woodlands"),
    "16th Reputation - Royal Woodlands": (ATSLocationClassification.biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Royal Woodlands"),
    "17th Reputation - Royal Woodlands": (ATSLocationClassification.biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Royal Woodlands"),
    "Victory - Royal Woodlands": (ATSLocationClassification.basic, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Royal Woodlands"),
    "1st Reputation - Coral Forest": (ATSLocationClassification.basic, [], "Coral Forest"),
    "2nd Reputation - Coral Forest": (ATSLocationClassification.biome_rep, ["Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "Coral Forest"),
    "3rd Reputation - Coral Forest": (ATSLocationClassification.biome_rep, ["Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "Coral Forest"),
    "4th Reputation - Coral Forest": (ATSLocationClassification.biome_rep, ["Planks,Bricks,Fabric", "Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "Coral Forest"),
    "5th Reputation - Coral Forest": (ATSLocationClassification.biome_rep, ["Planks,Bricks,Fabric", "Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish", "Purging Fire"], "Coral Forest"),
    "6th Reputation - Coral Forest": (ATSLocationClassification.biome_rep, ["Planks,Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Coral Forest"),
    "7th Reputation - Coral Forest": (ATSLocationClassification.biome_rep, ["Planks,Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Coral Forest"),
    "8th Reputation - Coral Forest": (ATSLocationClassification.biome_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Coral Forest"),
    "9th Reputation - Coral Forest": (ATSLocationClassification.biome_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Coral Forest"),
    "10th Reputation - Coral Forest": (ATSLocationClassification.biome_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Coral Forest"),
    "11th Reputation - Coral Forest": (ATSLocationClassification.biome_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Coral Forest"),
    "12th Reputation - Coral Forest": (ATSLocationClassification.biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Coral Forest"),
    "13th Reputation - Coral Forest": (ATSLocationClassification.biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Coral Forest"),
    "14th Reputation - Coral Forest": (ATSLocationClassification.biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Coral Forest"),
    "15th Reputation - Coral Forest": (ATSLocationClassification.biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Coral Forest"),
    "16th Reputation - Coral Forest": (ATSLocationClassification.biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Coral Forest"),
    "17th Reputation - Coral Forest": (ATSLocationClassification.biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Coral Forest"),
    "Victory - Coral Forest": (ATSLocationClassification.basic, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Coral Forest"),
    "1st Reputation - The Marshlands": (ATSLocationClassification.basic, [], "The Marshlands"),
    "2nd Reputation - The Marshlands": (ATSLocationClassification.biome_rep, ["Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "The Marshlands"),
    "3rd Reputation - The Marshlands": (ATSLocationClassification.biome_rep, ["Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "The Marshlands"),
    "4th Reputation - The Marshlands": (ATSLocationClassification.biome_rep, ["Planks,Bricks,Fabric", "Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "The Marshlands"),
    "5th Reputation - The Marshlands": (ATSLocationClassification.biome_rep, ["Planks,Bricks,Fabric", "Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish", "Purging Fire"], "The Marshlands"),
    "6th Reputation - The Marshlands": (ATSLocationClassification.biome_rep, ["Planks,Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "The Marshlands"),
    "7th Reputation - The Marshlands": (ATSLocationClassification.biome_rep, ["Planks,Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "The Marshlands"),
    "8th Reputation - The Marshlands": (ATSLocationClassification.biome_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "The Marshlands"),
    "9th Reputation - The Marshlands": (ATSLocationClassification.biome_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "The Marshlands"),
    "10th Reputation - The Marshlands": (ATSLocationClassification.biome_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "The Marshlands"),
    "11th Reputation - The Marshlands": (ATSLocationClassification.biome_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "The Marshlands"),
    "12th Reputation - The Marshlands": (ATSLocationClassification.biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "The Marshlands"),
    "13th Reputation - The Marshlands": (ATSLocationClassification.biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "The Marshlands"),
    "14th Reputation - The Marshlands": (ATSLocationClassification.biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "The Marshlands"),
    "15th Reputation - The Marshlands": (ATSLocationClassification.biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "The Marshlands"),
    "16th Reputation - The Marshlands": (ATSLocationClassification.biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "The Marshlands"),
    "17th Reputation - The Marshlands": (ATSLocationClassification.biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "The Marshlands"),
    "Victory - The Marshlands": (ATSLocationClassification.basic, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "The Marshlands"),
    "1st Reputation - Scarlet Orchard": (ATSLocationClassification.basic, [], "Scarlet Orchard"),
    "2nd Reputation - Scarlet Orchard": (ATSLocationClassification.biome_rep, ["Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "Scarlet Orchard"),
    "3rd Reputation - Scarlet Orchard": (ATSLocationClassification.biome_rep, ["Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "Scarlet Orchard"),
    "4th Reputation - Scarlet Orchard": (ATSLocationClassification.biome_rep, ["Planks,Bricks,Fabric", "Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "Scarlet Orchard"),
    "5th Reputation - Scarlet Orchard": (ATSLocationClassification.biome_rep, ["Planks,Bricks,Fabric", "Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish", "Purging Fire"], "Scarlet Orchard"),
    "6th Reputation - Scarlet Orchard": (ATSLocationClassification.biome_rep, ["Planks,Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Scarlet Orchard"),
    "7th Reputation - Scarlet Orchard": (ATSLocationClassification.biome_rep, ["Planks,Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Scarlet Orchard"),
    "8th Reputation - Scarlet Orchard": (ATSLocationClassification.biome_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Scarlet Orchard"),
    "9th Reputation - Scarlet Orchard": (ATSLocationClassification.biome_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Scarlet Orchard"),
    "10th Reputation - Scarlet Orchard": (ATSLocationClassification.biome_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Scarlet Orchard"),
    "11th Reputation - Scarlet Orchard": (ATSLocationClassification.biome_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Scarlet Orchard"),
    "12th Reputation - Scarlet Orchard": (ATSLocationClassification.biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Scarlet Orchard"),
    "13th Reputation - Scarlet Orchard": (ATSLocationClassification.biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Scarlet Orchard"),
    "14th Reputation - Scarlet Orchard": (ATSLocationClassification.biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Scarlet Orchard"),
    "15th Reputation - Scarlet Orchard": (ATSLocationClassification.biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Scarlet Orchard"),
    "16th Reputation - Scarlet Orchard": (ATSLocationClassification.biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Scarlet Orchard"),
    "17th Reputation - Scarlet Orchard": (ATSLocationClassification.biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Scarlet Orchard"),
    "Victory - Scarlet Orchard": (ATSLocationClassification.basic, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Scarlet Orchard"),
    "1st Reputation - Cursed Royal Woodlands": (ATSLocationClassification.basic, [], "Cursed Royal Woodlands"),
    "2nd Reputation - Cursed Royal Woodlands": (ATSLocationClassification.biome_rep, ["Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "Cursed Royal Woodlands"),
    "3rd Reputation - Cursed Royal Woodlands": (ATSLocationClassification.biome_rep, ["Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "Cursed Royal Woodlands"),
    "4th Reputation - Cursed Royal Woodlands": (ATSLocationClassification.biome_rep, ["Planks,Bricks,Fabric", "Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "Cursed Royal Woodlands"),
    "5th Reputation - Cursed Royal Woodlands": (ATSLocationClassification.biome_rep, ["Planks,Bricks,Fabric", "Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish", "Purging Fire"], "Cursed Royal Woodlands"),
    "6th Reputation - Cursed Royal Woodlands": (ATSLocationClassification.biome_rep, ["Planks,Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Cursed Royal Woodlands"),
    "7th Reputation - Cursed Royal Woodlands": (ATSLocationClassification.biome_rep, ["Planks,Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Cursed Royal Woodlands"),
    "8th Reputation - Cursed Royal Woodlands": (ATSLocationClassification.biome_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Cursed Royal Woodlands"),
    "9th Reputation - Cursed Royal Woodlands": (ATSLocationClassification.biome_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Cursed Royal Woodlands"),
    "10th Reputation - Cursed Royal Woodlands": (ATSLocationClassification.biome_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Cursed Royal Woodlands"),
    "11th Reputation - Cursed Royal Woodlands": (ATSLocationClassification.biome_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Cursed Royal Woodlands"),
    "12th Reputation - Cursed Royal Woodlands": (ATSLocationClassification.biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Cursed Royal Woodlands"),
    "13th Reputation - Cursed Royal Woodlands": (ATSLocationClassification.biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Cursed Royal Woodlands"),
    "14th Reputation - Cursed Royal Woodlands": (ATSLocationClassification.biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Cursed Royal Woodlands"),
    "15th Reputation - Cursed Royal Woodlands": (ATSLocationClassification.biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Cursed Royal Woodlands"),
    "16th Reputation - Cursed Royal Woodlands": (ATSLocationClassification.biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Cursed Royal Woodlands"),
    "17th Reputation - Cursed Royal Woodlands": (ATSLocationClassification.biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Cursed Royal Woodlands"),
    "Victory - Cursed Royal Woodlands": (ATSLocationClassification.basic, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Cursed Royal Woodlands"),
    "1st Reputation - Coastal Grove": (ATSLocationClassification.dlc, [], "Coastal Grove"),
    "2nd Reputation - Coastal Grove": (ATSLocationClassification.dlc_biome_rep, ["Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "Coastal Grove"),
    "3rd Reputation - Coastal Grove": (ATSLocationClassification.dlc_biome_rep, ["Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "Coastal Grove"),
    "4th Reputation - Coastal Grove": (ATSLocationClassification.dlc_biome_rep, ["Planks,Bricks,Fabric", "Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "Coastal Grove"),
    "5th Reputation - Coastal Grove": (ATSLocationClassification.dlc_biome_rep, ["Planks,Bricks,Fabric", "Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish", "Purging Fire"], "Coastal Grove"),
    "6th Reputation - Coastal Grove": (ATSLocationClassification.dlc_biome_rep, ["Planks,Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Coastal Grove"),
    "7th Reputation - Coastal Grove": (ATSLocationClassification.dlc_biome_rep, ["Planks,Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Coastal Grove"),
    "8th Reputation - Coastal Grove": (ATSLocationClassification.dlc_biome_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Coastal Grove"),
    "9th Reputation - Coastal Grove": (ATSLocationClassification.dlc_biome_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Coastal Grove"),
    "10th Reputation - Coastal Grove": (ATSLocationClassification.dlc_biome_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Coastal Grove"),
    "11th Reputation - Coastal Grove": (ATSLocationClassification.dlc_biome_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Coastal Grove"),
    "12th Reputation - Coastal Grove": (ATSLocationClassification.dlc_biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Coastal Grove"),
    "13th Reputation - Coastal Grove": (ATSLocationClassification.dlc_biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Coastal Grove"),
    "14th Reputation - Coastal Grove": (ATSLocationClassification.dlc_biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Coastal Grove"),
    "15th Reputation - Coastal Grove": (ATSLocationClassification.dlc_biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Coastal Grove"),
    "16th Reputation - Coastal Grove": (ATSLocationClassification.dlc_biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Coastal Grove"),
    "17th Reputation - Coastal Grove": (ATSLocationClassification.dlc_biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Coastal Grove"),
    "Victory - Coastal Grove": (ATSLocationClassification.dlc, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Coastal Grove"),
    "1st Reputation - Ashen Thicket": (ATSLocationClassification.dlc, [], "Ashen Thicket"),
    "2nd Reputation - Ashen Thicket": (ATSLocationClassification.dlc_biome_rep, ["Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "Ashen Thicket"),
    "3rd Reputation - Ashen Thicket": (ATSLocationClassification.dlc_biome_rep, ["Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "Ashen Thicket"),
    "4th Reputation - Ashen Thicket": (ATSLocationClassification.dlc_biome_rep, ["Planks,Bricks,Fabric", "Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "Ashen Thicket"),
    "5th Reputation - Ashen Thicket": (ATSLocationClassification.dlc_biome_rep, ["Planks,Bricks,Fabric", "Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish", "Purging Fire"], "Ashen Thicket"),
    "6th Reputation - Ashen Thicket": (ATSLocationClassification.dlc_biome_rep, ["Planks,Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Ashen Thicket"),
    "7th Reputation - Ashen Thicket": (ATSLocationClassification.dlc_biome_rep, ["Planks,Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Ashen Thicket"),
    "8th Reputation - Ashen Thicket": (ATSLocationClassification.dlc_biome_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Ashen Thicket"),
    "9th Reputation - Ashen Thicket": (ATSLocationClassification.dlc_biome_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Ashen Thicket"),
    "10th Reputation - Ashen Thicket": (ATSLocationClassification.dlc_biome_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Ashen Thicket"),
    "11th Reputation - Ashen Thicket": (ATSLocationClassification.dlc_biome_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Ashen Thicket"),
    "12th Reputation - Ashen Thicket": (ATSLocationClassification.dlc_biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Ashen Thicket"),
    "13th Reputation - Ashen Thicket": (ATSLocationClassification.dlc_biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Ashen Thicket"),
    "14th Reputation - Ashen Thicket": (ATSLocationClassification.dlc_biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Ashen Thicket"),
    "15th Reputation - Ashen Thicket": (ATSLocationClassification.dlc_biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Ashen Thicket"),
    "16th Reputation - Ashen Thicket": (ATSLocationClassification.dlc_biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Ashen Thicket"),
    "17th Reputation - Ashen Thicket": (ATSLocationClassification.dlc_biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Ashen Thicket"),
    "Victory - Ashen Thicket": (ATSLocationClassification.dlc, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Ashen Thicket"),
    "1st Reputation - Sealed Forest": (ATSLocationClassification.basic, [], "Sealed Forest"),
    "2nd Reputation - Sealed Forest": (ATSLocationClassification.biome_rep, ["Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "Sealed Forest"),
    "3rd Reputation - Sealed Forest": (ATSLocationClassification.biome_rep, ["Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "Sealed Forest"),
    "4th Reputation - Sealed Forest": (ATSLocationClassification.biome_rep, ["Planks,Bricks,Fabric", "Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "Sealed Forest"),
    "5th Reputation - Sealed Forest": (ATSLocationClassification.biome_rep, ["Planks,Bricks,Fabric", "Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish", "Purging Fire"], "Sealed Forest"),
    "6th Reputation - Sealed Forest": (ATSLocationClassification.biome_rep, ["Planks,Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Sealed Forest"),
    "7th Reputation - Sealed Forest": (ATSLocationClassification.biome_rep, ["Planks,Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Sealed Forest"),
    "8th Reputation - Sealed Forest": (ATSLocationClassification.biome_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Sealed Forest"),
    "9th Reputation - Sealed Forest": (ATSLocationClassification.biome_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Sealed Forest"),
    "10th Reputation - Sealed Forest": (ATSLocationClassification.biome_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Sealed Forest"),
    "11th Reputation - Sealed Forest": (ATSLocationClassification.biome_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Sealed Forest"),
    "12th Reputation - Sealed Forest": (ATSLocationClassification.biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Sealed Forest"),
    "13th Reputation - Sealed Forest": (ATSLocationClassification.biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Sealed Forest"),
    "14th Reputation - Sealed Forest": (ATSLocationClassification.biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Sealed Forest"),
    "15th Reputation - Sealed Forest": (ATSLocationClassification.biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Sealed Forest"),
    "16th Reputation - Sealed Forest": (ATSLocationClassification.biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Sealed Forest"),
    "17th Reputation - Sealed Forest": (ATSLocationClassification.biome_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Sealed Forest"),

    # Human - Planks, Bricks; Biscuits, Pie, Porridge; Ale, Incense
    # Beaver - Planks; Biscuits, Pickled Goods; Ale, Scrolls, Wine
    # Lizard - Bricks, Fabric; Jerky, Pickled Goods, Pie, Skewers; Training Gear
    # Harpy - Fabric; Jerky, Paste; Scrolls, Tea
    # Fox - Planks, Crystallized Dew; Pickled Goods, Porridge, Skewers; Incense, Tea
    # Frog - Bricks; Paste, Pie, Porridge; Training Gear, Incense, Wine

    # Food - If 2+ of the same food, we "Love" that food; we NEED a loved food for the last 3 reputation levels
    # Biscuits - Beaver, Human
    # Jerky - Lizard, Harpy
    # Porridge - Human, Fox, Frog
    # Skewers - Lizard, Fox
    # Paste - Harpy, Frog
    # Pie - Human, Lizard, Frog
    # Pickled Goods - Beaver, Fox, Lizard

    # Housing
    # Bricks - Human, Lizard, Frog
    # Fabric - Harpy, Lizard
    # Planks - Beaver, Fox, Human


    # Ale - Human, Beaver
    # Training Gear - Lizard, Frog
    # Incense - Human, Fox, Frog
    # Scrolls - Beaver, Harpy
    # Wine - Beaver, Frog
    # Tea - Harpy, Fox

    # Human Beaver Lizard
    # Planks, Bricks, Fabric
    # Jerky, Porridge, Skewers, Biscuits, Pie, Pickled Goods - Loves Biscuits, Pie, Pickled Goods
    # Ale, Training Gear, Incense, Scrolls, Wine
    "1st Reputation - Human Beaver Lizard": (ATSLocationClassification.species_rep, [], "Human Beaver Lizard"),
    "2nd Reputation - Human Beaver Lizard": (ATSLocationClassification.species_rep, ["Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "Human Beaver Lizard"),
    "3rd Reputation - Human Beaver Lizard": (ATSLocationClassification.species_rep, ["Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "Human Beaver Lizard"),
    "4th Reputation - Human Beaver Lizard": (ATSLocationClassification.species_rep, ["Planks,Bricks,Fabric", "Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "Human Beaver Lizard"),
    "5th Reputation - Human Beaver Lizard": (ATSLocationClassification.species_rep, ["Planks,Bricks,Fabric", "Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish", "Purging Fire"], "Human Beaver Lizard"),
    "6th Reputation - Human Beaver Lizard": (ATSLocationClassification.species_rep, ["Planks,Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods", "Purging Fire"], "Human Beaver Lizard"),
    "7th Reputation - Human Beaver Lizard": (ATSLocationClassification.species_rep, ["Planks,Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods", "Purging Fire"], "Human Beaver Lizard"),
    "8th Reputation - Human Beaver Lizard": (ATSLocationClassification.species_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods", "Purging Fire"], "Human Beaver Lizard"),
    "9th Reputation - Human Beaver Lizard": (ATSLocationClassification.species_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods", "Purging Fire"], "Human Beaver Lizard"),
    "10th Reputation - Human Beaver Lizard": (ATSLocationClassification.species_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine", "Purging Fire"], "Human Beaver Lizard"),
    "11th Reputation - Human Beaver Lizard": (ATSLocationClassification.species_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine", "Purging Fire"], "Human Beaver Lizard"),
    "12th Reputation - Human Beaver Lizard": (ATSLocationClassification.species_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine", "Purging Fire"], "Human Beaver Lizard"),
    "13th Reputation - Human Beaver Lizard": (ATSLocationClassification.species_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine", "Purging Fire"], "Human Beaver Lizard"),
    "14th Reputation - Human Beaver Lizard": (ATSLocationClassification.species_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine", "Purging Fire"], "Human Beaver Lizard"),
    "15th Reputation - Human Beaver Lizard": (ATSLocationClassification.species_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine", "Purging Fire"], "Human Beaver Lizard"),
    "16th Reputation - Human Beaver Lizard": (ATSLocationClassification.species_rep, ["Planks", "Bricks", "Fabric", "Biscuits,Pie,Pickled Goods", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine", "Purging Fire"], "Human Beaver Lizard"),
    "17th Reputation - Human Beaver Lizard": (ATSLocationClassification.species_rep, ["Planks", "Bricks", "Fabric", "Biscuits,Pie,Pickled Goods", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine", "Purging Fire"], "Human Beaver Lizard"),
    "Victory - Human Beaver Lizard": (ATSLocationClassification.species_rep, ["Planks", "Bricks", "Fabric", "Biscuits,Pie,Pickled Goods", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine", "Purging Fire"], "Human Beaver Lizard"),
    # Human Beaver Harpy
    # Planks, Bricks, Fabric
    # Jerky, Porridge, Biscuits, Pie, Pickled Goods, Paste - Loves Biscuits
    # Ale, Incense, Scrolls, Wine, Tea
    "1st Reputation - Human Beaver Harpy": (ATSLocationClassification.species_rep, [], "Human Beaver Harpy"),
    "2nd Reputation - Human Beaver Harpy": (ATSLocationClassification.species_rep, ["Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "Human Beaver Harpy"),
    "3rd Reputation - Human Beaver Harpy": (ATSLocationClassification.species_rep, ["Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "Human Beaver Harpy"),
    "4th Reputation - Human Beaver Harpy": (ATSLocationClassification.species_rep, ["Planks,Bricks,Fabric", "Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "Human Beaver Harpy"),
    "5th Reputation - Human Beaver Harpy": (ATSLocationClassification.species_rep, ["Planks,Bricks,Fabric", "Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish", "Purging Fire"], "Human Beaver Harpy"),
    "6th Reputation - Human Beaver Harpy": (ATSLocationClassification.species_rep, ["Planks,Bricks,Fabric", "Jerky,Porridge,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Human Beaver Harpy"),
    "7th Reputation - Human Beaver Harpy": (ATSLocationClassification.species_rep, ["Planks,Bricks,Fabric", "Jerky,Porridge,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Human Beaver Harpy"),
    "8th Reputation - Human Beaver Harpy": (ATSLocationClassification.species_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Human Beaver Harpy"),
    "9th Reputation - Human Beaver Harpy": (ATSLocationClassification.species_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Human Beaver Harpy"),
    "10th Reputation - Human Beaver Harpy": (ATSLocationClassification.species_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Human Beaver Harpy"),
    "11th Reputation - Human Beaver Harpy": (ATSLocationClassification.species_rep, ["Planks", "Bricks,Fabric", "Jerky,Porridge,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Human Beaver Harpy"),
    "12th Reputation - Human Beaver Harpy": (ATSLocationClassification.species_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Human Beaver Harpy"),
    "13th Reputation - Human Beaver Harpy": (ATSLocationClassification.species_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Human Beaver Harpy"),
    "14th Reputation - Human Beaver Harpy": (ATSLocationClassification.species_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Human Beaver Harpy"),
    "15th Reputation - Human Beaver Harpy": (ATSLocationClassification.species_rep, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Human Beaver Harpy"),
    "16th Reputation - Human Beaver Harpy": (ATSLocationClassification.species_rep, ["Planks", "Bricks", "Fabric", "Biscuits", "Amber,Tools", "Ale,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Human Beaver Harpy"),
    "17th Reputation - Human Beaver Harpy": (ATSLocationClassification.species_rep, ["Planks", "Bricks", "Fabric", "Biscuits", "Amber,Tools", "Ale,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Human Beaver Harpy"),
    "Victory - Human Beaver Harpy": (ATSLocationClassification.species_rep, ["Planks", "Bricks", "Fabric", "Biscuits", "Amber,Tools", "Ale,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Human Beaver Harpy"),
    # Human Beaver Fox
    # Planks, Bricks
    # Porridge, Skewers, Biscuits, Pie, Pickled Goods - Loves Porridge, Biscuits, Pickled Goods
    # Ale, Incense, Scrolls, Wine, Tea
    "1st Reputation - Human Beaver Fox": (ATSLocationClassification.species_rep, [], "Human Beaver Fox"),
    "2nd Reputation - Human Beaver Fox": (ATSLocationClassification.species_rep, ["Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "Human Beaver Fox"),
    "3rd Reputation - Human Beaver Fox": (ATSLocationClassification.species_rep, ["Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "Human Beaver Fox"),
    "4th Reputation - Human Beaver Fox": (ATSLocationClassification.species_rep, ["Planks,Bricks", "Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "Human Beaver Fox"),
    "5th Reputation - Human Beaver Fox": (ATSLocationClassification.species_rep, ["Planks,Bricks", "Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish", "Purging Fire"], "Human Beaver Fox"),
    "6th Reputation - Human Beaver Fox": (ATSLocationClassification.species_rep, ["Planks,Bricks", "Porridge,Skewers,Biscuits,Pie,Pickled Goods", "Purging Fire"], "Human Beaver Fox"),
    "7th Reputation - Human Beaver Fox": (ATSLocationClassification.species_rep, ["Planks,Bricks", "Porridge,Skewers,Biscuits,Pie,Pickled Goods", "Purging Fire"], "Human Beaver Fox"),
    "8th Reputation - Human Beaver Fox": (ATSLocationClassification.species_rep, ["Planks", "Bricks", "Porridge,Skewers,Biscuits,Pie,Pickled Goods", "Purging Fire"], "Human Beaver Fox"),
    "9th Reputation - Human Beaver Fox": (ATSLocationClassification.species_rep, ["Planks", "Bricks", "Porridge,Skewers,Biscuits,Pie,Pickled Goods", "Purging Fire"], "Human Beaver Fox"),
    "10th Reputation - Human Beaver Fox": (ATSLocationClassification.species_rep, ["Planks", "Bricks", "Porridge,Skewers,Biscuits,Pie,Pickled Goods", "Amber,Tools,Ale,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Human Beaver Fox"),
    "11th Reputation - Human Beaver Fox": (ATSLocationClassification.species_rep, ["Planks", "Bricks", "Porridge,Skewers,Biscuits,Pie,Pickled Goods", "Amber,Tools,Ale,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Human Beaver Fox"),
    "12th Reputation - Human Beaver Fox": (ATSLocationClassification.species_rep, ["Planks", "Bricks", "Fabric", "Porridge,Skewers,Biscuits,Pie,Pickled Goods", "Amber,Tools,Ale,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Human Beaver Fox"),
    "13th Reputation - Human Beaver Fox": (ATSLocationClassification.species_rep, ["Planks", "Bricks", "Fabric", "Porridge,Skewers,Biscuits,Pie,Pickled Goods", "Amber,Tools,Ale,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Human Beaver Fox"),
    "14th Reputation - Human Beaver Fox": (ATSLocationClassification.species_rep, ["Planks", "Bricks", "Fabric", "Porridge,Skewers,Biscuits,Pie,Pickled Goods", "Amber,Tools", "Ale,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Human Beaver Fox"),
    "15th Reputation - Human Beaver Fox": (ATSLocationClassification.species_rep, ["Planks", "Bricks", "Fabric", "Porridge,Skewers,Biscuits,Pie,Pickled Goods", "Amber,Tools", "Ale,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Human Beaver Fox"),
    "16th Reputation - Human Beaver Fox": (ATSLocationClassification.species_rep, ["Planks", "Bricks", "Fabric", "Porridge,Biscuits,Pickled Goods", "Amber,Tools", "Ale,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Human Beaver Fox"),
    "17th Reputation - Human Beaver Fox": (ATSLocationClassification.species_rep, ["Planks", "Bricks", "Fabric", "Porridge,Biscuits,Pickled Goods", "Amber,Tools", "Ale,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Human Beaver Fox"),
    "Victory - Human Beaver Fox": (ATSLocationClassification.species_rep, ["Planks", "Bricks", "Fabric", "Porridge,Biscuits,Pickled Goods", "Amber,Tools", "Ale,Incense,Scrolls,Wine,Tea", "Purging Fire"], "Human Beaver Fox"),
    # Human Beaver Frog
    # Planks, Bricks
    # Porridge, Biscuits, Pie, Pickled Goods, Paste - Loves Porridge, Pie, Biscuits
    # Ale, Training Gear, Incense, Scrolls, Wine
    "1st Reputation - Human Beaver Frog": (ATSLocationClassification.species_rep, [], "Human Beaver Frog"),
    "2nd Reputation - Human Beaver Frog": (ATSLocationClassification.species_rep, ["Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "Human Beaver Frog"),
    "3rd Reputation - Human Beaver Frog": (ATSLocationClassification.species_rep, ["Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "Human Beaver Frog"),
    "4th Reputation - Human Beaver Frog": (ATSLocationClassification.species_rep, ["Planks,Bricks", "Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "Human Beaver Frog"),
    "5th Reputation - Human Beaver Frog": (ATSLocationClassification.species_rep, ["Planks,Bricks", "Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish", "Purging Fire"], "Human Beaver Frog"),
    "6th Reputation - Human Beaver Frog": (ATSLocationClassification.species_rep, ["Planks,Bricks", "Porridge,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Human Beaver Frog"),
    "7th Reputation - Human Beaver Frog": (ATSLocationClassification.species_rep, ["Planks,Bricks", "Porridge,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Human Beaver Frog"),
    "8th Reputation - Human Beaver Frog": (ATSLocationClassification.species_rep, ["Planks", "Bricks", "Porridge,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Human Beaver Frog"),
    "9th Reputation - Human Beaver Frog": (ATSLocationClassification.species_rep, ["Planks", "Bricks", "Porridge,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Human Beaver Frog"),
    "10th Reputation - Human Beaver Frog": (ATSLocationClassification.species_rep, ["Planks", "Bricks", "Porridge,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine", "Purging Fire"], "Human Beaver Frog"),
    "11th Reputation - Human Beaver Frog": (ATSLocationClassification.species_rep, ["Planks", "Bricks", "Porridge,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine", "Purging Fire"], "Human Beaver Frog"),
    "12th Reputation - Human Beaver Frog": (ATSLocationClassification.species_rep, ["Planks", "Bricks", "Fabric", "Porridge,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine", "Purging Fire"], "Human Beaver Frog"),
    "13th Reputation - Human Beaver Frog": (ATSLocationClassification.species_rep, ["Planks", "Bricks", "Fabric", "Porridge,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools,Ale,Training Gear,Incense,Scrolls,Wine", "Purging Fire"], "Human Beaver Frog"),
    "14th Reputation - Human Beaver Frog": (ATSLocationClassification.species_rep, ["Planks", "Bricks", "Fabric", "Porridge,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine", "Purging Fire"], "Human Beaver Frog"),
    "15th Reputation - Human Beaver Frog": (ATSLocationClassification.species_rep, ["Planks", "Bricks", "Fabric", "Porridge,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine", "Purging Fire"], "Human Beaver Frog"),
    "16th Reputation - Human Beaver Frog": (ATSLocationClassification.species_rep, ["Planks", "Bricks", "Fabric", "Porridge,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine", "Purging Fire"], "Human Beaver Frog"),
    "17th Reputation - Human Beaver Frog": (ATSLocationClassification.species_rep, ["Planks", "Bricks", "Fabric", "Porridge,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine", "Purging Fire"], "Human Beaver Frog"),
    "Victory - Human Beaver Frog": (ATSLocationClassification.species_rep, ["Planks", "Bricks", "Fabric", "Porridge,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine", "Purging Fire"], "Human Beaver Frog"),
    # Human Lizard Harpy
    # Planks, Bricks, Fabric
    # Jerky, Porridge, Skewers, Biscuits, Pie, Pickled Goods, Paste - loves Jerky, Pie
    # Ale, Training Gear, Incense, Scrolls, Wine, Tea
    "1st Reputation - Human Lizard Harpy": (ATSLocationClassification.species_rep, [], "Human Lizard Harpy"),

    "Trade - 75 Berries": (ATSLocationClassification.extra_trade, ["Berries"], "Trade Routes"),
    "Trade - 75 Eggs": (ATSLocationClassification.extra_trade, ["Eggs"], "Trade Routes"),
    "Trade - 75 Insects": (ATSLocationClassification.extra_trade, ["Insects"], "Trade Routes"),
    "Trade - 75 Meat": (ATSLocationClassification.extra_trade, ["Meat"], "Trade Routes"),
    "Trade - 75 Mushrooms": (ATSLocationClassification.extra_trade, ["Mushrooms"], "Trade Routes"),
    "Trade - 75 Roots": (ATSLocationClassification.extra_trade, ["Roots"], "Trade Routes"),
    "Trade - 75 Vegetables": (ATSLocationClassification.extra_trade, ["Vegetables"], "Trade Routes"),
    "Trade - 75 Fish": (ATSLocationClassification.extra_trade, ["Fish"], "Trade Routes"),
    "Trade - 100 Biscuits": (ATSLocationClassification.extra_trade, ["Biscuits", "Planks", "Fabric", "Bricks"], "Trade Routes"),
    "Trade - 100 Jerky": (ATSLocationClassification.extra_trade, ["Jerky", "Planks", "Fabric", "Bricks"], "Trade Routes"),
    "Trade - 100 Pickled Goods": (ATSLocationClassification.extra_trade, ["Pickled Goods", "Planks", "Fabric", "Bricks"], "Trade Routes"),
    "Trade - 100 Pie": (ATSLocationClassification.extra_trade, ["Pie", "Planks", "Fabric", "Bricks"], "Trade Routes"),
    "Trade - 100 Porridge": (ATSLocationClassification.extra_trade, ["Porridge", "Planks", "Fabric", "Bricks"], "Trade Routes"),
    "Trade - 100 Skewers": (ATSLocationClassification.extra_trade, ["Skewers", "Planks", "Fabric", "Bricks"], "Trade Routes"),
    "Trade - 100 Paste": (ATSLocationClassification.extra_trade, ["Paste", "Planks", "Fabric", "Bricks"], "Trade Routes"),
    "Trade - 100 Coats": (ATSLocationClassification.extra_trade, ["Coats", "Planks", "Fabric", "Bricks"], "Trade Routes"),
    "Trade - 100 Boots": (ATSLocationClassification.extra_trade, ["Boots", "Planks", "Fabric", "Bricks"], "Trade Routes"),
    "Trade - 40 Bricks": (ATSLocationClassification.extra_trade, ["Bricks"], "Trade Routes"),
    "Trade - 40 Fabric": (ATSLocationClassification.extra_trade, ["Fabric"], "Trade Routes"),
    "Trade - 40 Planks": (ATSLocationClassification.extra_trade, ["Planks"], "Trade Routes"),
    "Trade - 30 Pipes": (ATSLocationClassification.extra_trade, ["Pipes", "Planks", "Fabric", "Bricks"], "Trade Routes"),
    "Trade - 75 Ale": (ATSLocationClassification.extra_trade, ["Ale", "Planks", "Fabric", "Bricks"], "Trade Routes"),
    "Trade - 75 Incense": (ATSLocationClassification.extra_trade, ["Incense", "Planks", "Fabric", "Bricks"], "Trade Routes"),
    "Trade - 75 Scrolls": (ATSLocationClassification.extra_trade, ["Scrolls", "Planks", "Fabric", "Bricks"], "Trade Routes"),
    "Trade - 75 Tea": (ATSLocationClassification.extra_trade, ["Tea", "Planks", "Fabric", "Bricks"], "Trade Routes"),
    "Trade - 75 Training Gear": (ATSLocationClassification.extra_trade, ["Training Gear", "Planks", "Fabric", "Bricks"], "Trade Routes"),
    "Trade - 75 Wine": (ATSLocationClassification.extra_trade, ["Wine", "Planks", "Fabric", "Bricks"], "Trade Routes"),
    "Trade - 75 Clay": (ATSLocationClassification.extra_trade, ["Clay"], "Trade Routes"),
    "Trade - 75 Copper Ore": (ATSLocationClassification.extra_trade, ["Copper Ore"], "Trade Routes"),
    "Trade - 75 Scales": (ATSLocationClassification.extra_trade, ["Scales"], "Trade Routes"),
    "Trade - 40 Crystallized Dew": (ATSLocationClassification.extra_trade, ["Crystallized Dew", "Planks", "Fabric", "Bricks"], "Trade Routes"),
    "Trade - 75 Grain": (ATSLocationClassification.extra_trade, ["Grain"], "Trade Routes"),
    "Trade - 75 Herbs": (ATSLocationClassification.extra_trade, ["Herbs"], "Trade Routes"),
    "Trade - 50 Leather": (ATSLocationClassification.extra_trade, ["Leather"], "Trade Routes"),
    "Trade - 75 Plant Fiber": (ATSLocationClassification.extra_trade, ["Plant Fiber"], "Trade Routes"),
    "Trade - 75 Algae": (ATSLocationClassification.extra_trade, ["Algae"], "Trade Routes"),
    "Trade - 75 Reeds": (ATSLocationClassification.extra_trade, ["Reeds"], "Trade Routes"),
    "Trade - 50 Resin": (ATSLocationClassification.extra_trade, ["Resin"], "Trade Routes"),
    "Trade - 75 Stone": (ATSLocationClassification.extra_trade, ["Stone"], "Trade Routes"),
    "Trade - 75 Salt": (ATSLocationClassification.extra_trade, ["Salt"], "Trade Routes"),
    "Trade - 75 Barrels": (ATSLocationClassification.extra_trade, ["Barrels", "Planks", "Fabric", "Bricks"], "Trade Routes"),
    "Trade - 40 Copper Bars": (ATSLocationClassification.extra_trade, ["Copper Bars", "Planks", "Fabric", "Bricks"], "Trade Routes"),
    "Trade - 75 Flour": (ATSLocationClassification.extra_trade, ["Flour", "Planks", "Fabric", "Bricks"], "Trade Routes"),
    "Trade - 75 Dye": (ATSLocationClassification.extra_trade, ["Dye", "Planks", "Fabric", "Bricks"], "Trade Routes"),
    "Trade - 75 Pottery": (ATSLocationClassification.extra_trade, ["Pottery", "Planks", "Fabric", "Bricks"], "Trade Routes"),
    "Trade - 50 Waterskins": (ATSLocationClassification.extra_trade, ["Waterskins", "Planks", "Fabric", "Bricks"], "Trade Routes"),
    "Trade - 3 Ancient Tablet": (ATSLocationClassification.extra_trade, ["Ancient Tablet", "Planks", "Fabric", "Bricks"], "Trade Routes"),
    "Trade - 75 Coal": (ATSLocationClassification.extra_trade, ["Coal"], "Trade Routes"),
    "Trade - 75 Oil": (ATSLocationClassification.extra_trade, ["Oil", "Planks", "Fabric", "Bricks"], "Trade Routes"),
    "Trade - 20 Purging Fire": (ATSLocationClassification.extra_trade, ["Purging Fire", "Planks", "Fabric", "Bricks"], "Trade Routes"),
    "Trade - 75 Sea Marrow": (ATSLocationClassification.extra_trade, ["Sea Marrow"], "Trade Routes"),
    "Trade - 30 Tools": (ATSLocationClassification.extra_trade, ["Tools", "Planks", "Fabric", "Bricks"], "Trade Routes"),

    "Trade - 5 Amber": (ATSLocationClassification.basic, ["Amber"], "Trade Routes"),
    "Trade - 50 Amber": (ATSLocationClassification.basic, ["Amber", "Pack of Provisions", "Planks"], "Trade Routes"),
    "Trade - 500 Amber": (ATSLocationClassification.basic, ["Amber", "Pack of Provisions", "Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Pack of Building Materials,Pack of Crops,Pack of Luxury Goods,Pack of Trade Goods", "Purging Fire"], "Trade Routes"),
    "Trade - 20 Pack of Building Materials": (ATSLocationClassification.basic, ["Pack of Building Materials"], "Trade Routes"),
    "Trade - 20 Pack of Crops": (ATSLocationClassification.basic, ["Pack of Crops"], "Trade Routes"),
    "Trade - 20 Pack of Provisions": (ATSLocationClassification.basic, ["Pack of Provisions"], "Trade Routes"),
    "Trade - 20 Pack of Luxury Goods": (ATSLocationClassification.basic, ["Pack of Luxury Goods", "Planks", "Bricks", "Fabric"], "Trade Routes"),
    "Trade - 20 Pack of Trade Goods": (ATSLocationClassification.basic, ["Pack of Trade Goods", "Planks", "Bricks", "Fabric"], "Trade Routes"),
    "Trade - 200 Drizzle Water": (ATSLocationClassification.basic, ["Planks", "Pipes"], "Trade Routes"),
    "Trade - 200 Clearance Water": (ATSLocationClassification.basic, ["Planks", "Pipes"], "Trade Routes"),
    "Trade - 200 Storm Water": (ATSLocationClassification.basic, ["Planks", "Pipes"], "Trade Routes"),

    "Reach level 1 standing with a neighbor": (ATSLocationClassification.basic, ["Amber", "Pack of Provisions"], "Trade Standing"),
    "Reach level 2 standing with a neighbor": (ATSLocationClassification.basic, ["Amber", "Pack of Provisions", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste"], "Trade Standing"),
    "Reach level 3 standing with a neighbor": (ATSLocationClassification.basic, ["Amber", "Planks,Fabric,Bricks", "Pack of Provisions", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Trade Standing"),
    "Reach level 4 standing with a neighbor": (ATSLocationClassification.basic, ["Amber", "Planks", "Fabric,Bricks", "Pack of Provisions", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire", "Pack of Building Materials,Pack of Crops,Pack of Luxury Goods,Pack of Trade Goods"], "Trade Standing"),
    "Reach level 5 standing with a neighbor": (ATSLocationClassification.basic, ["Amber", "Planks", "Fabric", "Bricks", "Pack of Provisions", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire", "Pack of Building Materials,Pack of Crops,Pack of Luxury Goods,Pack of Trade Goods"], "Trade Standing"),
    "Reach level 1 standing with ALL 4 neighbors": (ATSLocationClassification.basic, ["Amber", "Pack of Provisions", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste"], "Trade Standing"),
    "Reach level 2 standing with ALL 4 neighbors": (ATSLocationClassification.basic, ["Amber", "Planks,Fabric,Bricks", "Pack of Provisions", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire"], "Trade Standing"),
    "Reach level 3 standing with ALL 4 neighbors": (ATSLocationClassification.basic, ["Amber", "Planks", "Fabric,Bricks", "Pack of Provisions", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire", "Pack of Building Materials,Pack of Crops,Pack of Luxury Goods,Pack of Trade Goods"], "Trade Standing"),
    "Reach level 4 standing with ALL 4 neighbors": (ATSLocationClassification.basic, ["Amber", "Planks", "Fabric", "Bricks", "Pack of Provisions", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire", "Pack of Building Materials,Pack of Crops,Pack of Luxury Goods,Pack of Trade Goods"], "Trade Standing"),
    "Reach level 5 standing with ALL 4 neighbors": (ATSLocationClassification.basic, ["Amber", "Planks", "Fabric", "Bricks", "Pack of Provisions", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Purging Fire", "Pack of Building Materials", "Pack of Crops", "Pack of Luxury Goods", "Pack of Trade Goods"], "Trade Standing"),
    
    "Completed Order - 1st Pack": (ATSLocationClassification.basic, [], "Complete Orders"),
    "Completed Order - 2nd Pack": (ATSLocationClassification.basic, ["Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "Complete Orders"),
    "Completed Order - 3rd Pack": (ATSLocationClassification.basic, ["Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish", "Planks,Bricks,Fabric"], "Complete Orders"),
    "Completed Order - 4th Pack": (ATSLocationClassification.basic, ["Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Planks", "Bricks,Fabric"], "Complete Orders"),
    "Completed Order - 5th Pack": (ATSLocationClassification.basic, ["Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Planks", "Bricks,Fabric"], "Complete Orders"),
    "Completed Order - 6th Pack": (ATSLocationClassification.basic, ["Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Planks", "Bricks,Fabric", "Purging Fire"], "Complete Orders"),
    "Completed Order - 7th Pack": (ATSLocationClassification.basic, ["Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Planks", "Bricks,Fabric", "Purging Fire"], "Complete Orders"),
    "Completed Order - 8th Pack": (ATSLocationClassification.basic, ["Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Planks", "Bricks", "Fabric", "Purging Fire"], "Complete Orders"),
    "Completed Order - 9th Pack": (ATSLocationClassification.basic, ["Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Planks", "Bricks", "Fabric", "Amber,Tools", "Purging Fire"], "Complete Orders"),
    
    "Upgraded Hearth - 1st Tier": (ATSLocationClassification.basic, [], "Hearth Tier"),
    "Upgraded Hearth - 2nd Tier": (ATSLocationClassification.basic, ["Planks"], "Hearth Tier"),
    "Upgraded Hearth - 3rd Tier": (ATSLocationClassification.basic, ["Planks", "Fabric", "Bricks"], "Hearth Tier"),
    "Complete a Dangerous Glade Event": (ATSLocationClassification.basic, ["Tools", "Oil,Coal,Sea Marrow", "Incense,Scrolls,Tea", "Planks"], "Glade Event"),
    "Complete a Forbidden Glade Event": (ATSLocationClassification.basic, ["Tools", "Oil,Coal,Sea Marrow", "Incense,Scrolls,Tea", "Planks", "Bricks,Fabric", "Purging Fire"], "Glade Event"),
    "Complete a Glade Event with a Corruption tag": (ATSLocationClassification.basic, ["Tools", "Oil,Coal,Sea Marrow", "Incense,Scrolls,Tea", "Planks"], "Glade Event"),
    "Complete a Glade Event with an Empathy tag": (ATSLocationClassification.basic, ["Tools", "Oil,Coal,Sea Marrow", "Incense,Scrolls,Tea", "Planks"], "Glade Event"),
    "Complete a Glade Event with a Loyalty tag": (ATSLocationClassification.basic, ["Tools", "Berries,Eggs,Insects,Meat,Mushrooms,Roots,Vegetables,Fish"], "Glade Event"),
    "Have 20 Villagers in fully upgraded Housing - Humans": (ATSLocationClassification.basic, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire", "Pack of Building Materials", "Pack of Crops"], "20 Housed Villagers"),
    "Have 20 Villagers in fully upgraded Housing - Beavers": (ATSLocationClassification.basic, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire", "Pack of Building Materials", "Amber,Pack of Trade Goods"], "20 Housed Villagers"),
    "Have 20 Villagers in fully upgraded Housing - Lizards": (ATSLocationClassification.basic, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire", "Pack of Building Materials", "Jerky,Skewers"], "20 Housed Villagers"),
    "Have 20 Villagers in fully upgraded Housing - Harpies": (ATSLocationClassification.basic, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire", "Pack of Building Materials", "Dye"], "20 Housed Villagers"),
    "Have 20 Villagers in fully upgraded Housing - Foxes": (ATSLocationClassification.basic, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire", "Pack of Building Materials", "Resin", "Crystallized Dew"], "20 Housed Villagers"),
    "Have 20 Villagers in fully upgraded Housing - Frogs": (ATSLocationClassification.dlc, ["Planks", "Bricks", "Fabric", "Jerky,Porridge,Skewers,Biscuits,Pie,Pickled Goods,Paste", "Amber,Tools", "Ale,Training Gear,Incense,Scrolls,Wine,Tea", "Purging Fire", "Pack of Building Materials"], "20 Housed Villagers"),
    
    "Cursed Royal Woodlands - Appease a Calm Ghost": (ATSLocationClassification.basic, ["Planks", "Bricks", "Fabric", "Incense,Oil,Sea Marrow,Tools,Ancient Tablet"], "Cursed Royal Woodlands"),
    "Cursed Royal Woodlands - Appease an Angry Ghost": (ATSLocationClassification.basic, ["Planks", "Bricks", "Fabric", "Incense,Oil,Sea Marrow,Tools,Ancient Tablet"], "Cursed Royal Woodlands"),
    "The Marshlands - Harvest from an Ancient Proto Wheat": (ATSLocationClassification.basic, ["Planks", "Bricks", "Fabric"], "The Marshlands"),
    "The Marshlands - Harvest from a Dead Leviathan": (ATSLocationClassification.basic, ["Planks", "Bricks", "Fabric"], "The Marshlands"),
    "The Marshlands - Harvest from a Giant Proto Fungus": (ATSLocationClassification.basic, ["Planks", "Bricks", "Fabric"], "The Marshlands"),
    "Scarlet Orchard - Reconstruct the Sealed Spider": (ATSLocationClassification.basic, ["Planks", "Fabric", "Bricks", "Eggs,Meat,Roots,Berries,Mushrooms,Insects", "Incense,Scrolls,Tea,Resin", "Coal,Oil,Sea Marrow,Planks", "Stone,Copper Bars,Dye,Barrels,Incense", "Tools,Parts,Pipes"], "Scarlet Orchard"),
    "Scarlet Orchard - Reconstruct the Sea Snake": (ATSLocationClassification.basic, ["Planks", "Fabric", "Bricks", "Eggs,Meat,Roots,Berries,Mushrooms,Insects", "Incense,Scrolls,Tea,Resin", "Coal,Oil,Sea Marrow,Planks", "Stone,Copper Bars,Dye,Barrels,Incense", "Tools,Parts,Pipes"], "Scarlet Orchard"),
    "Scarlet Orchard - Reconstruct the Smoldering Scorpion": (ATSLocationClassification.basic, ["Planks", "Fabric", "Bricks", "Eggs,Meat,Roots,Berries,Mushrooms,Insects", "Incense,Scrolls,Tea,Resin", "Coal,Oil,Sea Marrow,Planks", "Stone,Copper Bars,Dye,Barrels,Incense", "Tools,Parts,Pipes"], "Scarlet Orchard"),
    "Ashen Thicket - Forge 1st Cornerstone": (ATSLocationClassification.dlc, [], "Ashen Thicket"),
    "Ashen Thicket - Forge 2nd Cornerstone": (ATSLocationClassification.dlc, ["Planks", "Bricks"], "Ashen Thicket"),
    "Ashen Thicket - Forge 3rd Cornerstone": (ATSLocationClassification.dlc, ["Planks", "Bricks", "Coal,Copper Ore,Salt"], "Ashen Thicket"),
    "Coastal Grove - 1st Expedition": (ATSLocationClassification.dlc_grove_expedition, ["Algae,Fish", "Roots,Berries,Insects,Mushrooms,Vegetables"], "Coastal Grove Expeditions"),
    "Coastal Grove - 2nd Expedition": (ATSLocationClassification.dlc_grove_expedition, ["Planks", "Algae,Fish", "Roots,Berries,Insects,Mushrooms,Vegetables"], "Coastal Grove Expeditions"),
    "Coastal Grove - 3rd Expedition": (ATSLocationClassification.dlc_grove_expedition, ["Planks", "Bricks", "Fabric", "Algae,Fish", "Roots,Berries,Insects,Mushrooms,Vegetables", "Paste,Skewers,Porridge"], "Coastal Grove Expeditions"),
    "Coastal Grove - 4th Expedition": (ATSLocationClassification.dlc_grove_expedition, ["Planks", "Bricks", "Fabric", "Purging Fire", "Algae,Fish", "Roots,Berries,Insects,Mushrooms,Vegetables", "Biscuits,Pie,Jerky,Pickled Goods", "Paste,Skewers,Porridge"], "Coastal Grove Expeditions"),
    "Coastal Grove - 5th Expedition": (ATSLocationClassification.dlc_grove_expedition, ["Planks", "Bricks", "Fabric", "Purging Fire", "Algae,Fish", "Roots,Berries,Insects,Mushrooms,Vegetables", "Biscuits,Pie,Jerky,Pickled Goods", "Paste,Skewers,Porridge"], "Coastal Grove Expeditions"),
    "Coastal Grove - 6th Expedition": (ATSLocationClassification.dlc_grove_expedition, ["Planks", "Bricks", "Fabric", "Purging Fire", "Algae,Fish", "Roots,Berries,Insects,Mushrooms,Vegetables", "Biscuits,Pie,Jerky,Pickled Goods", "Paste,Skewers,Porridge"], "Coastal Grove Expeditions"),
    "Coastal Grove - 7th Expedition": (ATSLocationClassification.dlc_grove_expedition, ["Planks", "Bricks", "Fabric", "Purging Fire", "Algae,Fish", "Roots,Berries,Insects,Mushrooms,Vegetables", "Biscuits,Pie,Jerky,Pickled Goods", "Paste,Skewers,Porridge", "Ale,Tea,Wine"], "Coastal Grove Expeditions"),
    "Coastal Grove - 8th Expedition": (ATSLocationClassification.dlc_grove_expedition, ["Planks", "Bricks", "Fabric", "Purging Fire", "Algae,Fish", "Roots,Berries,Insects,Mushrooms,Vegetables", "Biscuits,Pie,Jerky,Pickled Goods", "Paste,Skewers,Porridge", "Ale,Tea,Wine"], "Coastal Grove Expeditions"),
    "Coastal Grove - 9th Expedition": (ATSLocationClassification.dlc_grove_expedition, ["Planks", "Bricks", "Fabric", "Purging Fire", "Algae,Fish", "Roots,Berries,Insects,Mushrooms,Vegetables", "Biscuits,Pie,Jerky,Pickled Goods", "Paste,Skewers,Porridge", "Ale,Tea,Wine"], "Coastal Grove Expeditions"),
    "Coastal Grove - 10th Expedition": (ATSLocationClassification.dlc_grove_expedition, ["Planks", "Bricks", "Fabric", "Purging Fire", "Algae,Fish", "Roots,Berries,Insects,Mushrooms,Vegetables", "Biscuits,Pie,Jerky,Pickled Goods", "Paste,Skewers,Porridge", "Ale,Tea,Wine"], "Coastal Grove Expeditions"),
    "Coastal Grove - 11th Expedition": (ATSLocationClassification.dlc_grove_expedition, ["Planks", "Bricks", "Fabric", "Purging Fire", "Algae,Fish", "Roots,Berries,Insects,Mushrooms,Vegetables", "Biscuits,Pie,Jerky,Pickled Goods", "Paste,Skewers,Porridge", "Ale,Tea,Wine"], "Coastal Grove Expeditions"),
    "Coastal Grove - 12th Expedition": (ATSLocationClassification.dlc_grove_expedition, ["Planks", "Bricks", "Fabric", "Purging Fire", "Algae,Fish", "Roots,Berries,Insects,Mushrooms,Vegetables", "Biscuits,Pie,Jerky,Pickled Goods", "Paste,Skewers,Porridge", "Ale,Tea,Wine"], "Coastal Grove Expeditions"),
    "Coastal Grove - 13th Expedition": (ATSLocationClassification.dlc_grove_expedition, ["Planks", "Bricks", "Fabric", "Purging Fire", "Algae,Fish", "Roots,Berries,Insects,Mushrooms,Vegetables", "Biscuits,Pie,Jerky,Pickled Goods", "Paste,Skewers,Porridge", "Ale,Tea,Wine"], "Coastal Grove Expeditions"),
    "Coastal Grove - 14th Expedition": (ATSLocationClassification.dlc_grove_expedition, ["Planks", "Bricks", "Fabric", "Purging Fire", "Algae,Fish", "Roots,Berries,Insects,Mushrooms,Vegetables", "Biscuits,Pie,Jerky,Pickled Goods", "Paste,Skewers,Porridge", "Ale,Tea,Wine"], "Coastal Grove Expeditions"),
    "Coastal Grove - 15th Expedition": (ATSLocationClassification.dlc_grove_expedition, ["Planks", "Bricks", "Fabric", "Purging Fire", "Algae,Fish", "Roots,Berries,Insects,Mushrooms,Vegetables", "Biscuits,Pie,Jerky,Pickled Goods", "Paste,Skewers,Porridge", "Ale,Tea,Wine"], "Coastal Grove Expeditions"),
    "Coastal Grove - 16th Expedition": (ATSLocationClassification.dlc_grove_expedition, ["Planks", "Bricks", "Fabric", "Purging Fire", "Algae,Fish", "Roots,Berries,Insects,Mushrooms,Vegetables", "Biscuits,Pie,Jerky,Pickled Goods", "Paste,Skewers,Porridge", "Ale,Tea,Wine"], "Coastal Grove Expeditions"),
    "Coastal Grove - 17th Expedition": (ATSLocationClassification.dlc_grove_expedition, ["Planks", "Bricks", "Fabric", "Purging Fire", "Algae,Fish", "Roots,Berries,Insects,Mushrooms,Vegetables", "Biscuits,Pie,Jerky,Pickled Goods", "Paste,Skewers,Porridge", "Ale,Tea,Wine"], "Coastal Grove Expeditions"),
    "Coastal Grove - 18th Expedition": (ATSLocationClassification.dlc_grove_expedition, ["Planks", "Bricks", "Fabric", "Purging Fire", "Algae,Fish", "Roots,Berries,Insects,Mushrooms,Vegetables", "Biscuits,Pie,Jerky,Pickled Goods", "Paste,Skewers,Porridge", "Ale,Tea,Wine"], "Coastal Grove Expeditions"),
    "Coastal Grove - 19th Expedition": (ATSLocationClassification.dlc_grove_expedition, ["Planks", "Bricks", "Fabric", "Purging Fire", "Algae,Fish", "Roots,Berries,Insects,Mushrooms,Vegetables", "Biscuits,Pie,Jerky,Pickled Goods", "Paste,Skewers,Porridge", "Ale,Tea,Wine"], "Coastal Grove Expeditions"),
    "Coastal Grove - 20th Expedition": (ATSLocationClassification.dlc_grove_expedition, ["Planks", "Bricks", "Fabric", "Purging Fire", "Algae,Fish", "Roots,Berries,Insects,Mushrooms,Vegetables", "Biscuits,Pie,Jerky,Pickled Goods", "Paste,Skewers,Porridge", "Ale,Tea,Wine"], "Coastal Grove Expeditions"),
}

def get_location_name_groups(location_dict: Dict[str, Tuple[ATSLocationClassification, List[str], str]]):
    species_names = ["Humans", "Beavers", "Lizards", "Harpies", "Foxes", "Frogs"]
    location_groups: Dict[str, Set[str]] = {}
    for location_key, (_classification, _logic, location_group) in location_dict.items():
        if location_group in location_groups:
            location_groups[location_group].add(location_key)
        else:
            location_groups[location_group] = { location_key }
        
        # Create additional species groups
        for species in species_names:
            if species in location_key:
                location_group = species
                if location_group in location_groups:
                    location_groups[location_group].add(location_key)
                else:
                    location_groups[location_group] = { location_key }
        
    return location_groups
