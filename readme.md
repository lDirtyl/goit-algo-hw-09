# Аналіз ефективності алгоритмів знаходження мінімальної кількості монет

## Вступ

Цей документ аналізує та порівнює ефективність двох підходів до розв'язання задачі знаходження мінімальної кількості монет: жадібного алгоритму та алгоритму динамічного програмування.

## Аналіз

### Складність виконання

- **Жадібний алгоритм (find_coins_greedy):** Складність залежить від кількості номіналів монет і не прямо пов'язана з сумою, яку потрібно розміняти. У найгіршому випадку складність становить O(n), де n - кількість номіналів монет.

- **Алгоритм динамічного програмування (find_min_coins):** Має складність O(m*n), де m - сума грошей, а n - кількість номіналів монет. Він забезпечує знаходження оптимального рішення, але вимагає більше часу та пам'яті при роботі з великими сумами.

### Час виконання при великих сумах

- При роботі з великими сумами алгоритм динамічного програмування стає значно повільнішим через вищу складність і необхідність обробки більшої кількості даних.
- Жадібний алгоритм продовжує швидко працювати з великими сумами, особливо при малому наборі номіналів монет.

### Ефективність у різних ситуаціях

- Жадібний алгоритм є ефективним, коли його стратегія гарантує оптимальне рішення, але може не завжди знаходити мінімальну кількість монет для довільного набору номіналів.
- Алгоритм динамічного програмування гарантовано знаходить оптимальне рішення незалежно від набору монет, але вимагає значних обчислювальних ресурсів при роботі з великими сумами.

## Висновок

Алгоритм динамічного програмування є ідеальним вибором, коли потрібно гарантовано знайти оптимальне рішення, незалежно від набору монет. Він ефективно справляється з різноманітними наборами монет і завжди знаходить мінімальну кількість монет, необхідну для формування заданої суми. Цей підхід особливо корисний у ситуаціях, де різноманіття і непередбачуваність номіналів монет можуть призвести до неправильних результатів при використанні інших алгоритмів. Проте, з огляду на його складність O(m*n), де m - сума грошей, а n - кількість номіналів монет, алгоритм може бути відносно повільним при обробці дуже великих сум.

Жадібний алгоритм виявляється більш практичним при швидкому обчисленні та в ситуаціях, де набір монет дозволяє йому знаходити оптимальне рішення. Він ідеально підходить для систем монет, де застосування жадібної стратегії гарантує оптимальність результату, наприклад, у багатьох реальних валютних системах. Завдяки своїй простоті та ефективності в обраних випадках, жадібний алгоритм може бути значно швидшим за алгоритм динамічного програмування, особливо при роботі з великими сумами і невеликою кількістю різних номіналів монет.

Обираючи між цими двома алгоритмами, важливо зважати на конкретну задачу: якщо потрібна абсолютна впевненість у знаходженні мінімальної кількості монет для будь-якої суми, краще використовувати алгоритм динамічного програмування. Якщо ж швидкість є пріоритетом і набір монет дозволяє жадібному алгоритму бути ефективним, то вибір на користь жадібного алгоритму буде виправданим.