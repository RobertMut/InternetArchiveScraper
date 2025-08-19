import string
import sys
from dataclasses import fields

import internetarchive as ia

fields=['identifier', 'title', 'language']

def get_items(collection, language = None):
    return ia.search_items(f'collection:{collection}{f' AND language:{language}' if language else string.whitespace}', fields=fields)

if __name__ == '__main__':
    if sys.argv.count != 2:
        print("Usage: python main.py <config_file> <collection_to_search> <optional:language>")
        sys.exit(1)
    
    collection_to_search = sys.argv[1]
    language = sys.argv[2] if sys.argv.count == 3 else None
    ia.configure(config_file=sys.argv[0])
    
    results = get_items(collection_to_search, )
    
    with open('entries.csv', 'w') as csv_file:
        csv_file.write('identifier,title\n')
        for item in results:
            csv_file.write(f"{item['identifier']},{item['title']}\n")        
    print("Results written to entries.csv")
    sys.exit(0)