row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

column_position = int(position[0])
row_position = int(position[1])

# selected_row = map[row_position-1]
# selected_row[column_position-1] = "X"
# or

map[row_position-1][column_position-1] = "X"

print(f"{row1}\n{row2}\n{row3}")