import sys

def print_stats(total_size, status_counts):
    """Prints the file size and the number of lines per status code."""
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        print(f"{code}: {status_counts[code]}")

total_size = 0
status_counts = {}
valid_status_codes = {200, 301, 400, 401, 403, 404, 405, 500}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 7:
            continue

        try:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
            
            total_size += file_size
            if status_code in valid_status_codes:
                status_counts[status_code] = status_counts.get(status_code, 0) + 1
        except ValueError:
            continue
        
        line_count += 1
        if line_count % 10 == 0:
            print_stats(total_size, status_counts)

except KeyboardInterrupt:
    print_stats(total_size, status_counts)
    raise
