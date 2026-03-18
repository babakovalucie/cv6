import signal_plot_ops as ops

data = ops.load_signals_from_txt("ekg_signal.txt")

print(f"Min: {ops.signal_min(data)}")
print(f"Max: {ops.signal_max(data)}")
print(f"Avg: {ops.signal_avg(data)}")

ops.plot_signal(data)
