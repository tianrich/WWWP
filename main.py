import requests
import json

def check_wordpress_vulnerabilities(url):
  """Checks a WordPress website for vulnerabilities.

  Args:
    url: The URL of the WordPress website to check.

  Returns:
    A list of vulnerabilities, if any.
  """

  response = requests.get(f"https://wpvulndb.com/api/v3/wordpresses/{url}")
  if response.status_code == 200:
    data = json.loads(response.content)
    return data["vulnerabilities"]
  else:
    return []

def main():
  """Checks the WordPress website for vulnerabilities."""

  url = input("Enter the URL of your WordPress website: ")
  vulnerabilities = check_wordpress_vulnerabilities(url)

  if vulnerabilities:
    print("The following vulnerabilities were found on your website:")
    for vulnerability in vulnerabilities:
      print(f"* {vulnerability['name']}")
  else:
    print("No vulnerabilities were found on your website.")

if __name__ == "__main__":
  main()
