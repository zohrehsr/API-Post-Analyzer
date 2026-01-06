import json
import requests

def fetch_posts(api_url):
    try:
       response = requests.get(api_url)
       if response.status_code != 200:
           print(f"Error: API returned status code {response.status_code}")
           return None
       return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Network error : {e}") 
        return None


def analyze_posts(posts, user_id = None):
    if posts is None:
        print("No posts to analyze.")
        return None

    titles = [post["title"] for post in posts]
    filtered_posts = [post for post in posts if user_id is None or post["userId"] == user_id]
    

    return {
        "total_posts": len(posts),
        "titles" : titles,
        "filtered_posts" : filtered_posts
    }

def main() :
    api_url = 'https://jsonplaceholder.typicode.com/posts'
    posts = fetch_posts(api_url)

    user_input = input("Enter userId to filter posts (or press Enter to skip): ")
    if user_input.strip() == "":
        user_id = None
    else:
        try:
            user_id = int(user_input)
        except ValueError:
            print("Invalid input. No filter will be applied.")
            user_id = None

    result = analyze_posts(posts, user_id=user_id)

    if result is not None:
        print("Total posts: ", result["total_posts"])
        print("Title of first 5 posts:", result["titles"][:5])
        print("Filtered posts count:", len(result["filtered_posts"]))

        with open("api_results.txt", "w", encoding="utf-8") as f:
            f.write(f"Total posts: {result['total_posts']}\n")
            f.write(f"Filtered posts count: {len(result['filtered_posts'])}\n")
            f.write("Titles of first 10 posts:\n")
            for title in result["titles"][:10]:
                f.write(f"- {title}\n")

if __name__ == "__main__":
    main()
