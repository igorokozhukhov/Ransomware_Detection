# Обнаружение ВПО с использованием машинного обучения

С развитием Интернета вредоносные программы стали одной из основных киберугроз. При увеличении разнообразия вредоносных программ антивирусные сканеры не могут удовлетворить потребности в защите, что приводит к миллионам атакуемых узлов.

Кроме того, наблюдается снижение уровня навыков, необходимых для разработки вредоносного программного обеспечения, из-за высокой доступности атакующих инструментов в Интернете. Высокая доступность методов обхода обнаружения, а также возможность приобретения вредоносного программного обеспечения на черном рынке, позволяют любому стать атакующим, независимо от уровня навыков. Текущие исследования показывают, что все больше и больше атак осуществляется неопытными злоумышленниками или автоматизированно.

Обнаружение вредоносного программного обеспечения с помощью стандартных методов на основе сигнатур становится все сложнее, поскольку все текущие вредоносные приложения обычно имеют несколько полиморфных слоев, чтобы избежать обнаружения или использовать побочные механизмы для автоматического обновления себя до новой версии в короткие сроки, чтобы избежать обнаружения любым антивирусным программным обеспечением.

Машинное обучение помогает антивирусному программному обеспечению обнаруживать новые угрозы, не полагаясь на сигнатуры. Ранее антивирусное программное обеспечение в основном полагалось на метод фингерпринтинга, который работает путем сопоставления файлов с огромной базой известного вредоносного программного обеспечения.

Основной недостаток здесь заключается в том, что проверка сигнатур может обнаружить только вредоносное программное обеспечение, которое уже было известно ранее. Это довольно большая слепая зона, учитывая, что каждый день создается сотни тысяч новых вариантов вредоносного программного обеспечения. Машинное обучение, с другой стороны, может быть обучено распознавать признаки хороших и плохих файлов, что позволяет выявлять вредоносные шаблоны и обнаруживать вредоносное программное обеспечение - независимо от того, было оно известно ранее или нет.

## Цель
Как уже упоминалось ранее, антивирусные программы, основанные на сигнатурах, хорошо справляются с обнаружением известных вредоносных программ, которые уже были обнаружены некоторыми антивирусными компаниями. Однако они не способны обнаруживать полиморфные вредоносные программы, которые могут изменять свои сигнатуры, а также новые вредоносные программы, для которых сигнатуры еще не созданы. В свою очередь, точность эвристических детекторов не всегда достаточна для надежного обнаружения, что приводит к большому количеству ложных срабатываний и пропусков. Необходимость в новых методах обнаружения обусловлена высокой скоростью распространения полиморфных вирусов.

## Схема
![image](https://github.com/igorokozhukhov/Ransomware-Detection/assets/41119305/228eee12-99ba-481f-9324-6b8d6f6cb742)

## Специфические требования проекта

###	Требования к данным
Два набора данных, которые мы использовали в этом проекте, можно найти на Kaggle.com.  

При установке/запуске этого проекта пользователю не нужно устанавливать модуль с Kaggle, он уже предоставлен в файле проекта.  

###	Функциональные требования
Используемые модули:
- joblib==1.2.0
- numpy==1.24.3
- pandas==2.0.1
- pyfiglet==0.8.post1
- python-dateutil==2.8.2
- pytz==2023.3
- scikit-learn==1.2.2
- scipy==1.10.1
- six==1.16.0
- threadpoolctl==3.1.0
- tzdata==2023.3
- pefile==2023.2.7

## Архитектурный дизайн
![image](https://github.com/igorokozhukhov/Ransomware-Detection/assets/41119305/2cb9fb6b-e6b9-46b6-8e97-b4c017848fe7)
## Дизайн пользовательского интерфейса
![image](https://github.com/igorokozhukhov/Ransomware-Detection/assets/41119305/9f8a1fa8-0afd-4260-b6b9-f384befce7f2)

![image](https://github.com/igorokozhukhov/Ransomware-Detection/assets/41119305/c8b11f5b-8b05-42e8-8ca0-0be093b3580b)

![image](https://github.com/igorokozhukhov/Ransomware-Detection/assets/41119305/8017b6e4-c72a-4dc3-b704-228a6230463a)

## Технические решения

###	Обнаружение вредоносных файлов формата PE

Основная часть этого проекта - модель машинного обучения, в которой используется классификатор случайного леса (Random Forest) и дерево решений (Decision Tree) для классификации вредоносных и легитимных файлов. Используемый набор данных, содержит 70% вредоносных файлов и 30% легитимных файлов.

Затем выбираются наиболее существенные признаки, необходимые для классификации, с помощью функции extratrees.feature_importances_. После сравнивается оценка классификатора дерева принятия решений (Decision Tree Classifier) и классификатора случайного леса (Random Forest Classifier) и сохраняется наилучшая из обученных моделей в файлы Classifier.pkl и features.pkl для отслеживания необходимых признаков при извлечении их из любого реального файла.

Основной проблемой при написании этого проекта, было извлечение признаков из PE файла и их сохранение для сохраненной модели машинного обучения. Для извлечения содержимого используется библиотека pefile (https://pypi.org/project/pefile/) в Python. Выбор этих признаков осуществляется с использованием модели features.pkl, которая содержит все важные признаки для классификатора. Извлечение файлов PE-заголовков выполняется с использованием библиотеки pefile в Python, а затем выбранные признаки передаются модели classifier.pkl, которая предсказывает результат.

## Тестирование и проверка

### Матрица ошибок для обнаружения вредоносных PE файлов
![image](https://github.com/igorokozhukhov/Ransomware-Detection/assets/41119305/5ae88fb3-bce2-4092-81a3-f316f2b8d894)

## Анализ производительности

- Точность (Accuracy - TP/ALL) Случайного Леса (Random Forest): 99.37% 
- Точность (Accuracy - TP/ALL) Дерева решений (Decision Tree): 98.46%

## Будущие улучшения
- Использование более широкого и хорошо размеченного набора данных.
- Возможность загружать файлы для проверки на сайте.
- Программа с графическим интерфейсом для Windows, поскольку в настоящее время она сделана только для терминала.
- Сканирование в реальном времени каждого файла при его загрузке/передаче для использования в повседневной жизни с целью обнаружения вредоносных файлов.
