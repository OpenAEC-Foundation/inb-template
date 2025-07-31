import ifcopenshell
import ifcopenshell.util.placement
import time

start_time = time.time()

# IFC-bestand openen
ifc_file_path = "" # change \ for /
file_path = ifc_file_path.removesuffix(".ifc")
ifc_file = ifcopenshell.open(ifc_file_path)

# Invoervariabelen
target_name = 'FP_250_Type_FB_370kN'  # substring voor selectie van piles
peil = 1.000  # in meter t.o.v. N.A.P.
paalpunt_niveau = -23.000  # in meter t.o.v. N.A.P.
afhaklengte_mm = 350
afhaklengte = afhaklengte_mm / 1000  # in meter

# Initialisatie
pile_heights = {}  # z_mm → lijst van GlobalIds
matched_names = set()
all_names = set()

# Verzamelen
for pile in ifc_file.by_type('IfcPile'):
    if not pile.Name:
        continue

    all_names.add(pile.Name)

    if target_name in pile.Name:
        matched_names.add(pile.Name)

        if pile.ObjectPlacement:
            matrix = ifcopenshell.util.placement.get_local_placement(pile.ObjectPlacement)
            bovenkant_paal_mm = round(matrix[2][3])  # mm t.o.v. N.A.P.

            if bovenkant_paal_mm not in pile_heights:
                pile_heights[bovenkant_paal_mm] = []

            pile_heights[bovenkant_paal_mm].append(pile.GlobalId)

# Toon unieke pile-namen
print("\nUnieke pile-namen in het bestand:")
for name in sorted(all_names):
    print(f" - {name}")

# Toon gematchte namen
print(f"\nPile-namen die '{target_name}' bevatten:")
for name in sorted(matched_names):
    print(f" {name}")

# Analyse
if not pile_heights:
    print(f"\n⚠️ Geen palen gevonden waarvan de naam '{target_name}' bevat.")
else:
    print(f"\nHoogtes van bovenkant palen (in mm):")
    for height, ids in pile_heights.items():
        print(f"  • Hoogte {int(height)} mm – {len(ids)} paal/palen")

    if len(pile_heights) == 1:
        enige_hoogte_mm = list(pile_heights.keys())[0]
        bovenkant_paal_m = enige_hoogte_mm / 1000

        # Berekeningen
        paallengte_zonder_afhak = peil - paalpunt_niveau
        paallengte_met_afhak = paallengte_zonder_afhak + afhaklengte
        onderkant_paal_tov_peil = paalpunt_niveau - peil

        print(f"\nAlle gematchte palen hebben dezelfde bovenkant hoogte:")
        print(f" Bovenkant paal:                   {enige_hoogte_mm} mm ({bovenkant_paal_m:.3f} m t.o.v. N.A.P.)\n")

        print("Gebruikte invoerparameters:")
        print(f" - Peil:                           {peil:.3f} m t.o.v. N.A.P.")
        print(f" - Paalpuntniveau:                {paalpunt_niveau:.3f} m t.o.v. N.A.P.")
        print(f" - Afhaklengte:                   {afhaklengte_mm} mm ({afhaklengte:.3f} m)\n")

        print("Resultaten:")
        print(f" - Totale paallengte zonder afhak: {paallengte_zonder_afhak:.3f} m")
        print(f" - Totale paallengte met afhak:    {paallengte_met_afhak:.3f} m")
        print(f" - Onderkant paal t.o.v. peil:     {onderkant_paal_tov_peil:.3f} m")

    else:
        print(f"\n⚠️ Verschillende paalkoppen gevonden! Controleer de volgende hoogtes:")
        for height, ids in pile_heights.items():
            print(f"  → Hoogte {int(height)} mm: {len(ids)} palen – GlobalIds: {ids}")

print("\nKlaar in %.2f seconden" % (time.time() - start_time))
import ifcopenshell
import ifcopenshell.util.placement
import time

start_time = time.time()

# IFC-bestand openen
ifc_file_path = "//Driebm-nas/3bm/50_projecten/3_3BM_bouwtechniek/2321 Plan WHSD-locatie Oude-Tonge/70_BIM/2321_Constructie_Hal_Vierpolders.ifc"
file_path = ifc_file_path.removesuffix(".ifc")
ifc_file = ifcopenshell.open(ifc_file_path)

# Invoervariabelen
target_name = 'FP_250_Type_FB_370kN'  # substring voor selectie van piles
peil = 1.000  # in meter t.o.v. N.A.P.
paalpunt_niveau = -23.000  # in meter t.o.v. N.A.P.
afhaklengte_mm = 350
afhaklengte = afhaklengte_mm / 1000  # in meter

# Initialisatie
pile_heights = {}  # z_mm → lijst van GlobalIds
matched_names = set()
all_names = set()

# Verzamelen
for pile in ifc_file.by_type('IfcPile'):
    if not pile.Name:
        continue

    all_names.add(pile.Name)

    if target_name in pile.Name:
        matched_names.add(pile.Name)

        if pile.ObjectPlacement:
            matrix = ifcopenshell.util.placement.get_local_placement(pile.ObjectPlacement)
            bovenkant_paal_mm = round(matrix[2][3])  # mm t.o.v. N.A.P.

            if bovenkant_paal_mm not in pile_heights:
                pile_heights[bovenkant_paal_mm] = []

            pile_heights[bovenkant_paal_mm].append(pile.GlobalId)

# Toon unieke pile-namen
print("\nUnieke pile-namen in het bestand:")
for name in sorted(all_names):
    print(f" - {name}")

# Toon gematchte namen
print(f"\nPile-namen die '{target_name}' bevatten:")
for name in sorted(matched_names):
    print(f" {name}")

# Analyse
if not pile_heights:
    print(f"\n⚠️ Geen palen gevonden waarvan de naam '{target_name}' bevat.")
else:
    print(f"\nHoogtes van bovenkant palen (in mm):")
    for height, ids in pile_heights.items():
        print(f"  • Hoogte {int(height)} mm – {len(ids)} paal/palen")

    if len(pile_heights) == 1:
        enige_hoogte_mm = list(pile_heights.keys())[0]
        bovenkant_paal_m = enige_hoogte_mm / 1000

        # Berekeningen
        paallengte_zonder_afhak = peil - paalpunt_niveau
        paallengte_met_afhak = paallengte_zonder_afhak + afhaklengte
        onderkant_paal_tov_peil = paalpunt_niveau - peil

        print(f"\nAlle gematchte palen hebben dezelfde bovenkant hoogte:")
        print(f" Bovenkant paal:                   {enige_hoogte_mm} mm ({bovenkant_paal_m:.3f} m t.o.v. N.A.P.)\n")

        print("Gebruikte invoerparameters:")
        print(f" - Peil:                           {peil:.3f} m t.o.v. N.A.P.")
        print(f" - Paalpuntniveau:                {paalpunt_niveau:.3f} m t.o.v. N.A.P.")
        print(f" - Afhaklengte:                   {afhaklengte_mm} mm ({afhaklengte:.3f} m)\n")

        print("Resultaten:")
        print(f" - Totale paallengte zonder afhak: {paallengte_zonder_afhak:.3f} m")
        print(f" - Totale paallengte met afhak:    {paallengte_met_afhak:.3f} m")
        print(f" - Onderkant paal t.o.v. peil:     {onderkant_paal_tov_peil:.3f} m")

    else:
        print(f"\n⚠️ Verschillende paalkoppen gevonden! Controleer de volgende hoogtes:")
        for height, ids in pile_heights.items():
            print(f"  → Hoogte {int(height)} mm: {len(ids)} palen – GlobalIds: {ids}")

print("\nKlaar in %.2f seconden" % (time.time() - start_time))
