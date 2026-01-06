# API Post Analyzer

A small Python project to fetch posts from a public API, analyze them, and filter by `userId`.

## Features
- Fetch data from a public API
- Count total posts
- Extract post titles
- Filter posts by `userId` (user input)
- Save output to a file `api_results.txt`
- Handle network errors and invalid status codes

## Installation & Run
1. Make sure Python 3.7+ is installed
2. Install the required package:
```bash
pip install requests
3. Run the script:
```bash
python api_post_analyzer.py
4. Enter a userId to filter posts or press Enter to skip filtering.

## Example
Input:
Enter userId to filter posts (or press Enter to skip): 1

Console Output:
Total posts: 100
Titles of first 5 posts: ['sunt aut facere...', 'qui est esse...', 'ea molestias quasi...', 'eum et est occaecati', 'nesciunt quas odio']
Filtered posts count: 10

Output saved to api_results.txt:
Total posts: 100
Filtered posts count: 10
Titles of first 10 posts:
- sunt aut facere...
- qui est esse...
- ea molestias quasi...
- eum et est occaecati
- nesciunt quas odio
- dolorem eum magni eos aperiam quia
- magnam facilis autem
- dolorem dolore est ipsam
- nesciunt iure omnis dolorem tempora et accusantium
- optio molestias id quia eum

