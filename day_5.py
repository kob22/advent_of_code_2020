with open('data_day_5.txt', 'r') as data:
    boarding_passes = data.read().splitlines()

seats_id = set()

for boarding_pass in boarding_passes:
    min_row = 0
    max_row = 127
    for letter in boarding_pass[:7]:
        mid_row = (max_row + min_row) // 2
        if letter == 'F':
            max_row = mid_row
        if letter == 'B':
            min_row = mid_row + 1

    min_col = 0
    max_col = 7

    for letter in boarding_pass[7:]:
        mid_col = (max_col + min_col) // 2
        if letter == 'L':
            max_col = mid_col
        if letter == 'R':
            min_col = mid_col + 1

    seats_id.add(min_row * 8 + min_col)

print(max(seats_id))

sorted_seats_id = sorted(seats_id)

prv_seat = sorted_seats_id[0]
missing_seat = None

for seat_id in sorted_seats_id[1:]:
    if seat_id - 1 != prv_seat:
        missing_seat = seat_id-1
    prv_seat = seat_id

print(missing_seat)

