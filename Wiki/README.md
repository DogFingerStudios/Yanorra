## Info Panel

The Info Panel is a YAML structure at the top of the Wiki pages (aka as Frontmatter) that provides two purposes:

- indexing and categorization of the page for search and navigation purposes
- providing a structured summary of key information about the subject of the page, which can be displayed in a sidebar or info box on the page itself

### Indexing and Categorization

The first part of the Info Panel consists of key-value pairs that categorize the page. This categorization helps layout the links of the website, and also allows for filtering and searching across the wiki. The main keys used for categorization include:
- `id`: a unique identifier for the page, written in lowercase, with non-alphanumeric characters omitted and the remaining words pushed together (e.g. "Saint Aveline" becomes "saintaveline", "Gate 43" becomes "gate43", "S'Tsutodo" becomes "stsutodoh").
- `category`: a broad category that the subject of the page falls under (e.g. "places", "people", "events", "concepts", etc.)
- `subcategory`: a more specific category that further classifies the subject (e.g. "island", "city", "nation", "historical figure", "cultural practice", etc.)

## Website Navigation

```
Search...

Places
  Nations
  Cities
  Islands
  Waters
  Regions

History
  Events
  Wars
  Timeline  

Lore
  Myths
  Mysteries
  World Lore

Reference
  Calendar
  Glossary
  All Pages
```