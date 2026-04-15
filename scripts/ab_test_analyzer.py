import math

def calculate_conversion_rate(clicks, conversions):
    return (conversions / clicks) * 100

def check_statistical_significance(clicks_a, conv_a, clicks_b, conv_b):
    """
    Упрощенный расчет Z-теста для проверки значимости А/Б теста.
    Цель: Понять, действительно ли AI-комментарии (Группа B) повышают CR.
    """
    cr_a = conv_a / clicks_a
    cr_b = conv_b / clicks_b
    
    # Расчет стандартной ошибки
    pooled_cr = (conv_a + conv_b) / (clicks_a + clicks_b)
    standard_error = math.sqrt(pooled_cr * (1 - pooled_cr) * (1/clicks_a + 1/clicks_b))
    
    # Расчет Z-score
    z_score = (cr_b - cr_a) / standard_error
    
    # Для доверительного интервала 95% Z-score должен быть > 1.645 (односторонний тест)
    is_significant = z_score > 1.645
    
    return round(z_score, 3), is_significant

# Данные эксперимента (имитация результатов за 14 дней)
# Группа А: Стандартный ИИ
# Группа B: ИИ + Обоснования «Почему это подходит вам»
results = {
    "Group_A": {"clicks": 10000, "conversions": 190}, # CR = 1.9%
    "Group_B": {"clicks": 10000, "conversions": 220}  # CR = 2.2% (Твой целевой KPI)
}

if __name__ == "__main__":
    z, significant = check_statistical_significance(
        results["Group_A"]["clicks"], results["Group_A"]["conversions"],
        results["Group_B"]["clicks"], results["Group_B"]["conversions"]
    )
    
    print(f"--- StyleGenie AI A/B Test Results ---")
    print(f"Group A Conversion: {calculate_conversion_rate(10000, 190)}%")
    print(f"Group B Conversion: {calculate_conversion_rate(10000, 220)}%")
    print(f"Z-score: {z}")
    
    if significant:
        print("Status: ✅ STATISTICALLY SIGNIFICANT")
        print("Action: Roll out the 'Reasoning Block' to 100% of users. Target CR 2.2% achieved!")
    else:
        print("Status: ❌ NOT SIGNIFICANT")
        print("Action: Keep testing or refine AI prompts. Difference might be due to chance.")
