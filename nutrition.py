def calculate_nutritional_needs(age_group, trimester):
    nutritional_standards = {
        1: {"Kelompok Umur": "16 - 18 Tahun", "Berat Badan": 52, "Tinggi Badan": 159, "Energi": 2100, "Protein": 65, "Lemak": 70, "Karbohidrat": 300, "Serat": 29, "Air": 2150},
        2: {"Kelompok Umur": "19 - 29 tahun", "Berat Badan": 55, "Tinggi Badan": 159, "Energi": 2250, "Protein": 60, "Lemak": 65, "Karbohidrat": 360, "Serat": 32, "Air": 2350},
        3: {"Kelompok Umur": "30 - 49 tahun", "Berat Badan": 56, "Tinggi Badan": 158, "Energi": 2150, "Protein": 60, "Lemak": 60, "Karbohidrat": 340, "Serat": 30, "Air": 2350},
    }

    trimester_additions = {
        1: {"Trimester": "Trimester 1", "Energi": 180, "Protein": 1, "Lemak": 2.3, "Karbohidrat": 25, "Serat": 3, "Air": 300},
        2: {"Trimester": "Trimester 2", "Energi": 300, "Protein": 10, "Lemak": 2.3, "Karbohidrat": 40, "Serat": 4, "Air": 300},
        3: {"Trimester": "Trimester 3", "Energi": 300, "Protein": 30, "Lemak": 2.3, "Karbohidrat": 40, "Serat": 4, "Air": 300},
    }

    standard_nutrition = nutritional_standards[age_group]
    additional_nutrition = trimester_additions[trimester]

    total_nutrition = {key: standard_nutrition[key] + additional_nutrition[key] for key in standard_nutrition if key in additional_nutrition}

    return standard_nutrition["Kelompok Umur"], additional_nutrition["Trimester"], total_nutrition
