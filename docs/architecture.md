ML Architecture & Data Pipeline
StyleGenie AI использует гибридную архитектуру, сочетающую компьютерное зрение (Computer Vision) для анализа пользователя и RAG-подход для генерации стилистических рекомендаций.

1. High-Level Workflow (Схема процесса)
Input: Пользователь загружает фото и заполняет краткий анкетный профиль.

Vision Engine:

Body Analysis: Определение типа фигуры (Hourglass, Pear и др.).

Color Analysis: Определение цветотипа на основе оттенка кожи и волос.

Embedding Generation: Запрос преобразуется в вектор (математический код).

Vector Retrieval (RAG): Поиск по базе данных (Pinecone/Weaviate) наиболее подходящих товаров из инклюзивного каталога.

LLM Reasoning: Модель (на базе GPT-4 или Claude) сопоставляет найденные товары с типом фигуры и пишет обоснование.

Guardrails Audit: Финальная проверка ответа на соответствие этическим нормам перед показом пользователю.

Компонент	Технология	Зачем это нужно
Model Hosting	AWS Sagemaker / Google Vertex AI	Масштабируемость вычислений.
Vector DB	Pinecone	Мгновенный поиск товаров по вектору стиля.
Orchestration	LangChain	Управление цепочкой "Данные -> Промпт -> Ответ".
Monitoring	Weights & Biases	Отслеживание дрейфа модели и ошибок (галлюцинаций).

3. Data Governance в архитектуре
Мы встроили этические проверки на каждом этапе:

Pre-processing: Анонимизация лиц (Privacy by Design).

Inference: Приоритетная выдача товаров брендов, имеющих метку is_inclusive: true.

Post-processing: Скрипт bias_monitor.py проверяет отклонение рекомендаций в реальном времени.
