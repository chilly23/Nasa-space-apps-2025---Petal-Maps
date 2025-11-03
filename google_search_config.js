// Google Custom Search API Configuration
// You need to:
// 1. Go to https://developers.google.com/custom-search/v1/introduction
// 2. Get an API key
// 3. Create a Custom Search Engine at https://cse.google.com/cse/
// 4. Get your Search Engine ID

const GOOGLE_SEARCH_CONFIG = {
  apiKey: 'AIzaSyDObv6ZowtHDhU1zmhDSwalW_b-gZn5-j4',
  searchEngineId: '3144ca98089234e28',
  baseUrl: 'https://www.googleapis.com/customsearch/v1'
};

// Function to search for plant images using Google Custom Search
async function searchPlantImage(species) {
  try {
    const query = `${species} plant flower botanical`;
    const url = `${GOOGLE_SEARCH_CONFIG.baseUrl}?key=${GOOGLE_SEARCH_CONFIG.apiKey}&cx=${GOOGLE_SEARCH_CONFIG.searchEngineId}&q=${encodeURIComponent(query)}&searchType=image&num=1`;
    
    const response = await fetch(url);
    const data = await response.json();
    
    if (data.items && data.items.length > 0) {
      return data.items[0].link; // Return the image URL
    }
  } catch (error) {
    console.log(`Google Search API error for ${species}:`, error);
  }
  
  return null;
}

// Alternative: Use Unsplash API (free but requires API key)
const UNSPLASH_CONFIG = {
  accessKey: 'YOUR_UNSPLASH_ACCESS_KEY_HERE',
  baseUrl: 'https://api.unsplash.com/search/photos'
};

async function searchPlantImageUnsplash(species) {
  try {
    const query = `${species} plant flower`;
    const url = `${UNSPLASH_CONFIG.baseUrl}?query=${encodeURIComponent(query)}&per_page=1&client_id=${UNSPLASH_CONFIG.accessKey}`;
    
    const response = await fetch(url);
    const data = await response.json();
    
    if (data.results && data.results.length > 0) {
      return data.results[0].urls.small;
    }
  } catch (error) {
    console.log(`Unsplash API error for ${species}:`, error);
  }
  
  return null;
}
