import sys

def show_help():
    print("Usage: go2web <url>")
    print("go2web -u <url> - Update something")
    print("go2web -h - Show this help message")
    print("go2web -s <search-term> - Search for something and print top 10 results")

if len(sys.argv) < 2:
    show_help()
    sys.exit(1)

flag = sys.argv[1]

if flag == '-h':
    show_help()
elif flag == '-u':
    if len(sys.argv) < 3:
        print("Error: URL is required for update")
    else:
        url = sys.argv[2]
        print(f"URL requested {url}...")
elif flag == '-s':
    if len(sys.argv) < 3:
        print("Error: missing search term")
    else:
        url = sys.argv[2]
        print(f"Search term: {url}...")
else:
    print("Unknown option", flag)
    show_help()