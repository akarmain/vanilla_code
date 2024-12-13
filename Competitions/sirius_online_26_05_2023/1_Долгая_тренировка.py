"""
Женя готовится к городским спортивным соревнованиям, где хочет показать себя самым сильным.
Он тренируется по системе шаолиньских монахов. Тренировка должна состоять из 𝑁 подходов,
каждый из которых длится 𝑀 минут и 𝑆 секунд, между каждой парой подряд идущих подходов должен быть перерыв длительностью 𝑃 секунд.
Помогите Жене определить, сколько всего времени займёт тренировка.

Ввод
4
3
24
70
Вывод
17
6
"""

all_pod = int(input())
time_pod_M = int(input())
time_pod_S = int(input())
time_otd_S = int(input())
total_time_approaches = all_pod * (time_pod_M * 60 + time_pod_S)
total_time_breaks = (all_pod - 1) * time_otd_S
total_training_time = total_time_approaches + total_time_breaks
minutes = total_training_time // 60
seconds = total_training_time % 60
print(minutes)
print(seconds)