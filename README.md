# StyleGenie AI: Inclusive Personal Stylist

**StyleGenie AI** — это интеллектуальная система персонального стайлинга на базе Vision AI и LLM, разработанная для рынка Fashion Tech. Продукт решает проблему высокого процента возвратов в eCommerce и отсутствия персонализации при подборе гардероба.

---

## Key Product Deliverables

Проект структурирован по ключевым областям ответственности Product Manager:

### 1. Product Discovery & Strategy
* [**/docs/strategy.md**](./docs/strategy.md) — Дорожная карта (Roadmap), фазы запуска и стратегия MVP.
* [**/docs/market_analysis.md**](./docs/market_analysis.md) — Анализ рынка Казахстана, сегментация аудитории и конкурентный ландшафт.
* [**/docs/experiments_log.md**](./docs/experiments_log.md) — Лог Lean-экспериментов: валидация гипотез через Wizard of Oz и Smoke-тесты.

### 2. AI Architecture & Technical Specs
* [**/docs/architecture.md**](./docs/architecture.md) — Схема ML-пайплайна: Vision AI + RAG (Retrieval-Augmented Generation).
* [**/data-schemas/product_metadata.json**](./data-schemas/product_metadata.json) — Техническая структура данных для интеграции с каталогом.
* [**/prompts/system_instructions.md**](./prompts/system_instructions.md) — Конфигурация системных инструкций для управления Persona и логикой ИИ.

### 3. Analytics & Business Performance
* [**/analytics/ab_test_design.md**](./analytics/ab_test_design.md) — Методология тестирования влияния ИИ-обоснований на конверсию (CR).
* [**/analytics/kpi_dashboard_spec.md**](./analytics/kpi_dashboard_spec.md) — Спецификация дашборда для мониторинга бизнес-метрик и здоровья ИИ.
* [**/docs/business_model.md**](./docs/business_model.md) — Юнит-экономика ($COGS_{AI}$), связь ML-метрик с прибылью и операционные плейбуки.

### 4. AI Governance & Ethics
* [**/docs/governance.md**](./docs/governance.md) — Фреймворк по управлению этическими рисками и Fairness Gap.
* [**/prompts/guardrails.md**](./prompts/guardrails.md) — Жесткие ограничения (Safety constraints) для предотвращения предвзятости.
* [**/scripts/bias_monitor.py**](./scripts/bias_monitor.py) — Прототип скрипта для автоматического контроля этических метрик.
* [**/scripts/ab_test_analyzer.py**](./scripts/ab_test_analyzer.py) — Скрипт для расчета статистической значимости экспериментов.

---

## Tech Stack & Tools
* **AI/ML:** Vision AI (silhouette analysis), LLM (reasoning), RAG (context retrieval).
* **Data:** Vector Databases (Pinecone/Weaviate), JSON Schemas.
* **Product:** Miro (Visual Roadmap), Python (Analytics), Google Analytics (KPI tracking).

---

## Core Performance Targets (KPIs)
* **Conversion Rate (CR):** 2.2% (+15-20% от базового уровня).
* **Return Rate Reduction:** -15% за счет точности подбора.
* **Fairness Gap:** < 15% (разрыв в качестве сервиса между разными типами фигур).
* **Average Order Value (AOV):** +10% через генерацию полных образов (Full Looks).

---

## Visual Concepts & Brainstorming
* [**Miro Board**](https://miro.com/app/board/uXjVGfSebtI=/) — Визуализация концепции, фундамента данных и циклов аудита.

---

## Contact
**Gulnar Kaz** — AI Product Manager www.linkedin.com/in/gulnara-bakirova-7a341918
