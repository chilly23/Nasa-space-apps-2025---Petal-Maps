// Fast local plant icons - no API calls needed!

// Plant emoji mapping for different species
const PLANT_EMOJIS = {
  // Common flower types
  'rose': '🌹',
  'tulip': '🌷', 
  'sunflower': '🌻',
  'daisy': '🌼',
  'hibiscus': '🌺',
  'cherry': '🌸',
  'blossom': '🌿',
  'herb': '🌿',
  'mint': '🌿',
  'clover': '🍀',
  'maple': '🍁',
  'cactus': '🌵',
  'palm': '🌴',
  'tree': '🌳',
  'seedling': '🌱',
  'leaf': '🍃',
  'fallen': '🍂',
  'bouquet': '💐',
  
  // Default fallback
  'default': '🌱'
};

// Plant category mapping
const PLANT_CATEGORIES = {
  'flower': '🌸',
  'tree': '🌳',
  'shrub': '🌿',
  'grass': '🌾',
  'vine': '🌿',
  'fern': '🌿',
  'moss': '🌿',
  'succulent': '🌵',
  'cactus': '🌵',
  'palm': '🌴',
  'bush': '🌿',
  'herb': '🌿',
  'weed': '🌱',
  'plant': '🌱'
};

// Color mapping for different plant families
const PLANT_COLORS = {
  'rose': '#FF69B4',     // Hot pink
  'tulip': '#FFB6C1',    // Light pink
  'sunflower': '#FFD700', // Gold
  'daisy': '#FFFFFF',    // White
  'hibiscus': '#FF1493', // Deep pink
  'cherry': '#FFB6C1',   // Light pink
  'clover': '#32CD32',   // Lime green
  'mint': '#98FB98',     // Pale green
  'cactus': '#228B22',   // Forest green
  'palm': '#228B22',     // Forest green
  'tree': '#8B4513',     // Saddle brown
  'default': '#32CD32'   // Lime green
};

// Function to get plant emoji based on species name
function getPlantEmoji(species) {
  if (!species) return PLANT_EMOJIS.default;
  
  const lowerSpecies = species.toLowerCase();
  
  // Direct match
  if (PLANT_EMOJIS[lowerSpecies]) {
    return PLANT_EMOJIS[lowerSpecies];
  }
  
  // Partial match
  for (const [key, emoji] of Object.entries(PLANT_EMOJIS)) {
    if (lowerSpecies.includes(key)) {
      return emoji;
    }
  }
  
  // Category match
  for (const [category, emoji] of Object.entries(PLANT_CATEGORIES)) {
    if (lowerSpecies.includes(category)) {
      return emoji;
    }
  }
  
  return PLANT_EMOJIS.default;
}

// Function to get plant color based on species name
function getPlantColor(species) {
  if (!species) return PLANT_COLORS.default;
  
  const lowerSpecies = species.toLowerCase();
  
  // Direct match
  if (PLANT_COLORS[lowerSpecies]) {
    return PLANT_COLORS[lowerSpecies];
  }
  
  // Partial match
  for (const [key, color] of Object.entries(PLANT_COLORS)) {
    if (lowerSpecies.includes(key)) {
      return color;
    }
  }
  
  return PLANT_COLORS.default;
}

// Function to create a beautiful SVG icon instantly
function createPlantIcon(species) {
  const emoji = getPlantEmoji(species);
  const color = getPlantColor(species);
  
  return `data:image/svg+xml;base64,${btoa(`
    <svg width="32" height="32" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <radialGradient id="grad" cx="50%" cy="30%" r="70%">
          <stop offset="0%" style="stop-color:${color};stop-opacity:1" />
          <stop offset="100%" style="stop-color:${color}CC;stop-opacity:1" />
        </radialGradient>
      </defs>
      <circle cx="16" cy="16" r="15" fill="url(#grad)" stroke="white" stroke-width="2"/>
      <text x="16" y="22" text-anchor="middle" font-size="16" font-family="Arial, sans-serif">${emoji}</text>
    </svg>
  `)}`;
}

// Function to create a simple colored circle (fastest option)
function createSimplePlantIcon(species) {
  const color = getPlantColor(species);
  
  return `data:image/svg+xml;base64,${btoa(`
    <svg width="24" height="24" xmlns="http://www.w3.org/2000/svg">
      <circle cx="12" cy="12" r="10" fill="${color}" stroke="white" stroke-width="2"/>
    </svg>
  `)}`;
}
