import random

# Define a Chunk class to hold each chunk's data
class Chunk:
    def __init__(self, num, loc, heat):
        self.num = num
        self.loc = loc
        self.heat = heat

# Define a function to generate the temperature of a chunk based on its adjacent chunks
def generate_heat(chunks, curr_chunk):
    adj_temps = []
    for chunk in chunks:
        if chunk is not curr_chunk:
            # Calculate distance between current chunk and adjacent chunk
            dist = abs(chunk.loc[0] - curr_chunk.loc[0]) + abs(chunk.loc[1] - curr_chunk.loc[1])
            if dist == 1:
                # If adjacent chunk is directly adjacent, append its temperature to list
                adj_temps.append(chunk.heat)
    # Calculate the average temperature of adjacent chunks and round to nearest integer
    avg_temp = round(sum(adj_temps) / len(adj_temps)) if len(adj_temps) > 0 else 3
    # Calculate a random chance of changing the temperature
    if random.random() < 0.2:
        curr_chunk.heat = avg_temp
    else:
        # Calculate a random chance of increasing or decreasing the temperature by 1
        if random.random() < 0.5:
            curr_chunk.heat = min(avg_temp + 1, 5)
        else:
            curr_chunk.heat = max(avg_temp - 1, 1)
    return curr_chunk.heat

# Define a function to create the matrix of chunks
def create_matrix():
    # Create mother chunk with num 1, loc (0,0), and initial heat of 3
    chunks = [Chunk(1, (0,0), 3)]
    for i in range(2, 26):
        # Determine location of new chunk based on its num
        x = (i - 2) % 5 - 2
        y = 2 - (i - 2) // 5
        loc = (x, y)
        # Generate heat for new chunk based on adjacent chunks
        new_heat = generate_heat(chunks, Chunk(i, loc, 0))
        # Create new chunk with generated data
        new_chunk = Chunk(i, loc, new_heat)
        chunks.append(new_chunk)
    return chunks

# Define a function to display the matrix of chunks
def display_matrix(chunks):
    # Create empty matrix
    matrix = [[' ']*10 for _ in range(10)]
    for chunk in chunks:
        # Calculate matrix coordinates based on chunk location
        x = chunk.loc[0] + 2
        y = 2 - chunk.loc[1]
        # Format chunk data as string
        chunk_str = f"num: {chunk.num}, loc: {chunk.loc}, heat: {chunk.heat}"
        # Add chunk data to matrix
        matrix[y][x] = chunk_str
    # Print matrix
    for row in matrix:
        print('| ' + ' | '.join(row) + ' |')

# Main function to run the program
def main():
    chunks = create_matrix()
    display_matrix(chunks)

if __name__ == '__main__':
    main()
