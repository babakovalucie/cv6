import matplotlib.pyplot as plt

def load_signals_from_txt(path):
    values = []
    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            values.append(float(line))
    return values

def signal_min(values):
    return min(values)

def signal_max(values):
    return max(values)

def signal_avg(values):
    return sum(values) / len(values)

def plot_signal(values):
    plt.plot(values)
    plt.show()
    return

if __name__ == "__main__":
    data = load_signals_from_txt("ekg_signal.txt")

    print(f"Min: {signal_min(data)}")
    print(f"Max: {signal_max(data)}")
    print(f"Avg: {signal_avg(data)}")
    
    plot_signal(data)
