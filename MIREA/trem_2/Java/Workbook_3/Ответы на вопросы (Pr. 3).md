# Ответы на вопросы (часть 2, bikeproject)

- **Примитивный тип в полях класса:** `int NumGears` (`Bike`), `int tyreWidth`, `postHeight` (`RoadBike`), `int frameSize` (`MountainBike`).
- **Конкатенация строк:** в `Bike.printDescription()` (`"This bike has " + this.handleBars + ...`), а также в `printDescription()` у `RoadBike` и `MountainBike`.
- **Имена объектов:** `bike1`, `bike2` (`RoadBike`), `bike3` (`MountainBike`), `bike4` (`Bike`).
- **Число конструкторов:** `Bike` — 2, `RoadBike` — 3, `MountainBike` — 2, `BikeDriver` — 0 явных (есть только конструктор по умолчанию).
- **Суперкласс и подклассы:** суперкласс `Bike`, подклассы `RoadBike` и `MountainBike`.
- **Значения стандартного велосипеда (конструктор по умолчанию):**
  - `RoadBike`: drop, racing, tread less, razor, 19 передач, 20 мм, штырь 22.
  - `MountainBike`: Bull Horn, Hardtail, Maxxis, dropper, 27 передач, RockShox XC32, Pro, рама 19.

# Модернизация
Добавлены `BikeParts` (константа `MAKE = "Oracle Cycles"` вместо `final make`, метод `printDescription()`), `MountainParts` (`TERRAIN = "off_road"`), `RoadParts` (`terrain = "track_racing"`). `Bike`, `MountainBike`, `RoadBike` их реализуют. В `BikeDriver` `bike1.postHeight` меняется с 22 на 20 и выводится.
