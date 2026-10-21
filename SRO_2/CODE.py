<!DOCTYPE html>
<html lang="ru" class="h-full">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>СРО №16 - Каталог мероприятий университета (АТУ)</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Google Fonts Inter -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                    },
                    colors: {
                        atu: {
                            blue: '#00529b',
                            gold: '#f39c12',
                            dark: '#0f172a',
                            card: 'rgba(15, 23, 42, 0.75)'
                        }
                    },
                    animation: {
                        'ken-burns': 'kenburns 35s ease-in-out infinite alternate',
                        'pulse-glow': 'pulseGlow 3s infinite',
                    },
                    keyframes: {
                        kenburns: {
                            '0%': { transform: 'scale(1) translate(0, 0)' },
                            '50%': { transform: 'scale(1.12) translate(-1%, -1%)' },
                            '100%': { transform: 'scale(1) translate(0, 0)' },
                        },
                        pulseGlow: {
                            '0%, 100%': { opacity: '0.6' },
                            '50%': { opacity: '0.9' }
                        }
                    }
                }
            }
        }
    </script>

    <style>
        /* Glassmorphism Styles */
        .glass-panel {
            background: rgba(15, 23, 42, 0.78);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.12);
        }
        .glass-card {
            background: rgba(30, 41, 59, 0.7);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.08);
        }
        .glass-input {
            background: rgba(15, 23, 42, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: #ffffff;
        }
        .glass-input:focus {
            border-color: #3b82f6;
            outline: none;
            box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.3);
        }

        /* Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        ::-webkit-scrollbar-track {
            background: rgba(15, 23, 42, 0.5);
        }
        ::-webkit-scrollbar-thumb {
            background: rgba(100, 116, 139, 0.5);
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: rgba(148, 163, 184, 0.8);
        }
    </style>
</head>
<body class="bg-slate-950 text-slate-100 font-sans min-h-screen flex flex-col relative overflow-x-hidden">

    <!-- Background Image with Ken Burns Zoom & Overlay -->
    <div class="fixed inset-0 z-0 overflow-hidden pointer-events-none">
        <div class="absolute inset-0 bg-cover bg-center animate-ken-burns filter brightness-90 scale-105" 
             style="background-image: url('https://images.unsplash.com/photo-1541829070764-84a7d30dd3f3?auto=format&fit=crop&w=1920&q=80');">
             <!-- Note: Real ATU image source fallback / ambient style -->
        </div>
        <!-- Dark Gradient Overlays for Readability -->
        <div class="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/80 to-slate-900/60"></div>
        <div class="absolute inset-0 bg-blue-950/30 mix-blend-multiply"></div>
    </div>

    <!-- MAIN HEADER / NAVIGATION -->
    <header class="sticky top-0 z-40 glass-panel border-b border-slate-800/80 px-4 lg:px-8 py-3 transition-all duration-300">
        <div class="max-w-7xl mx-mx-auto flex flex-col md:flex-row items-center justify-between gap-4">
            
            <!-- Logo & Title -->
            <div class="flex items-center space-x-3 cursor-pointer" onclick="switchTab('app')">
                <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-blue-600 to-cyan-400 flex items-center justify-center shadow-lg shadow-blue-500/30">
                    <i class="fa-solid me-0 fa-graduation-cap text-white text-xl"></i>
                </div>
                <div>
                    <h1 class="font-bold text-lg leading-tight tracking-wide text-white">АТУ Events <span class="text-xs px-2 py-0.5 rounded bg-blue-500/20 text-blue-300 border border-blue-500/30">СРО №16</span></h1>
                    <p class="text-xs text-slate-400">Языки и технология программирования (Лекции 1-8)</p>
                </div>
            </div>

            <!-- Navigation Tabs -->
            <nav class="flex items-center space-x-1 md:space-x-2 bg-slate-900/60 p-1.5 rounded-xl border border-slate-800 text-xs md:text-sm overflow-x-auto max-w-full">
                <button id="nav-app" onclick="switchTab('app')" class="px-3 py-1.5 rounded-lg font-medium transition-all duration-200 flex items-center gap-2 bg-blue-600 text-white shadow-md">
                    <i class="fa-solid fa-calendar-days"></i> <span>Каталог (Приложение)</span>
                </button>
                <button id="nav-report" onclick="switchTab('report')" class="px-3 py-1.5 rounded-lg font-medium transition-all duration-200 flex items-center gap-2 text-slate-300 hover:text-white hover:bg-slate-800">
                    <i class="fa-solid fa-file-lines"></i> <span>Отчёт и ЖЦ ПО</span>
                </button>
                <button id="nav-tests" onclick="switchTab('tests')" class="px-3 py-1.5 rounded-lg font-medium transition-all duration-200 flex items-center gap-2 text-slate-300 hover:text-white hover:bg-slate-800">
                    <i class="fa-solid fa-vial-circle-check"></i> <span>Тестирование</span>
                </button>
                <button id="nav-readme" onclick="switchTab('readme')" class="px-3 py-1.5 rounded-lg font-medium transition-all duration-200 flex items-center gap-2 text-slate-300 hover:text-white hover:bg-slate-800">
                    <i class="fa-brands fa-github"></i> <span>GitHub & README</span>
                </button>
                <button id="nav-slides" onclick="switchTab('slides')" class="px-3 py-1.5 rounded-lg font-medium transition-all duration-200 flex items-center gap-2 text-slate-300 hover:text-white hover:bg-slate-800">
                    <i class="fa-solid fa-file-powerpoint"></i> <span>Презентация</span>
                </button>
            </nav>
            
            <!-- Student / Author Info -->
            <div class="hidden xl:flex items-center gap-3 text-right text-xs">
                <div>
                    <div class="font-semibold text-slate-200">Студент СРО</div>
                    <div class="text-slate-400">Тема №16 (Лекции 1-8)</div>
                </div>
            </div>

        </div>
    </header>

    <!-- CONTENT WRAPPER -->
    <main class="relative z-10 flex-1 max-w-7xl w-full mx-auto p-4 md:p-6 lg:p-8">

        <!-- Notification Toast Container -->
        <div id="toast-container" class="fixed bottom-5 right-5 z-50 flex flex-col gap-2 pointer-events-none"></div>

        <!-- ========================================== -->
        <!-- TAB 1: INTERACTIVE APP (КАТАЛОГ МЕРОПРИЯТИЙ) -->
        <!-- ========================================== -->
        <section id="tab-app" class="space-y-6">
            
            <!-- Banner / Hero Section -->
            <div class="glass-panel rounded-2xl p-6 md:p-8 border border-slate-700/50 relative overflow-hidden">
                <div class="absolute -right-10 -bottom-10 w-64 h-64 bg-blue-600/20 rounded-full blur-3xl pointer-events-none"></div>
                <div class="relative z-10 flex flex-col md:flex-row justify-between items-start md:items-center gap-6">
                    <div class="space-y-2">
                        <span class="inline-block px-3 py-1 text-xs font-semibold uppercase tracking-wider bg-blue-500/10 text-blue-400 rounded-full border border-blue-500/20">
                            Алматинский Технологический Университет
                        </span>
                        <h2 class="text-2xl md:text-3xl font-extrabold text-white">Каталог мероприятий и событий АТУ</h2>
                        <p class="text-slate-300 text-sm max-w-2xl leading-relaxed">
                            Интерактивная система регистраций на университетские хакатоны, мастер-классы, спортивные турниры и научные конференции.
                        </p>
                    </div>
                    <button onclick="openModal('add-event-modal')" class="px-5 py-3 rounded-xl bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 text-white font-semibold shadow-lg shadow-blue-600/30 transition-all flex items-center gap-2 text-sm whitespace-nowrap">
                        <i class="fa-solid fa-plus"></i> Создать мероприятие
                    </button>
                </div>

                <!-- Statistics Widgets (Переменные и Массивы) -->
                <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 mt-6 pt-6 border-t border-slate-800">
                    <div class="glass-card p-4 rounded-xl">
                        <div class="text-xs text-slate-400 font-medium">Всего событий</div>
                        <div id="stat-total-events" class="text-2xl font-bold text-blue-400 mt-1">0</div>
                    </div>
                    <div class="glass-card p-4 rounded-xl">
                        <div class="text-xs text-slate-400 font-medium">Свободных мест</div>
                        <div id="stat-total-seats" class="text-2xl font-bold text-emerald-400 mt-1">0</div>
                    </div>
                    <div class="glass-card p-4 rounded-xl">
                        <div class="text-xs text-slate-400 font-medium">Всего регистраций</div>
                        <div id="stat-total-regs" class="text-2xl font-bold text-purple-400 mt-1">0</div>
                    </div>
                    <div class="glass-card p-4 rounded-xl">
                        <div class="text-xs text-slate-400 font-medium">Категорий</div>
                        <div id="stat-categories" class="text-2xl font-bold text-amber-400 mt-1">0</div>
                    </div>
                </div>
            </div>

            <!-- Controls & Filters (Строки, Функции) -->
            <div class="glass-panel p-4 rounded-2xl flex flex-col md:flex-row gap-4 items-center justify-between">
                <!-- Search Input -->
                <div class="relative w-full md:w-80">
                    <i class="fa-solid fa-magnifying-glass absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400 text-sm"></i>
                    <input type="text" id="search-input" oninput="renderEvents()" placeholder="Поиск по названию или локации..." class="w-full glass-input rounded-xl pl-10 pr-4 py-2 text-sm">
                </div>

                <!-- Category Filter Pills -->
                <div id="category-filters" class="flex flex-wrap gap-2 w-full md:w-auto">
                    <!-- Dynamic categories injected by JS -->
                </div>

                <!-- Sort Control -->
                <div class="flex items-center gap-2 w-full md:w-auto justify-end">
                    <span class="text-xs text-slate-400 whitespace-nowrap">Сортировка:</span>
                    <select id="sort-select" onchange="renderEvents()" class="glass-input rounded-xl px-3 py-2 text-xs">
                        <option value="date-asc">По дате (сначала ближайшие)</option>
                        <option value="date-desc">По дате (сначала дальние)</option>
                        <option value="seats-desc">По наличию мест</option>
                        <option value="title-asc">По алфавиту (А-Я)</option>
                    </select>
                </div>
            </div>

            <!-- Events Grid -->
            <div id="events-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <!-- Dynamic cards populated by JavaScript -->
            </div>

            <!-- Empty State -->
            <div id="empty-state" class="hidden glass-panel p-12 text-center rounded-2xl space-y-3">
                <i class="fa-solid fa-folder-open text-4xl text-slate-500"></i>
                <h3 class="text-lg font-semibold text-slate-300">Мероприятия не найдены</h3>
                <p class="text-xs text-slate-400">Попробуйте изменить параметры поиска или фильтрации.</p>
                <button onclick="resetFilters()" class="px-4 py-2 bg-slate-800 text-xs font-medium rounded-lg text-blue-400 hover:bg-slate-700">Сбросить фильтры</button>
            </div>

        </section>

        <!-- ========================================== -->
        <!-- TAB 2: АНАЛИЗ И ТРЕБОВАНИЯ (ПОЛНЫЙ ОТЧЕТ СРО) -->
        <!-- ========================================== -->
        <section id="tab-report" class="hidden space-y-6">
            
            <div class="glass-panel p-6 md:p-8 rounded-2xl space-y-8">
                
                <div>
                    <span class="text-xs uppercase tracking-widest text-blue-400 font-bold">Раздел 1: Введение и Исследования</span>
                    <h2 class="text-2xl font-bold text-white mt-1">Анализ предметной области и обоснование актуальности</h2>
                    <p class="text-slate-300 text-sm mt-3 leading-relaxed">
                        В современных вузах, таких как Алматинский Технологический Университет (АТУ), проходит большое количество внеучебных, академических и научных мероприятий. Отсутствие единого централизованного цифрового узла приводит к низкой информированности студентов, накладкам во времени и проблемам при подсчёте участников.
                    </p>
                </div>

                <!-- Comparison Table of 3 Systems -->
                <div class="space-y-3">
                    <h3 class="text-lg font-semibold text-blue-300"><i class="fa-solid fa-code-compare mr-2"></i> Обзор и сравнение аналогов (не менее 3 источников)</h3>
                    <div class="overflow-x-auto">
                        <table class="w-full text-left text-xs border-collapse">
                            <thead>
                                <tr class="bg-slate-800/80 text-slate-200">
                                    <th class="p-3 rounded-tl-lg">Критерий сравнения</th>
                                    <th class="p-3">Timepad.ru</th>
                                    <th class="p-3">Leader-ID</th>
                                    <th class="p-3">Университетский портал (Аналог)</th>
                                    <th class="p-3 rounded-tr-lg text-blue-400">Разрабатываемая система (Тема 16)</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-slate-800 text-slate-300">
                                <tr>
                                    <td class="p-3 font-medium text-slate-100">Целевая аудитория</td>
                                    <td class="p-3">Коммерческие события</td>
                                    <td class="p-3">Стартапы и точки кипения</td>
                                    <td class="p-3">Общие новости вуза</td>
                                    <td class="p-3 text-emerald-400 font-semibold">Студенты и ППС АТУ</td>
                                </tr>
                                <tr>
                                    <td class="p-3 font-medium text-slate-100">Интеграция с академическими группами</td>
                                    <td class="p-3">Отсутствует</td>
                                    <td class="p-3">Частично</td>
                                    <td class="p-3">Отсутствует</td>
                                    <td class="p-3 text-emerald-400 font-semibold">Полная (Валидация факультета/группы)</td>
                                </tr>
                                <tr>
                                    <td class="p-3 font-medium text-slate-100">Контроль лимита мест</td>
                                    <td class="p-3">Платный функционал</td>
                                    <td class="p-3">Да</td>
                                    <td class="p-3">Нет (только анонсы)</td>
                                    <td class="p-3 text-emerald-400 font-semibold">Да (Автоматический пересчёт)</td>
                                </tr>
                                <tr>
                                    <td class="p-3 font-medium text-slate-100">Простота интерфейса</td>
                                    <td class="p-3">Перегружен рекламой</td>
                                    <td class="p-3">Сложная регистрация</td>
                                    <td class="p-3">Устаревший веб-дизайн</td>
                                    <td class="p-3 text-emerald-400 font-semibold">Легковесный Glassmorphic SPA</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Requirements Section -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6 pt-4 border-t border-slate-800">
                    <div class="space-y-3">
                        <h3 class="text-base font-bold text-emerald-400 flex items-center gap-2">
                            <i class="fa-solid fa-list-check"></i> 5+ Функциональных требований (FR)
                        </h3>
                        <ul class="space-y-2 text-xs text-slate-300 list-disc list-inside leading-relaxed">
                            <li><strong class="text-slate-100">FR-01:</strong> Отображение актуального каталога мероприятий с лимитами мест.</li>
                            <li><strong class="text-slate-100">FR-02:</strong> Регистрация студента на событие с проверкой валидности Email и Группы.</li>
                            <li><strong class="text-slate-100">FR-03:</strong> Динамическая фильтрация по категориям и текстовый поиск.</li>
                            <li><strong class="text-slate-100">FR-04:</strong> Создание новых мероприятий организаторами с защитой от пустых полей.</li>
                            <li><strong class="text-slate-100">FR-05:</strong> Просмотр списка участников выбранного мероприятия в реальном времени.</li>
                            <li><strong class="text-slate-100">FR-06:</strong> Расчёт статистики доступных мест и суммарного количества регистраций.</li>
                        </ul>
                    </div>
                    <div class="space-y-3">
                        <h3 class="text-base font-bold text-amber-400 flex items-center gap-2">
                            <i class="fa-solid fa-shield-halved"></i> 3+ Нефункциональных требования (NFR)
                        </h3>
                        <ul class="space-y-2 text-xs text-slate-300 list-disc list-inside leading-relaxed">
                            <li><strong class="text-slate-100">NFR-01 (Производительность):</strong> Время отклика поиска и сортировки &lt; 50 мс.</li>
                            <li><strong class="text-slate-100">NFR-02 (Адаптивность):</strong> Поддержка мобильных устройств, планшетов и ПК.</li>
                            <li><strong class="text-slate-100">NFR-03 (Надёжность):</strong> Обработка исключительных ситуаций и дубликатов без сбоя JS.</li>
                            <li><strong class="text-slate-100">NFR-04 (Usability):</strong> Соответствие стилю Glassmorphism с понятными ошибками ввода.</li>
                        </ul>
                    </div>
                </div>

                <!-- Life Cycle Model (ЖЦ ПО) -->
                <div class="pt-6 border-t border-slate-800 space-y-4">
                    <span class="text-xs uppercase tracking-widest text-purple-400 font-bold">Раздел 2: Проектирование и ЖЦ ПО</span>
                    <h3 class="text-lg font-bold text-white">Выбор модели жизненного цикла разработки</h3>
                    
                    <div class="glass-card p-4 rounded-xl border-l-4 border-purple-500 space-y-2">
                        <h4 class="font-semibold text-purple-300 text-sm">Инкрементная модель (Agile / Iterative approach)</h4>
                        <p class="text-xs text-slate-300 leading-relaxed">
                            Для данного проекта выбрана **Инкрементная модель ЖЦ ПО**. Разработка разбита на 3 спринта:
                            <br>1. <em>Базовый каркас:</em> Модель данных (структуры) и интерфейс каталога.
                            <br>2. <em>Логика взаимодействия:</em> Валидатор форм, поиск, алгоритмы фильтрации и подсчёта мест.
                            <br>3. <em>Аналитика и Тестирование:</em> Модуль статистики, формирование отчёта и прохождение 8 тест-кейсов.
                        </p>
                    </div>

                    <!-- Curriculum Alignment Table (Лекции 1-8) -->
                    <h4 class="text-sm font-semibold text-slate-200 mt-4">Применение концепций программирования (Лекции №1-8)</h4>
                    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-3 text-xs">
                        <div class="glass-card p-3 rounded-lg border border-slate-700">
                            <div class="font-bold text-blue-400">Лекция 1-3: Введение & Парадигмы</div>
                            <div class="text-slate-400 mt-1">Модульная архитектура, события DOM, работа с жизненным циклом ПО.</div>
                        </div>
                        <div class="glass-card p-3 rounded-lg border border-slate-700">
                            <div class="font-bold text-emerald-400">Лекция 4: Циклы</div>
                            <div class="text-slate-400 mt-1">Использование `for`, `forEach`, `filter` для перебора и рендера массива событий.</div>
                        </div>
                        <div class="glass-card p-3 rounded-lg border border-slate-700">
                            <div class="font-bold text-amber-400">Лекция 5-6: Функции & Массивы</div>
                            <div class="text-slate-400 mt-1">Декомпозиция на функции (`renderEvents`, `registerUser`), динамические коллекции.</div>
                        </div>
                        <div class="glass-card p-3 rounded-lg border border-slate-700">
                            <div class="font-bold text-purple-400">Лекция 7-8: Строки & Структуры</div>
                            <div class="text-slate-400 mt-1">Регулярные выражения (RegEx), методы строк `toLowerCase()`, JSON структуры (Event, Participant).</div>
                        </div>
                    </div>
                </div>

            </div>

        </section>

        <!-- ========================================== -->
        <!-- TAB 3: ПРОТОКОЛ ТЕСТИРОВАНИЯ (8+ ТЕСТ-КЕЙСОВ) -->
        <!-- ========================================== -->
        <section id="tab-tests" class="hidden space-y-6">
            
            <div class="glass-panel p-6 md:p-8 rounded-2xl space-y-6">
                <div>
                    <span class="text-xs uppercase tracking-widest text-emerald-400 font-bold">Раздел 5: Проверка и Верификация</span>
                    <h2 class="text-2xl font-bold text-white mt-1">Протокол тестирования программного обеспечения</h2>
                    <p class="text-slate-300 text-sm mt-2 leading-relaxed">
                        В соответствии с методическими требованиями СРО проведено не менее 8 тест-кейсов (4 основных сценария, 2 случая ошибочного ввода и 2 граничных случая).
                    </p>
                </div>

                <div class="overflow-x-auto">
                    <table class="w-full text-left text-xs border-collapse">
                        <thead>
                            <tr class="bg-slate-800/90 text-slate-200">
                                <th class="p-3 border-b border-slate-700">ID</th>
                                <th class="p-3 border-b border-slate-700">Тип</th>
                                <th class="p-3 border-b border-slate-700">Сценарий / Описание</th>
                                <th class="p-3 border-b border-slate-700">Входные данные</th>
                                <th class="p-3 border-b border-slate-700">Ожидаемый результат</th>
                                <th class="p-3 border-b border-slate-700">Фактический результат</th>
                                <th class="p-3 border-b border-slate-700">Статус</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-800/60 text-slate-300">
                            <!-- T-01 -->
                            <tr class="hover:bg-slate-800/30">
                                <td class="p-3 font-bold text-blue-400">T-01</td>
                                <td class="p-3"><span class="px-2 py-0.5 rounded bg-blue-500/20 text-blue-300">Основной</span></td>
                                <td class="p-3 font-medium text-slate-100">Успешная регистрация на мероприятие</td>
                                <td class="p-3">ФИО: "Аскаров Аманат", Email: "a.askarov@atu.kz", Группа: "ИС-21-2"</td>
                                <td class="p-3">Количество мест уменьшается на 1, участник добавлен в список.</td>
                                <td class="p-3">Места пересчитаны, выведено уведомление об успехе.</td>
                                <td class="p-3"><span class="px-2 py-1 bg-emerald-500/20 text-emerald-400 font-bold rounded">PASS</span></td>
                            </tr>
                            <!-- T-02 -->
                            <tr class="hover:bg-slate-800/30">
                                <td class="p-3 font-bold text-blue-400">T-02</td>
                                <td class="p-3"><span class="px-2 py-0.5 rounded bg-blue-500/20 text-blue-300">Основной</span></td>
                                <td class="p-3 font-medium text-slate-100">Поиск мероприятия по ключевому слову</td>
                                <td class="p-3">Поисковый запрос: "Хакатон"</td>
                                <td class="p-3">Фильтрация карточек, вывод только событий со словом "Хакатон".</td>
                                <td class="p-3">Карточки отфильтрованы корректно.</td>
                                <td class="p-3"><span class="px-2 py-1 bg-emerald-500/20 text-emerald-400 font-bold rounded">PASS</span></td>
                            </tr>
                            <!-- T-03 -->
                            <tr class="hover:bg-slate-800/30">
                                <td class="p-3 font-bold text-blue-400">T-03</td>
                                <td class="p-3"><span class="px-2 py-0.5 rounded bg-blue-500/20 text-blue-300">Основной</span></td>
                                <td class="p-3 font-medium text-slate-100">Фильтрация по категории</td>
                                <td class="p-3">Клик на категорию "IT & Наука"</td>
                                <td class="p-3">Отображаются события категории "IT & Наука".</td>
                                <td class="p-3">Список перестроен без перезагрузки.</td>
                                <td class="p-3"><span class="px-2 py-1 bg-emerald-500/20 text-emerald-400 font-bold rounded">PASS</span></td>
                            </tr>
                            <!-- T-04 -->
                            <tr class="hover:bg-slate-800/30">
                                <td class="p-3 font-bold text-blue-400">T-04</td>
                                <td class="p-3"><span class="px-2 py-0.5 rounded bg-blue-500/20 text-blue-300">Основной</span></td>
                                <td class="p-3 font-medium text-slate-100">Добавление нового мероприятия</td>
                                <td class="p-3">Заполнена форма нового события с лимитом 25 мест</td>
                                <td class="p-3">Новое событие появляется в сетке, счетчик категорий обновлен.</td>
                                <td class="p-3">Событие успешно добавлено в массив.</td>
                                <td class="p-3"><span class="px-2 py-1 bg-emerald-500/20 text-emerald-400 font-bold rounded">PASS</span></td>
                            </tr>
                            <!-- T-05 -->
                            <tr class="hover:bg-slate-800/30">
                                <td class="p-3 font-bold text-amber-400">T-05</td>
                                <td class="p-3"><span class="px-2 py-0.5 rounded bg-amber-500/20 text-amber-300">Ошибка ввода</span></td>
                                <td class="p-3 font-medium text-slate-100">Некорректный формат Email</td>
                                <td class="p-3">Email: "amanat_atu.kz" (без @)</td>
                                <td class="p-3">Блокировка отправки, подсвечивание ошибки валидации.</td>
                                <td class="p-3">Сообщение «Некорректный формат Email» показано.</td>
                                <td class="p-3"><span class="px-2 py-1 bg-emerald-500/20 text-emerald-400 font-bold rounded">PASS</span></td>
                            </tr>
                            <!-- T-06 -->
                            <tr class="hover:bg-slate-800/30">
                                <td class="p-3 font-bold text-amber-400">T-06</td>
                                <td class="p-3"><span class="px-2 py-0.5 rounded bg-amber-500/20 text-amber-300">Ошибка ввода</span></td>
                                <td class="p-3 font-medium text-slate-100">Отправка формы с пустыми полями</td>
                                <td class="p-3">ФИО: "", Email: "", Группа: ""</td>
                                <td class="p-3">Форма не отправляется, индикация обязательных полей.</td>
                                <td class="p-3">Запрос отклонен функцией валидации.</td>
                                <td class="p-3"><span class="px-2 py-1 bg-emerald-500/20 text-emerald-400 font-bold rounded">PASS</span></td>
                            </tr>
                            <!-- T-07 -->
                            <tr class="hover:bg-slate-800/30">
                                <td class="p-3 font-bold text-purple-400">T-07</td>
                                <td class="p-3"><span class="px-2 py-0.5 rounded bg-purple-500/20 text-purple-300">Граничный</span></td>
                                <td class="p-3 font-medium text-slate-100">Попытка записи при 0 свободных мест</td>
                                <td class="p-3">Событие с `availableSeats = 0`</td>
                                <td class="p-3">Кнопка записи заблокирована (Disabled), статус "Завершено".</td>
                                <td class="p-3">Запись невозможна, кнопка неактивна.</td>
                                <td class="p-3"><span class="px-2 py-1 bg-emerald-500/20 text-emerald-400 font-bold rounded">PASS</span></td>
                            </tr>
                            <!-- T-08 -->
                            <tr class="hover:bg-slate-800/30">
                                <td class="p-3 font-bold text-purple-400">T-08</td>
                                <td class="p-3"><span class="px-2 py-0.5 rounded bg-purple-500/20 text-purple-300">Граничный</span></td>
                                <td class="p-3 font-medium text-slate-100">Повторная регистрация того же Email</td>
                                <td class="p-3">Дублирующийся Email "a.askarov@atu.kz" на одно событие</td>
                                <td class="p-3">Система выдает предупреждение о дубликате.</td>
                                <td class="p-3">Зафиксировано предупреждение, запись отклонена.</td>
                                <td class="p-3"><span class="px-2 py-1 bg-emerald-500/20 text-emerald-400 font-bold rounded">PASS</span></td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <!-- Test Summary Widget -->
                <div class="glass-card p-4 rounded-xl flex items-center justify-between border border-slate-700">
                    <div class="flex items-center gap-3">
                        <div class="w-10 h-10 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold text-lg">
                            <i class="fa-solid fa-check"></i>
                        </div>
                        <div>
                            <div class="font-bold text-sm text-slate-100">Итоговый результат верификации: 100% PASS</div>
                            <div class="text-xs text-slate-400">Все 8 тест-кейсов успешно пройдены без сбоев интерфейса.</div>
                        </div>
                    </div>
                    <span class="text-xs text-slate-400">Окружение: Chrome / HTML5 / JS ES6</span>
                </div>

            </div>

        </section>

        <!-- ========================================== -->
        <!-- TAB 4: GITHUB & README.MD DOCUMENTATION -->
        <!-- ========================================== -->
        <section id="tab-readme" class="hidden space-y-6">
            
            <div class="glass-panel p-6 md:p-8 rounded-2xl space-y-6">
                <div>
                    <span class="text-xs uppercase tracking-widest text-slate-400 font-bold">Раздел 6: Документация Проекта</span>
                    <h2 class="text-2xl font-bold text-white mt-1">Репозиторий GitHub и README.md</h2>
                    <p class="text-slate-300 text-sm mt-2">
                        Структура файлов согласно разделу 4 и 5 методических указаний СРО.
                    </p>
                </div>

                <!-- Recommended Repository Tree -->
                <div class="space-y-2">
                    <h3 class="text-sm font-semibold text-blue-300"><i class="fa-solid fa-sitemap mr-2"></i> Структура репозитория (Recommended Tree)</h3>
                    <pre class="bg-slate-900/90 p-4 rounded-xl text-xs font-mono text-emerald-400 border border-slate-800 overflow-x-auto">
atu-events-catalog/
├── README.md               # Главное описание, инструкции, таблица тестов
├── index.html              # Единственный веб-клиент (HTML/CSS/JS Glassmorphic SPA)
├── src/
│   ├── app.js              # Модульная логика, обработка массивов и функций
│   └── styles.css          # Дополнительные стили и переменные
├── docs/
│   ├── analysis.md         # Обзор 3-х аналогов и обоснование актуальности
│   └── requirements.md     # SRS, функциональные и нефункциональные требования
├── tests/
│   └── test-protocol.pdf   # Протокол 8 тест-кейсов с подтверждениями
└── presentation/
    └── slides.pdf          # Презентация на 10 слайдов для защиты
</pre>
                </div>

                <!-- Markdown Formatted README View -->
                <div class="space-y-3 pt-4 border-t border-slate-800">
                    <h3 class="text-sm font-semibold text-blue-300"><i class="fa-brands fa-markdown mr-2"></i> Содержание README.md</h3>
                    <div class="glass-card p-5 rounded-xl text-xs text-slate-300 space-y-4 font-mono leading-relaxed border border-slate-800">
                        <div>
                            <h1 class="text-lg font-bold text-slate-100"># Каталог мероприятий АТУ (СРО №16)</h1>
                            <p class="text-slate-400">Дисциплина: Языки и технология программирования (Лекции 1-8)</p>
                        </div>
                        <div>
                            <h2 class="text-sm font-bold text-blue-400">## Цель проекта</h2>
                            <p>Создание веб-ориентированной системы учета и регистрации студентов АТУ на академические и внеучебные события с фильтрацией, проверкой ввода и статистикой.</p>
                        </div>
                        <div>
                            <h2 class="text-sm font-bold text-blue-400">## Инструкция по запуску</h2>
                            <p>1. Клонировать репозиторий: <code class="bg-slate-800 px-1 py-0.5 rounded text-amber-300">git clone https://github.com/student/atu-events.git</code></p>
                            <p>2. Открыть файл <code class="bg-slate-800 px-1 py-0.5 rounded text-amber-300">index.html</code> в любом современном браузере (Chrome, Firefox, Edge).</p>
                            <p>3. Серверные зависимости не требуются (Single File Executable / JS Native).</p>
                        </div>
                        <div>
                            <h2 class="text-sm font-bold text-blue-400">## Стек технологий</h2>
                            <p>- HTML5 / CSS3 (Tailwind CSS Framework)</p>
                            <p>- JavaScript ES6+ (Array methods, Regex, Structural objects)</p>
                            <p>- FontAwesome Icons</p>
                        </div>
                    </div>
                </div>

            </div>

        </section>

        <!-- ========================================== -->
        <!-- TAB 5: ПРЕЗЕНТАЦИЯ ДЛЯ ЗАЩИТЫ (10 СЛАЙДОВ) -->
        <!-- ========================================== -->
        <section id="tab-slides" class="hidden space-y-6">
            
            <div class="glass-panel p-6 md:p-8 rounded-2xl space-y-6">
                
                <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
                    <div>
                        <span class="text-xs uppercase tracking-widest text-amber-400 font-bold">Раздел 7: Защита Проекта</span>
                        <h2 class="text-2xl font-bold text-white mt-1">Интерактивная презентация (10 слайдов)</h2>
                    </div>
                    <!-- Slide Navigation Controls -->
                    <div class="flex items-center gap-3 bg-slate-900/80 px-4 py-2 rounded-xl border border-slate-800">
                        <button onclick="prevSlide()" class="p-2 text-slate-300 hover:text-white rounded hover:bg-slate-800"><i class="fa-solid fa-chevron-left"></i></button>
                        <span id="slide-indicator" class="text-xs font-bold text-blue-400">Слайд 1 из 10</span>
                        <button onclick="nextSlide()" class="p-2 text-slate-300 hover:text-white rounded hover:bg-slate-800"><i class="fa-solid fa-chevron-right"></i></button>
                    </div>
                </div>

                <!-- SLIDE CANVAS CONTAINER -->
                <div id="slide-container" class="glass-card p-8 rounded-2xl min-h-[380px] flex flex-col justify-between border border-slate-700/80 relative overflow-hidden transition-all duration-300">
                    <!-- Slide content injected by JS -->
                </div>

                <!-- Thumbnails indicator -->
                <div id="slide-dots" class="flex justify-center items-center gap-2 pt-2">
                    <!-- Dots injected by JS -->
                </div>

            </div>

        </section>

    </main>

    <!-- FOOTER -->
    <footer class="relative z-10 glass-panel border-t border-slate-800 py-4 px-6 text-center text-xs text-slate-400 mt-auto">
        <div class="max-w-7xl mx-auto flex flex-col sm:flex-row justify-between items-center gap-2">
            <div>Алматинский Технологический Университет &copy; 2026. Дисциплина «Языки и технология программирования».</div>
            <div class="flex items-center gap-4">
                <span>СРО Мини-проект Тема №16</span>
                <span class="text-emerald-400 font-medium"><i class="fa-solid fa-circle-check"></i> Готово к сдаче</span>
            </div>
        </div>
    </footer>


    <!-- ========================================== -->
    <!-- MODAL 1: REGISTRATION ON EVENT -->
    <!-- ========================================== -->
    <div id="reg-modal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-md hidden">
        <div class="glass-panel w-full max-w-md rounded-2xl p-6 border border-slate-700 space-y-5 shadow-2xl relative">
            <button onclick="closeModal('reg-modal')" class="absolute top-4 right-4 text-slate-400 hover:text-white"><i class="fa-solid fa-xmark text-lg"></i></button>
            
            <div class="space-y-1">
                <span class="text-xs font-bold text-blue-400 uppercase tracking-wider">Форма записи</span>
                <h3 id="reg-modal-title" class="text-lg font-bold text-white">Регистрация на событие</h3>
                <p id="reg-modal-subtitle" class="text-xs text-slate-400"></p>
            </div>

            <form id="reg-form" onsubmit="handleRegistration(event)" class="space-y-4">
                <input type="hidden" id="reg-event-id">
                
                <div>
                    <label class="block text-xs font-medium text-slate-300 mb-1">ФИО Студента *</label>
                    <input type="text" id="reg-name" placeholder="Например: Ибраев Данияр Нурланулы" class="w-full glass-input rounded-xl px-3 py-2 text-xs" required>
                </div>

                <div>
                    <label class="block text-xs font-medium text-slate-300 mb-1">Корпоративный Email *</label>
                    <input type="email" id="reg-email" placeholder="student@atu.kz" class="w-full glass-input rounded-xl px-3 py-2 text-xs" required>
                </div>

                <div>
                    <label class="block text-xs font-medium text-slate-300 mb-1">Факультет и Группа *</label>
                    <input type="text" id="reg-group" placeholder="Например: ФИТ / ИС-21-2" class="w-full glass-input rounded-xl px-3 py-2 text-xs" required>
                </div>

                <div class="pt-2 flex justify-end gap-3">
                    <button type="button" onclick="closeModal('reg-modal')" class="px-4 py-2 rounded-xl text-xs font-medium text-slate-300 hover:bg-slate-800">Отмена</button>
                    <button type="submit" class="px-5 py-2 rounded-xl text-xs font-bold bg-blue-600 hover:bg-blue-500 text-white shadow-lg shadow-blue-600/30">Записаться</button>
                </div>
            </form>
        </div>
    </div>


    <!-- ========================================== -->
    <!-- MODAL 2: ADD NEW EVENT (ADMIN / ORGANIZER) -->
    <!-- ========================================== -->
    <div id="add-event-modal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-md hidden">
        <div class="glass-panel w-full max-w-lg rounded-2xl p-6 border border-slate-700 space-y-5 shadow-2xl relative max-h-[90vh] overflow-y-auto">
            <button onclick="closeModal('add-event-modal')" class="absolute top-4 right-4 text-slate-400 hover:text-white"><i class="fa-solid fa-xmark text-lg"></i></button>
            
            <div class="space-y-1">
                <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider">Панель организатора</span>
                <h3 class="text-lg font-bold text-white">Создание нового мероприятия АТУ</h3>
            </div>

            <form id="add-event-form" onsubmit="handleAddEvent(event)" class="space-y-4">
                <div>
                    <label class="block text-xs font-medium text-slate-300 mb-1">Название мероприятия *</label>
                    <input type="text" id="add-title" placeholder="Например: Хакатон 'Smart ATU 2026'" class="w-full glass-input rounded-xl px-3 py-2 text-xs" required>
                </div>

                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <label class="block text-xs font-medium text-slate-300 mb-1">Категория *</label>
                        <select id="add-category" class="w-full glass-input rounded-xl px-3 py-2 text-xs" required>
                            <option value="IT & Наука">IT & Наука</option>
                            <option value="Спорт">Спорт</option>
                            <option value="Культура">Культура</option>
                            <option value="Карьера">Карьера</option>
                            <option value="Семинар">Семинар</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-xs font-medium text-slate-300 mb-1">Дата проведения *</label>
                        <input type="date" id="add-date" class="w-full glass-input rounded-xl px-3 py-2 text-xs" required>
                    </div>
                </div>

                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <label class="block text-xs font-medium text-slate-300 mb-1">Локация / Корпус *</label>
                        <input type="text" id="add-location" placeholder="Главный корпус, Актовый зал" class="w-full glass-input rounded-xl px-3 py-2 text-xs" required>
                    </div>
                    <div>
                        <label class="block text-xs font-medium text-slate-300 mb-1">Лимит мест *</label>
                        <input type="number" id="add-seats" min="1" max="500" value="30" class="w-full glass-input rounded-xl px-3 py-2 text-xs" required>
                    </div>
                </div>

                <div>
                    <label class="block text-xs font-medium text-slate-300 mb-1">Описание мероприятия *</label>
                    <textarea id="add-desc" rows="3" placeholder="Подробная информация о спикерах, правилах и регламенте..." class="w-full glass-input rounded-xl px-3 py-2 text-xs" required></textarea>
                </div>

                <div class="pt-2 flex justify-end gap-3">
                    <button type="button" onclick="closeModal('add-event-modal')" class="px-4 py-2 rounded-xl text-xs font-medium text-slate-300 hover:bg-slate-800">Отмена</button>
                    <button type="submit" class="px-5 py-2 rounded-xl text-xs font-bold bg-emerald-600 hover:bg-emerald-500 text-white shadow-lg shadow-emerald-600/30">Опубликовать</button>
                </div>
            </form>
        </div>
    </div>


    <!-- ========================================== -->
    <!-- MODAL 3: VIEW EVENT DETAILS & PARTICIPANTS -->
    <!-- ========================================== -->
    <div id="details-modal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-md hidden">
        <div class="glass-panel w-full max-w-lg rounded-2xl p-6 border border-slate-700 space-y-5 shadow-2xl relative max-h-[90vh] overflow-y-auto">
            <button onclick="closeModal('details-modal')" class="absolute top-4 right-4 text-slate-400 hover:text-white"><i class="fa-solid fa-xmark text-lg"></i></button>
            
            <div class="space-y-2">
                <span id="detail-category" class="px-2.5 py-1 text-[10px] font-bold uppercase tracking-wider rounded-full bg-blue-500/20 text-blue-300 border border-blue-500/30"></span>
                <h3 id="detail-title" class="text-xl font-bold text-white"></h3>
                <p id="detail-desc" class="text-xs text-slate-300 leading-relaxed"></p>
            </div>

            <div class="grid grid-cols-2 gap-3 text-xs bg-slate-900/60 p-3 rounded-xl border border-slate-800">
                <div><span class="text-slate-400">Дата:</span> <strong id="detail-date" class="text-slate-200"></strong></div>
                <div><span class="text-slate-400">Локация:</span> <strong id="detail-location" class="text-slate-200"></strong></div>
                <div><span class="text-slate-400">Всего мест:</span> <strong id="detail-total-seats" class="text-slate-200"></strong></div>
                <div><span class="text-slate-400">Осталось мест:</span> <strong id="detail-avail-seats" class="text-emerald-400"></strong></div>
            </div>

            <div class="space-y-3">
                <h4 class="text-xs font-bold uppercase tracking-wider text-slate-300 flex items-center justify-between">
                    <span>Зарегистрированные участники</span>
                    <span id="detail-count" class="text-blue-400">0</span>
                </h4>
                
                <div id="participants-list" class="space-y-2 max-h-48 overflow-y-auto pr-1">
                    <!-- Dynamic participants injected by JS -->
                </div>
            </div>

            <div class="pt-2 flex justify-end">
                <button onclick="closeModal('details-modal')" class="px-5 py-2 rounded-xl text-xs font-medium bg-slate-800 text-slate-200 hover:bg-slate-700">Закрыть</button>
            </div>
        </div>
    </div>


    <!-- ========================================== -->
    <!-- JAVASCRIPT APP LOGIC (LECTURES 1-8 COVERAGE) -->
    <!-- ========================================== -->
    <script>
        /* ====================================================
           1. DATA STRUCTURES & INITIAL STATE (Лекции 6, 8)
           ==================================================== */
        
        // Initial Mock Events Array
        let events = [
            {
                id: "evt-001",
                title: "Студенческий Хакатон 'ATU Tech Cup 2026'",
                category: "IT & Наука",
                date: "2026-11-15",
                location: "Главный корпус, IT-Лаборатория 304",
                description: "48-часовой соревновательный хакатон по разработке мобильных и веб-сервисов для университета. Призовой фонд и гранты от IT-компаний.",
                totalSeats: 40,
                availableSeats: 3,
                participants: [
                    { name: "Аскаров Аманат", email: "a.askarov@atu.kz", group: "ФИТ / ИС-21-2" },
                    { name: "Серикова Аружан", email: "a.serikova@atu.kz", group: "ФИТ / ВТиПО-22-1" }
                ]
            },
            {
                id: "evt-002",
                title: "Турнир по Настольному Теннису АТУ",
                category: "Спорт",
                date: "2026-10-28",
                location: "Спортивный комплекс АТУ",
                description: "Первенство университета среди студентов всех факультетов. Одиночные и парные разряды. Награждение кубками и медалями.",
                totalSeats: 24,
                availableSeats: 0, // Bordercase: 0 seats available
                participants: [
                    { name: "Бексултанов Арман", email: "a.beksultan@atu.kz", group: "ФТБ / ТПП-20-1" }
                ]
            },
            {
                id: "evt-003",
                title: "Ярмарка Вакансий и Карьеры АТУ 2026",
                category: "Карьера",
                date: "2026-11-05",
                location: "Дворец студентов АТУ, Холл 1-го этажа",
                description: "Встреча с ведущими работодателями пищевой, легкой и IT-промышленности Казахстана. Стажировки и трудоустройство для выпускников.",
                totalSeats: 150,
                availableSeats: 98,
                participants: []
            },
            {
                id: "evt-004",
                title: "Фестиваль Искусств 'ATU Talent Star'",
                category: "Культура",
                date: "2026-12-01",
                location: "Актовый зал Главного корпуса",
                description: "Ежегодный конкурс талантов: вокал, хореография, инструментальная музыка и театральное искусство.",
                totalSeats: 80,
                availableSeats: 45,
                participants: []
            }
        ];

        let selectedCategory = "Все";

        /* ====================================================
           2. PRESENTATION SLIDES DATA (Лекции 1-8)
           ==================================================== */
        const slidesData = [
            {
                number: 1,
                title: "Тема №16: Каталог мероприятий университета",
                subtitle: "Дисциплина: Языки и технология программирования (Лекции №1-8)",
                content: `
                    <div class="space-y-4">
                        <div class="p-4 bg-blue-500/10 rounded-xl border border-blue-500/20 text-slate-200">
                            <h4 class="font-bold text-blue-400">Алматинский Технологический Университет (АТУ)</h4>
                            <p class="text-xs mt-1">Автор: Студент факультета IT | Преподаватель: Кафедра ИТ</p>
                        </div>
                        <p class="text-xs text-slate-300 leading-relaxed">
                            Данный проект представляет собой полнофункциональный интерактивный одностраничный сервис для публикации, поиска и записи на события университета, разработанный в соответствии со строгими методическими требованиями СРО.
                        </p>
                    </div>
                `
            },
            {
                number: 2,
                title: "Проблема и Актуальность Проекта",
                subtitle: "Зачем университету единый каталог мероприятий?",
                content: `
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs">
                        <div class="glass-card p-4 rounded-xl border-l-4 border-red-500">
                            <h5 class="font-bold text-red-400 mb-1">Существующая проблема</h5>
                            <p class="text-slate-300">Разрозненность анонсов по социальным сетям, отсутствие лимита регистраций и потеря заявок студентов.</p>
                        </div>
                        <div class="glass-card p-4 rounded-xl border-l-4 border-emerald-500">
                            <h5 class="font-bold text-emerald-400 mb-1">Решение</h5>
                            <p class="text-slate-300">Единый веб-каталог с мгновенным поиском, фильтрацией по категориям и автоматическим подсчетом мест.</p>
                        </div>
                    </div>
                `
            },
            {
                number: 3,
                title: "Анализ 3-х Аналогов",
                subtitle: "Сравнительный анализ существующего ПО",
                content: `
                    <div class="text-xs space-y-2">
                        <p class="text-slate-300">Были проанализированы сервисы: <strong>Timepad</strong>, <strong>Leader-ID</strong> и <strong>Университетский новостной портал</strong>.</p>
                        <div class="p-3 bg-slate-900/80 rounded-xl border border-slate-800 text-slate-300">
                            <strong class="text-blue-400">Преимущество нашего решения:</strong> Полная узкоспециализированная адаптация под академические группы АТУ, нулевая стоимость инфраструктуры и мгновенная работа без перезагрузки страниц.
                        </div>
                    </div>
                `
            },
            {
                number: 4,
                title: "Формализация Требований (SRS)",
                subtitle: "Функциональные и Нефункциональные требования",
                content: `
                    <div class="grid grid-cols-2 gap-3 text-xs">
                        <div class="p-3 glass-card rounded-xl">
                            <strong class="text-emerald-400">6 Функциональных requirements:</strong>
                            <ul class="list-disc list-inside mt-1 space-y-1 text-slate-300">
                                <li>Просмотр списка событий</li>
                                <li>Запись участников</li>
                                <li>Фильтрация и поиск</li>
                                <li>Создание новых мероприятий</li>
                            </ul>
                        </div>
                        <div class="p-3 glass-card rounded-xl">
                            <strong class="text-amber-400">4 Нефункциональных requirements:</strong>
                            <ul class="list-disc list-inside mt-1 space-y-1 text-slate-300">
                                <li>Отклики UI < 50мс</li>
                                <li>Адаптивность (Mobile/Desktop)</li>
                                <li>Валидация полей Regex</li>
                            </ul>
                        </div>
                    </div>
                `
            },
            {
                number: 5,
                title: "Модель Жизненного Цикла ПО",
                subtitle: "Инкрементная разработка (Agile Iterations)",
                content: `
                    <div class="p-4 glass-card rounded-xl text-xs space-y-2 border-l-4 border-purple-500">
                        <h5 class="font-bold text-purple-300">Почему выбрана Инкрементная модель?</h5>
                        <p class="text-slate-300">Модель позволила поэтапно наращивать функционал: от базовых структур данных (Итерация 1) к алгоритмам поиска/валидации (Итерация 2) и окончательному модулю верификации/тестирования (Итерация 3).</p>
                    </div>
                `
            },
            {
                number: 6,
                title: "Архитектура & Связь с Лекциями №1-8",
                subtitle: "Практическое применение концепций программирования",
                content: `
                    <div class="grid grid-cols-3 gap-2 text-[11px] text-center">
                        <div class="p-2 bg-slate-900 rounded-lg border border-slate-800">
                            <strong class="text-blue-400">Лекция 4: Циклы</strong>
                            <p class="text-slate-400 mt-1">Рендеринг массивов через forEach</p>
                        </div>
                        <div class="p-2 bg-slate-900 rounded-lg border border-slate-800">
                            <strong class="text-emerald-400">Лекция 5-6: Массивы</strong>
                            <p class="text-slate-400 mt-1">Методы filter, push, sort</p>
                        </div>
                        <div class="p-2 bg-slate-900 rounded-lg border border-slate-800">
                            <strong class="text-amber-400">Лекция 7-8: Строки & Данные</strong>
                            <p class="text-slate-400 mt-1">Регулярные выражения и Объекты</p>
                        </div>
                    </div>
                `
            },
            {
                number: 7,
                title: "Демонстрация Интерфейса",
                subtitle: "Стиль Glassmorphism с Ken Burns эффектом",
                content: `
                    <div class="p-4 bg-slate-900/90 rounded-xl border border-slate-800 text-xs space-y-2">
                        <p class="text-slate-300">Интерфейс оформлен в академическом стиле с адаптивным полупрозрачным блюр-оверлеем на фоне корпуса **Алматинского Технологического Университета**.</p>
                        <p class="text-blue-400 font-semibold">Все элементы управления привязаны к стандартным событиям DOM (onClick, onInput, onSubmit).</p>
                    </div>
                `
            },
            {
                number: 8,
                title: "Результаты Тестирования ПО",
                subtitle: "Протокол верификации из 8 тест-кейсов",
                content: `
                    <div class="p-4 bg-emerald-500/10 rounded-xl border border-emerald-500/20 text-xs space-y-2">
                        <div class="flex items-center justify-between font-bold text-emerald-400">
                            <span>Успешность тестов: 100% PASS</span>
                            <span>8 / 8 Тестов пройдено</span>
                        </div>
                        <p class="text-slate-300">Проверены основные сценарии записи, обработка пустых полей, некорректный Email и граничные условия (0 свободных мест).</p>
                    </div>
                `
            },
            {
                number: 9,
                title: "Структура GitHub & Документация",
                subtitle: "Соответствие требованиям раздела 4-5",
                content: `
                    <div class="p-3 bg-slate-900/90 rounded-xl border border-slate-800 text-xs font-mono text-slate-300">
                        <p class="text-amber-400 font-bold">Репозиторий содержит:</p>
                        <p>• README.md с полной инструкцией</p>
                        <p>• Файл исходного кода index.html</p>
                        <p>• Каталог docs/ с SRS и Анализом</p>
                    </div>
                `
            },
            {
                number: 10,
                title: "Заключение и Перспективы",
                subtitle: "Итоги работы над СРО Тема №16",
                content: `
                    <div class="space-y-3 text-xs text-slate-300">
                        <p>В ходе выполнения СРО были успешно продемонстрированы навыки применения фундаментальных концепций программирования (циклы, массивы, функции, объекты, валидация).</p>
                        <div class="p-3 bg-blue-600/20 rounded-xl border border-blue-500/30 text-blue-300 font-semibold text-center">
                            Проект полностью готов к демонстрации и защите перед преподавателем!
                        </div>
                    </div>
                `
            }
        ];

        let currentSlideIndex = 0;

        /* ====================================================
           3. APPLICATION RENDER FUNCTIONS (Лекция 4, 5, 6)
           ==================================================== */
        
        // Initial setup on load
        window.addEventListener('DOMContentLoaded', () => {
            renderCategoryFilters();
            renderEvents();
            renderSlide(currentSlideIndex);
        });

        // Tab Switching Logic
        function switchTab(tabId) {
            const tabs = ['app', 'report', 'tests', 'readme', 'slides'];
            tabs.forEach(t => {
                const el = document.getElementById(`tab-${t}`);
                const nav = document.getElementById(`nav-${t}`);
                if (t === tabId) {
                    el.classList.remove('hidden');
                    nav.className = 'px-3 py-1.5 rounded-lg font-medium transition-all duration-200 flex items-center gap-2 bg-blue-600 text-white shadow-md';
                } else {
                    el.classList.add('hidden');
                    nav.className = 'px-3 py-1.5 rounded-lg font-medium transition-all duration-200 flex items-center gap-2 text-slate-300 hover:text-white hover:bg-slate-800';
                }
            });
        }

        // Render Category Filter Buttons (Лекция 6: Массивы)
        function renderCategoryFilters() {
            const categories = ["Все", ...new Set(events.map(e => e.category))];
            const container = document.getElementById('category-filters');
            
            container.innerHTML = categories.map(cat => `
                <button onclick="setCategory('${cat}')" class="px-3 py-1.5 rounded-xl text-xs font-medium transition-all ${selectedCategory === cat ? 'bg-blue-600 text-white shadow-md' : 'glass-card text-slate-300 hover:text-white hover:bg-slate-800'}">
                    ${cat}
                </button>
            `).join('');

            document.getElementById('stat-categories').innerText = categories.length - 1;
        }

        function setCategory(cat) {
            selectedCategory = cat;
            renderCategoryFilters();
            renderEvents();
        }

        function resetFilters() {
            document.getElementById('search-input').value = '';
            selectedCategory = "Все";
            renderCategoryFilters();
            renderEvents();
        }

        // Render Events Grid (Лекции 4, 5, 6, 7: Циклы, Функции, Строки)
        function renderEvents() {
            const grid = document.getElementById('events-grid');
            const emptyState = document.getElementById('empty-state');
            const searchVal = document.getElementById('search-input').value.toLowerCase().trim();
            const sortVal = document.getElementById('sort-select').value;

            // 1. Filter logic (Лекция 6: Array Filter)
            let filtered = events.filter(e => {
                const matchesCat = selectedCategory === "Все" || e.category === selectedCategory;
                const matchesSearch = e.title.toLowerCase().includes(searchVal) || 
                                      e.location.toLowerCase().includes(searchVal) ||
                                      e.description.toLowerCase().includes(searchVal);
                return matchesCat && matchesSearch;
            });

            // 2. Sort logic (Лекция 6: Array Sort)
            filtered.sort((a, b) => {
                if (sortVal === 'date-asc') return new Date(a.date) - new Date(b.date);
                if (sortVal === 'date-desc') return new Date(b.date) - new Date(a.date);
                if (sortVal === 'seats-desc') return b.availableSeats - a.availableSeats;
                if (sortVal === 'title-asc') return a.title.localeCompare(b.title);
                return 0;
            });

            // 3. Update Statistics Widget (Лекция 5)
            updateStats();

            // 4. Render DOM
            if (filtered.length === 0) {
                grid.innerHTML = '';
                emptyState.classList.remove('hidden');
                return;
            }

            emptyState.classList.add('hidden');
            grid.innerHTML = filtered.map(e => {
                const isFull = e.availableSeats <= 0;
                return `
                    <div class="glass-card rounded-2xl p-5 border border-slate-700/80 hover:border-blue-500/50 transition-all duration-300 flex flex-col justify-between space-y-4 group">
                        <div class="space-y-2">
                            <div class="flex items-center justify-between">
                                <span class="px-2.5 py-0.5 text-[10px] font-bold uppercase tracking-wider rounded-full bg-blue-500/10 text-blue-300 border border-blue-500/20">
                                    ${e.category}
                                </span>
                                <span class="text-xs ${isFull ? 'text-red-400 font-bold' : 'text-emerald-400 font-medium'} flex items-center gap-1">
                                    <i class="fa-solid ${isFull ? 'fa-circle-xmark' : 'fa-user-check'}"></i>
                                    ${isFull ? 'Мест нет' : `Свободно: ${e.availableSeats}`}
                                </span>
                            </div>

                            <h3 class="font-bold text-base text-white group-hover:text-blue-400 transition-colors line-clamp-2">
                                ${e.title}
                            </h3>

                            <p class="text-xs text-slate-300 line-clamp-2 leading-relaxed">
                                ${e.description}
                            </p>
                        </div>

                        <div class="space-y-3 pt-3 border-t border-slate-800 text-xs">
                            <div class="flex items-center gap-2 text-slate-400">
                                <i class="fa-regular fa-calendar text-blue-400"></i>
                                <span>${formatDate(e.date)}</span>
                            </div>
                            <div class="flex items-center gap-2 text-slate-400">
                                <i class="fa-solid fa-location-dot font-size text-rose-400"></i>
                                <span class="truncate">${e.location}</span>
                            </div>

                            <div class="flex items-center gap-2 pt-2">
                                <button onclick="openRegModal('${e.id}')" ${isFull ? 'disabled' : ''} 
                                        class="flex-1 py-2 rounded-xl text-xs font-bold transition-all ${isFull ? 'bg-slate-800 text-slate-500 cursor-not-allowed' : 'bg-blue-600 hover:bg-blue-500 text-white shadow-lg shadow-blue-600/20'}">
                                    ${isFull ? 'Запись закрыта' : 'Записаться'}
                                </button>
                                <button onclick="openDetailsModal('${e.id}')" class="px-3 py-2 rounded-xl glass-panel text-slate-300 hover:text-white hover:bg-slate-800 text-xs">
                                    <i class="fa-solid fa-info-circle"></i>
                                </button>
                            </div>
                        </div>
                    </div>
                `;
            }).join('');
        }

        // Helper: Format Date String
        function formatDate(dateStr) {
            const options = { year: 'numeric', month: 'long', day: 'numeric' };
            return new Date(dateStr).toLocaleDateString('ru-RU', options);
        }

        // Calculate and Update Top Widget Stats
        function updateStats() {
            const totalEvents = events.length;
            const totalSeats = events.reduce((acc, curr) => acc + curr.availableSeats, 0);
            const totalRegs = events.reduce((acc, curr) => acc + curr.participants.length, 0);

            document.getElementById('stat-total-events').innerText = totalEvents;
            document.getElementById('stat-total-seats').innerText = totalSeats;
            document.getElementById('stat-total-regs').innerText = totalRegs;
        }

        /* ====================================================
           4. MODALS & REGISTRATION LOGIC (Лекция 5, 7)
           ==================================================== */
        
        function openModal(modalId) {
            document.getElementById(modalId).classList.remove('hidden');
        }

        function closeModal(modalId) {
            document.getElementById(modalId).classList.add('hidden');
        }

        // Open Modal for User Registration
        function openRegModal(eventId) {
            const evt = events.find(e => e.id === eventId);
            if (!evt) return;

            document.getElementById('reg-event-id').value = evt.id;
            document.getElementById('reg-modal-title').innerText = `Запись: ${evt.title}`;
            document.getElementById('reg-modal-subtitle').innerText = `Осталось мест: ${evt.availableSeats} из ${evt.totalSeats}`;
            
            // Reset fields
            document.getElementById('reg-name').value = '';
            document.getElementById('reg-email').value = '';
            document.getElementById('reg-group').value = '';

            openModal('reg-modal');
        }

        // Handle Registration Form Submission (Regex & Validations - Лекция 7)
        function handleRegistration(event) {
            event.preventDefault();

            const eventId = document.getElementById('reg-event-id').value;
            const name = document.getElementById('reg-name').value.trim();
            const email = document.getElementById('reg-email').value.trim();
            const group = document.getElementById('reg-group').value.trim();

            const evt = events.find(e => e.id === eventId);
            if (!evt) return;

            // 1. Validation: Email Regex (Лекция 7)
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(email)) {
                showToast('Ошибка: Введите корректный Email адрес!', 'error');
                return;
            }

            // 2. Validation: Empty fields
            if (!name || !group) {
                showToast('Ошибка: Все поля обязательны к заполнению!', 'error');
                return;
            }

            // 3. Validation: Duplicate Email Check
            const isAlreadyReg = evt.participants.some(p => p.email.toLowerCase() === email.toLowerCase());
            if (isAlreadyReg) {
                showToast('Предупреждение: Студент с таким Email уже зарегистрирован!', 'error');
                return;
            }

            // 4. Validation: Seats available boundary check
            if (evt.availableSeats <= 0) {
                showToast('Ошибка: Свободные места закончились!', 'error');
                closeModal('reg-modal');
                return;
            }

            // Add Participant & Decrement Seats
            evt.participants.push({ name, email, group });
            evt.availableSeats -= 1;

            closeModal('reg-modal');
            renderEvents();
            showToast(`Успешно! ${name} зарегистрирован(а) на мероприятие.`, 'success');
        }

        // Handle Adding New Event (Admin Form)
        function handleAddEvent(event) {
            event.preventDefault();

            const title = document.getElementById('add-title').value.trim();
            const category = document.getElementById('add-category').value;
            const date = document.getElementById('add-date').value;
            const location = document.getElementById('add-location').value.trim();
            const seats = parseInt(document.getElementById('add-seats').value);
            const description = document.getElementById('add-desc').value.trim();

            if (!title || !date || !location || !seats || !description) {
                showToast('Заполните все обязательные поля!', 'error');
                return;
            }

            const newEvent = {
                id: `evt-${Date.now()}`,
                title,
                category,
                date,
                location,
                description,
                totalSeats: seats,
                availableSeats: seats,
                participants: []
            };

            events.unshift(newEvent);
            renderCategoryFilters();
            renderEvents();
            closeModal('add-event-modal');
            showToast('Новое мероприятие успешно добавлено в каталог!', 'success');
            
            // Reset form
            document.getElementById('add-event-form').reset();
        }

        // View Event Details & Registered Participants
        function openDetailsModal(eventId) {
            const evt = events.find(e => e.id === eventId);
            if (!evt) return;

            document.getElementById('detail-category').innerText = evt.category;
            document.getElementById('detail-title').innerText = evt.title;
            document.getElementById('detail-desc').innerText = evt.description;
            document.getElementById('detail-date').innerText = formatDate(evt.date);
            document.getElementById('detail-location').innerText = evt.location;
            document.getElementById('detail-total-seats').innerText = evt.totalSeats;
            document.getElementById('detail-avail-seats').innerText = evt.availableSeats;
            document.getElementById('detail-count').innerText = `${evt.participants.length} чел.`;

            const list = document.getElementById('participants-list');
            if (evt.participants.length === 0) {
                list.innerHTML = `<p class="text-xs text-slate-500 italic">На данный момент участников нет.</p>`;
            } else {
                list.innerHTML = evt.participants.map((p, idx) => `
                    <div class="glass-card p-2.5 rounded-lg flex items-center justify-between text-xs border border-slate-800">
                        <div class="flex items-center gap-2">
                            <span class="w-5 h-5 rounded-full bg-blue-500/20 text-blue-400 flex items-center justify-center font-bold text-[10px]">${idx + 1}</span>
                            <div>
                                <div class="font-semibold text-slate-200">${p.name}</div>
                                <div class="text-[10px] text-slate-400">${p.group}</div>
                            </div>
                        </div>
                        <span class="text-[10px] text-slate-400">${p.email}</span>
                    </div>
                `).join('');
            }

            openModal('details-modal');
        }

        /* ====================================================
           5. PRESENTATION SLIDER CONTROLLER (Лекция 4, 5)
           ==================================================== */
        
        function renderSlide(index) {
            if (index < 0) index = 0;
            if (index >= slidesData.length) index = slidesData.length - 1;
            currentSlideIndex = index;

            const slide = slidesData[currentSlideIndex];
            const container = document.getElementById('slide-container');

            container.innerHTML = `
                <div class="space-y-4">
                    <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                        <div>
                            <span class="text-[10px] uppercase font-bold tracking-widest text-blue-400">Слайд №${slide.number}</span>
                            <h3 class="text-xl font-bold text-white mt-0.5">${slide.title}</h3>
                        </div>
                        <span class="px-3 py-1 rounded-full bg-slate-800 text-xs text-slate-300 border border-slate-700">${slide.subtitle}</span>
                    </div>
                    <div class="pt-2">
                        ${slide.content}
                    </div>
                </div>
                <div class="flex justify-between items-center text-xs text-slate-500 border-t border-slate-800/60 pt-3 mt-4">
                    <span>Защита СРО Тема №16 | АТУ 2026</span>
                    <span>Используйте стрелки для навигации</span>
                </div>
            `;

            document.getElementById('slide-indicator').innerText = `Слайд ${slide.number} из ${slidesData.length}`;

            // Render Dots
            const dotsContainer = document.getElementById('slide-dots');
            dotsContainer.innerHTML = slidesData.map((s, idx) => `
                <button onclick="renderSlide(${idx})" class="w-2.5 h-2.5 rounded-full transition-all ${idx === currentSlideIndex ? 'bg-blue-500 w-6' : 'bg-slate-700 hover:bg-slate-500'}"></button>
            `).join('');
        }

        function nextSlide() {
            if (currentSlideIndex < slidesData.length - 1) {
                renderSlide(currentSlideIndex + 1);
            }
        }

        function prevSlide() {
            if (currentSlideIndex > 0) {
                renderSlide(currentSlideIndex - 1);
            }
        }

        // Keyboard listener for slider
        document.addEventListener('keydown', (e) => {
            const slidesTab = document.getElementById('tab-slides');
            if (!slidesTab.classList.contains('hidden')) {
                if (e.key === 'ArrowRight') nextSlide();
                if (e.key === 'ArrowLeft') prevSlide();
            }
        });

        /* ====================================================
           6. TOAST NOTIFICATION UTILITY
           ==================================================== */
        function showToast(message, type = 'info') {
            const container = document.getElementById('toast-container');
            const toast = document.createElement('div');
            
            const bgColor = type === 'success' ? 'bg-emerald-600' : type === 'error' ? 'bg-rose-600' : 'bg-blue-600';
            const icon = type === 'success' ? 'fa-circle-check' : type === 'error' ? 'fa-triangle-exclamation' : 'fa-circle-info';

            toast.className = `${bgColor} text-white px-4 py-3 rounded-xl shadow-2xl flex items-center gap-3 text-xs pointer-events-auto transition-all duration-300 transform translate-y-2 opacity-0`;
            toast.innerHTML = `<i class="fa-solid ${icon} text-base"></i><span>${message}</span>`;

            container.appendChild(toast);

            // Animate in
            setTimeout(() => {
                toast.classList.remove('translate-y-2', 'opacity-0');
            }, 10);

            // Remove
            setTimeout(() => {
                toast.classList.add('opacity-0', 'translate-y-2');
                setTimeout(() => toast.remove(), 300);
            }, 3500);
        }
    </script>
</body>
</html>
