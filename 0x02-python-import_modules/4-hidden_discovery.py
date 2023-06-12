#!/usr/bin/python3
# 4-hidden_discovery.py

if __name__ == "__main__":
    import hidden_4

    hidden_discovery = dir(hidden_4)

    for j in range(len(hidden_discovery)):
    if hidden_discovery[j][0] != '_' and hidden_discovery[j][1] != '_':
    print(hidden_discovery[j])
