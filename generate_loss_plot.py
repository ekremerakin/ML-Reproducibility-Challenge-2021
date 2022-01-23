import matplotlib.pyplot as plt
import glob

paths = glob.glob('warmup/c100/*/*/*/*.log')

# Readingn the logs
logs = []
for path in paths:
    with open(path) as f:
       logs.append(f.readlines())

# Fetching accuracies from the logs
accuracies = []
for lines in logs:
    temp = []
    for i, line in enumerate(lines):
        if i==50:
            break
        acc_index = line.find('Accuracy')
        temp.append(float(line[acc_index+10:acc_index+15]))
    accuracies.append(temp)

print(len(accuracies[0]))

print(len(accuracies[1]))
print(len(accuracies[2]))
print(len(accuracies[3]))
# Plotting the results

labels = ['50sym_warmup0', '50sym_warmup10', '50sym_warmup20', '50sym_warmup30']
plt.figure(figsize=(15, 15))

for i, t in enumerate(accuracies):
    plt.plot(t, label=labels[i])

plt.legend()
plt.show()