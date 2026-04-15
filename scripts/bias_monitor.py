import json

def calculate_fairness_gap(performance_data):
    """
    Функция для расчета разрыва в качестве рекомендаций (Fairness Gap) 
    между различными сегментами фигур (Plus-size, Petite, Standard).
    
    Целевой порог PM: < 15%
    """
    
    # Извлекаем CSAT (Customer Satisfaction Score) по категориям
    scores = [data['csat'] for data in performance_data.values()]
    
    if not scores:
        return 0
        
    # Рассчитываем разрыв между лучшим и худшим сегментом
    fairness_gap = max(scores) - min(scores)
    
    return round(fairness_gap, 2)

def audit_report(gap):
    threshold = 15.0  # Установленный PM лимит в процентах
    
    print(f"--- StyleGenie AI Ethics Audit ---")
    print(f"Current Fairness Gap: {gap}%")
    
    if gap <= threshold:
        print("Status: ✅ PASS")
        print("Action: System is balanced. Proceed with standard monitoring.")
    else:
        print("Status: ❌ FAIL")
        print(f"Action: Alerting Ethics Committee! Release blocked. Initiate RLHF.")

# Пример данных для аудита (CSAT по сегментам)
mock_data = {
    "Standard": {"csat": 92.5},
    "Petite":   {"csat": 88.0},
    "Plus-size": {"csat": 79.0}  # Здесь разрыв > 10%, модель требует внимания
}

if __name__ == "__main__":
    gap = calculate_fairness_gap(mock_data)
    audit_report(gap)
