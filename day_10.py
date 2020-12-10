from collections import Counter

with open('data_day_10.txt') as file:
    data = file.read()

adapters = [int(x) for x in data.split('\n')]
adapters = sorted(adapters)

latest_adapter = 0
i = 1
diff = Counter()

verified_adapters = []

while i < 4:
    if (latest_adapter + i) in adapters:
        diff[i] += 1
        latest_adapter += i
        verified_adapters.append(latest_adapter)
        i = 1
    else:
        i += 1

diff[3] += 1

print(diff[1] * diff[3])

verified_adapters.append(verified_adapters[-1] + 3)

ans = {0: 1}

for adapter in verified_adapters:
    ans[adapter] = ans.get(adapter - 1, 0) + ans.get(adapter - 2, 0) + ans.get(adapter - 3, 0)

print(ans[verified_adapters[-1]])
