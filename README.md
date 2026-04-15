# styleai-pm
Product specification, ethical governance framework, and bias monitoring logic for StyleGenie AI (Fashion Tech).
# StyleGenie AI: Product Management Specification

![Industry: Fashion Tech](https://img.shields.io/badge/Industry-Fashion_Tech-pink)
![Role: Product Manager](https://img.shields.io/badge/Role-Product_Manager-blue)
![Focus: AI Ethics & Governance](https://img.shields.io/badge/Focus-AI_Ethics-green)

### 🌟 Обзор проекта
**StyleGenie AI** — это инновационный AI-ассистент, объединяющий Vision AI и RAG-архитектуру для создания персональных гардеробных решений. Продукт трансформирует процесс онлайн-шопинга, обеспечивая экспертный уровень стайлинга на основе анализа визуальных данных пользователя и актуальных стоков ритейлеров.

**Ключевая цель:** Достижение целевой конверсии **CR 2.2%** и минимизация возвратов через гипер-персонализацию.

---

### 📂 Структура репозитория

* [**/docs**](./docs) — Стратегия запуска (Staged Rollout), Launch Checklist и Governance Framework.
* [**/prompts**](./prompts) — Системные инструкции (System Prompts) с встроенными этическими guardrails.
* [**/scripts**](./scripts) — Автоматизация мониторинга: Python-скрипт для аудита Fairness (порог 15%).
* [**/analytics**](./analytics) — Спецификация KPI, расчет ROI и план послезапускового мониторинга.

---

### 🛠 Технологический стек и Продукт
- **Core AI:** Интеграция мультимодальных моделей (Claude 3.5 Sonnet / GPT-4o).
- **Architecture:** RAG (Retrieval-Augmented Generation) с использованием векторных баз данных (Pinecone/Weaviate) для работы с каталогами.
- **Vision AI:** Анализ типа фигуры, цветотипа и стилистических предпочтений по фото.
- **Compliance:** Проектирование с учетом GDPR и EU AI Act.

---

### ⚖️ Этический аудит и Governance (Ключевая экспертиза)
Проект прошел комплексный этический аудит, что критично для работы с изображениями людей:
- **Fairness Threshold:** Контроль разброса качества рекомендаций между группами (Plus-size, Standard, Petite) с лимитом отклонения **< 15%**.
- **Data Privacy:** Внедрена система анонимизации лиц и протокол «Цифрового забвения».
- **Transparency:** Текстовое обоснование каждой рекомендации («Почему это вам подходит»).
- **Ethics Committee:** Сформированная структура принятия решений (PM, Data Scientist, Legal Advisor).

---

### 📈 Бизнес-эффект и Рынок
- **Целевой рынок:** Центральная Азия (Казахстан), женщины 25–40 лет.
- **Конверсия:** Ожидаемый рост CR на **15–35%** по сравнению с базовыми алгоритмами.
- **ROI:** Оценка возврата инвестиций через 6 месяцев эксплуатации (анализ снижения операционных затрат на возвраты).

---

### 📫 Контакты
**Gulnar Kaz** *AI Product Manager* [LinkedIn](https://www.linkedin.com/in/gulnara-bakirova-7a341918) | [GitHub](https://github.com/gulnarkaz)
