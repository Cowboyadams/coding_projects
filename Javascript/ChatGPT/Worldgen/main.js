// Create an empty array to store the chunks
const chunks = [];

// Create the Mother Chunk and add it to the chunks array
const motherChunk = { num: 1, loc: [0, 0], heat: 3 };
chunks.push(motherChunk);

// Generate the other chunks and add them to the chunks array
for (let i = 2; i <= 25; i++) {
  // Determine the location of the new chunk relative to the mother chunk
  const x = (i % 5) - 3;
  const y = Math.floor(i / 5) - 2;
  const loc = [x, y];

  // Determine the initial heat level of the new chunk
  let heat;
  if (Math.random() < 0.2) {
    heat = Math.floor(Math.random() * 5) + 1;
  } else {
    const adjacentChunks = chunks.filter(chunk => {
      return (
        Math.abs(chunk.loc[0] - x) <= 1 && Math.abs(chunk.loc[1] - y) <= 1
      );
    });
    const avgHeat =
      adjacentChunks.reduce((sum, chunk) => sum + chunk.heat, 0) /
      adjacentChunks.length;
    heat = Math.round(avgHeat);
    if (Math.random() < 0.5) {
      heat = Math.max(heat - 1, 1);
    } else {
      heat = Math.min(heat + 1, 5);
    }
  }

  // Create the new chunk object and add it to the chunks array
  const chunk = { num: i, loc: loc, heat: heat };
  chunks.push(chunk);
}

// Display the chunks matrix
for (let y = -2; y <= 2; y++) {
  let row = "";
  for (let x = -2; x <= 2; x++) {
    const chunk = chunks.find(chunk => {
      return chunk.loc[0] === x && chunk.loc[1] === y;
    });
    if (chunk) {
      row += `{ num: ${chunk.num}, loc: [${chunk.loc}], heat: ${chunk.heat} } `;
    } else {
      row += "{ empty } ";
    }
  }
  console.log(row);
}
